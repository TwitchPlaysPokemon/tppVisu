'''
Created on 02.05.2015

@author: Felk
'''
from __future__ import division

from tppVisu.move import MoveCategory
from tppVisu.tables import moveFuncs, abilityFuncs
from tppVisu.tables.typeEffs import getEff
from tppVisu.util import Eff, enum
from copy import deepcopy
from collections import namedtuple

Kind = enum(normal='normal', status='status', ohko='ohko', notVisuable='notVisuable')
#class Kind(Enum):
#    normal      = 'normal'
#    status      = 'status'
#    ohko        = 'ohko'
#    notVisuable = 'notVisuable'

class MoveResult(object):
    def __init__(self, env, accuracy, speed, kind=Kind.normal, eff=Eff.NORMAL, damage=None):
        self.env = env
        if accuracy == None:
            self.accuracy = None
        else:
            self.accuracy = int(accuracy)
        self.speed = int(speed)
        self.kind = kind
        self.eff  = eff
        if damage == None:
            self.damage = None
        else:
            self.damage = tuple(int(D) for D in damage)
        
SetupResult = namedtuple('Setupresult', 'blues reds env')

def calcSetup(blue, red, env):
    
    # work on local copies
    blue = deepcopy(blue)
    red  = deepcopy(red)
    env  = deepcopy(env)
    
    abilityFuncs.call(blue.ability, blue, red, env)
    abilityFuncs.call(red.ability, red, blue, env)
    
    blues = [calcMove(move, blue, red, env) for move in blue.moves]
    reds  = [calcMove(move, red, blue, env) for move in red.moves]
    
    return SetupResult(blues, reds, env)
    

def calcMove(move, pkmn, opp, env):
    
    ovwr = moveFuncs.call(move, pkmn, opp, env)
    #moveNotice = ovwr.notice
    
    if not move.visuable:
        return MoveResult(env, move.accuracy, pkmn.SPE.get(), kind=Kind.notVisuable)
    
    #weather effects
    for mon in [pkmn,opp]:
        if env.weather == "sun":
            mon.typeMults.fire *= 2
            mon.typeMults.water /= 2
        if env.weather == "rain":
            mon.typeMults.fire /= 2
            mon.typeMults.water *= 2
        if env.weather == "sandstorm":
            if "rock" in [mon.type1,mon.type2]:
                mon.SPD *= 1.5
    if env.weather == "fog":
        if move.accuracy != None: move.accuracy *= 6.0/10
        #Hail doesn't change any stats or anything
    
    # calculate final accuracy
    accu = None
    if move.accuracy != None and move.accuracy >= 0: accu = move.accuracy * (pkmn.ACC.get() / opp.EVA.get())
    # "no accuracy" modifier might be saved as -1
    
    # accuracy is a fixed value for OHKO moves
    if move.isOHKOMove():
        accu = 30 + (pkmn.level - opp.level)
        if accu > 100: accu = 100
        if accu < 30: move.disable()
        
    if move.isDisabled():
        return MoveResult(env, accu, pkmn.SPE.get(), eff=Eff.NOT)
    
    ##########################################################
    
    # TODO don't calculate para-nerf here
    if pkmn.status == 'par':
        pkmn.SPE *= pkmn.parMult
        
    if move.category == MoveCategory.nonDamaging:
        # No more calculating needed
        return MoveResult(env, accu, pkmn.SPE.get(), kind=Kind.status)
    elif move.category == MoveCategory.physical:
        valueAtkDef = pkmn.ATK.get() / opp.DEF.get()
    else:
        valueAtkDef = pkmn.SPA.get() / opp.SPD.get()
        
    StabModifier = 1
    if pkmn.type1 == move.type: StabModifier *= pkmn.stab
    if pkmn.type2 == move.type: StabModifier *= pkmn.stab
    
    ChangedMultMultiplier = getEff(move.type, opp.type1)
    if opp.type2: ChangedMultMultiplier *= getEff(move.type, opp.type2)
    
    TypeModifier = getattr(pkmn.typeMults,move.type)
    
    
    
    if ChangedMultMultiplier == 0:
        ChangedMultMultiplier = pkmn.effs.NOT
    elif ChangedMultMultiplier < 1:
        ChangedMultMultiplier *= pkmn.effs.WEAK * 2 # scale default (0.5) to 1 to act as multiplier in
    elif ChangedMultMultiplier > 1:
        ChangedMultMultiplier *= pkmn.effs.SUPER * 0.5 # scale default (2) to 1 to act as multiplier
    else:
        ChangedMultMultiplier *= pkmn.effs.NORMAL
      
    if ChangedMultMultiplier == 0 or TypeModifier == 0:
        eff = Eff.NOT
    elif ChangedMultMultiplier < 1:
        eff = Eff.WEAK
    elif ChangedMultMultiplier > 1:
        eff = Eff.SUPER
    else:
        eff = Eff.NORMAL
    
    if move.isOHKOMove():
        return MoveResult(env, accu, pkmn.SPE.get(), kind=Kind.ohko, eff=eff)
    
    power = ovwr.power if ovwr.power != None else (move.power, move.power)
    
    calcSetup = lambda P: (((2 * pkmn.level + 10) / 250) * valueAtkDef * P + 2) * StabModifier * ChangedMultMultiplier * TypeModifier
    predamage = tuple(calcSetup(P) for P in power)
    
    # BRN attack nerf
    if pkmn.status == 'brn' and move.category == MoveCategory.physical:
        predamage = tuple(D * pkmn.brnMult for D in predamage)
        
    damage = ovwr.damage if ovwr.damage != None else (int(predamage[0] * 0.85)* move.minMaxHits[0], int(predamage[1]) * move.minMaxHits[1])
    damage = tuple(max(0, D) for D in damage)

    return MoveResult(env, accu, pkmn.SPE.get(), eff=eff, damage=damage)
