'''
Created on 02.05.2015

@author: Felk
'''
from enum import Enum

from tppVisu.move import MoveCategory
from tppVisu.tables import moveFuncs, abilityFuncs
from tppVisu.tables.typeEffs import getEff
from tppVisu.util import Eff
from copy import deepcopy
from tppVisu.move import Move
from collections import namedtuple


class Kind(Enum):
    normal      = 'normal'
    status      = 'status'
    ohko        = 'ohko'
    notVisuable = 'notVisuable'

class MoveResult(object):
    def __init__(self, env, accuracy, speed, kind=Kind.normal, eff=Eff.NORMAL, damage=None):
        self.env = env
        self.accuracy = int(accuracy)
        self.speed = int(speed)
        self.kind = kind
        self.eff  = eff
        self.damage = damage
        
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
        
    modifierStab = 1
    if pkmn.type1 == move.type: modifierStab *= pkmn.stab
    if pkmn.type2 == move.type: modifierStab *= pkmn.stab
    
    modifierType = getEff(move.type, opp.type1)
    if opp.type2: modifierType *= getEff(move.type, opp.type2)
    
    modifierPost = getattr(pkmn.typeMults, move.type)
    
    if modifierType == 0 or modifierPost == 0:
        eff = Eff.NOT
        modifierType = pkmn.effs.NOT
    elif modifierType < 1:
        eff = Eff.WEAK
        modifierType *= pkmn.effs.WEAK * 2 # scale default (0.5) to 1 to act as multiplier
    elif modifierType > 1:
        eff = Eff.SUPER
        modifierType *= pkmn.effs.SUPER * 0.5 # scale default (2) to 1 to act as multiplier
    else:
        eff = Eff.NORMAL
        modifierType *= pkmn.effs.NORMAL
    
    if move.isOHKOMove():
        return MoveResult(env, accu, pkmn.SPE.get(), kind=Kind.ohko, eff=eff)
    
    power = ovwr.power if ovwr.power != None else (move.power, move.power)
    
    calcSetup = lambda P: (((2 * pkmn.level + 10) / 250) * valueAtkDef * P + 2) * modifierStab * modifierType * modifierPost
    predamage = tuple(calcSetup(P) for P in power)
    
    # BRN attack nerf
    if pkmn.status == 'brn' and move.category == MoveCategory.physical:
        predamage = tuple(D * pkmn.brnMult for D in predamage)
        
    damage = ovwr.damage if ovwr.damage != None else (predamage[0] * move.minMaxHits[0] * 0.85, predamage[1] * move.minMaxHits[1])
    damage = tuple(max(0, D) for D in damage)

    return MoveResult(env, accu, pkmn.SPE.get(), eff=eff, damage=damage)
