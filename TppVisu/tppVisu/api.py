'''
Created on 08.05.2015

@author: Felk

"outer" API-functions for the TPP visualizer. Calls the "real" API-function calcSetup() in calculator module.
Packs the data into dictionaries for easy JSON-conversion.
NOTE: Data like the ability-visuable-flag, move-anomaly-notices or move-priorities are currently NOT included.
      They are inferred at Pokemon/Move-object-creation and available in those objects. They are not returned by calcSetup() or calcMove().
      They could be included here somewhere, but currently just aren't. They might also only be important for the Web-Version of the visualizer.
'''
from tppVisu.calculator import calcSetup

def buildDictMatch(blues, reds, env):
    '''builds a dictionary from a whole match. Takes 2 pokemon arrays "blues" and "reds" plus an Environment (see util).
    Calls buildDictSetup multiple times.
    
    The built dictionary looks like this in JSON:
    [                          # array "for each blue"
        [                      # array "for each red against this blue"
            { "weather"... }   # setup-object. See buildDictSetup()
        ]
    ]'''
    match = []
    for i in range(len(blues)):
        match.append([])
        for j in range(len(reds)):
            match[i].append(buildDictSetup(blues[i], reds[j], env))
    return match
            

def buildDictSetup(blue, red, env):
    '''builds a dictionary from a single setup. Takes 2 pokemons "blue" and "red" plus an Environment (see util).
    Calls directly to the API.
    
    The built dictionary looks like this in JSON:
    {
        "weather": String,             # none, sun, rain, sandstorm, hail or fog
        "red": [
            {
                "kind": String,        # normal, status, ohko or notVisuable
                "speed": Number,       # final speed stat value.
                "eff": String,         # not, weak, normal or super.
                "damage": [Numbers],   # 2 numbers: min and max damage. null if not applicable
                "accuracy": Number     # final accuracy value as integer (0-100). null if no modifier (=can't miss)
            }, ...                     # same for each move
        ],
        "blue": ...                    # same as above
    }'''
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

