'''
Created on 08.05.2015

@author: Felk
'''
from tppVisu.calculator import calcSetup

def buildDictMatch(blues, reds, env):
    match = []
    for i in range(len(blues)):
        match.append([])
        for j in range(len(reds)):
            match[i].append(buildDictSetup(blues[i], reds[j], env))
    return match
            

def buildDictSetup(blue, red, env):
    blues, reds, envOut = calcSetup(blue, red, env)
    setup = {}
    setup['weather'] = envOut.weather
    setup['blue'] = []
    setup['red'] = []
    for b in blues:
        data = {}
        data['kind'] = b.kind.value
        data['eff'] = b.eff.value
        data['damage'] = b.damage
        data['accuracy'] = b.accuracy
        data['speed'] = b.speed
        setup['blue'].append(data)
    for r in reds:
        data = {}
        data['kind'] = r.kind.value
        data['eff'] = r.eff.value
        data['damage'] = r.damage
        data['accuracy'] = r.accuracy
        data['speed'] = r.speed
        setup['red'].append(data)
        
    return setup

