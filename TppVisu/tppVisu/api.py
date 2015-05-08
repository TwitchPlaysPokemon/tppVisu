'''
Created on 08.05.2015

@author: Felk
'''
from tppVisu.calculator import calcMove

def buildDictSetup(pkmn, opp, env):
    setup = {}
    setup['blue'] = []
    setup['red'] = []
    for i in range(len(pkmn.moves)):
        res = calcMove(i, pkmn, opp, env)
        data = {}
        data['kind'] = res.kind.value
        data['eff'] = res.eff.value
        data['damage'] = res.damage
        data['accuracy'] = res.accuracy
        setup['blue'].append(data)
    for i in range(len(opp.moves)):
        res = calcMove(i, opp, pkmn, env)
        data = {}
        data['kind'] = res.kind.value
        data['eff'] = res.eff.value
        data['damage'] = res.damage
        data['accuracy'] = res.accuracy
        setup['red'].append(data)
        
    return setup

