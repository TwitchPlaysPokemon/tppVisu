'''
Created on 08.05.2015

@author: Felk
'''
from tppVisu.calculator import calcMove

def buildJsonSetup(pkmn, opp, env):
    setup = {}
    setup['blue'] = []
    setup['red'] = []
    for move in pkmn.moves:
        res = calcMove(move, pkmn, opp, env)
        data = {}
        data['kind'] = res.kind.value
        data['eff'] = res.eff.value
        data['damage'] = res.damage
        data['accuracy'] = res.accuracy
        setup['blue'].append(data)
    for move in opp.moves:
        res = calcMove(move, opp, pkmn, env)
        data = {}
        data['kind'] = res.kind.value
        data['eff'] = res.eff.value
        data['damage'] = res.damage
        data['accuracy'] = res.accuracy
        setup['red'].append(data)
        
    return setup

