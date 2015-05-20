'''
Created on 08.05.2015

@author: Felk

"outer" API-functions for the TPP visualizer. Calls the "real" API-function calcSetup() in calculator module.
Packs the data into dictionaries for easy JSON-conversion.
NOTE: Data like the ability-visuable-flag, move-anomaly-notices or move-priorities are currently NOT included.
      They are inferred at Pokemon/Move-object-creation and available in those objects. They are not returned by calcSetup() or calcMove().
      They could be included here somewhere, but currently just aren't. They might also only be important for the Web-Version of the visualizer.
'''




from __future__ import division, print_function

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
    for ib, b in enumerate(blues):
        match.append([])
        for r in reds:
            match[ib].append(buildDictSetup(b, r, env))
    return match
            

def buildDictSetup(blue, red, env):
    '''builds a dictionary from a single setup. Takes 2 pokemons "blue" and "red" plus an Environment (see util).
    Calls directly to the API.
    
    The built dictionary looks like this in JSON:
    {
        "weather": String,             # none, sun, rain, sandstorm, hail or fog
        "blue": [
            {
                "kind": String,        # normal, status, ohko or notVisuable
                "speed": Number,       # final speed stat value.
                "eff": String,         # not, weak, normal or super.
                "damage": [Numbers],   # 2 numbers: min and max damage. null if not applicable
                "accuracy": Number     # final accuracy value as integer (0-100). null if no modifier (=can't miss)
            }, ...                     # same for each move
        ],
        "red": ...                    # same as above
    }'''
    blues, reds, envOut = calcSetup(blue, red, env)
    setup = {}
    setup['weather'] = envOut.weather
    setup['blue'] = []
    setup['red'] = []
    for b in blues:
        data = {}
        data['kind'] = b.kind
        data['eff'] = b.eff
        data['damage'] = b.damage
        data['accuracy'] = b.accuracy
        data['speed'] = b.speed
        setup['blue'].append(data)
    for r in reds:
        data = {}
        data['kind'] = r.kind
        data['eff'] = r.eff
        data['damage'] = r.damage
        data['accuracy'] = r.accuracy
        data['speed'] = r.speed
        setup['red'].append(data)
    return setup

def buildDictOldApi(blues, reds, env):
    '''Builds a dictionary from a whole match.
    Basically does the same as buildDictMatch(), but returns an extended dictionary mimicing the old php api style.
    Reference: http://pastebin.com/raw.php?i=zct7wJb0 or "oldApiSample.json"
    The old api returned the whole pokemon data with the api results just "woven into".
    NOTE: This dict is significantly different to the old api though!
    
    The built dictionary looks like this in JSON:
    {
        "blue": [
            {
                "id": Number,                                  # national dex number
                "name": String,
                "type1": String,
                "type2": String,                               # can be null if no 2nd type
                "gender": String,                              # m, f or -
                "ability": String
                "ability_description": String,
                "ability_visuable": Boolean,                   # True, if the ability is/was visualizable. False otherwise
                "stats": {                                     # BASE stats
                    "HP": Number,
                    "ATK": Number,
                    "DEF": Number,
                    "SPA": Number,
                    "SPD": Number,
                    "SPE": Number
                },
                "moves": [
                    {
                        "name": String,
                        "description": String,
                        "type": String,
                        "pp", Number,
                        "power": Number,                       # null if not applicable (status move)
                        "accuracy": Number,                    # BASE accuracy, can be null if no modifier (=can't miss)
                        "category": String,                    # physical, special or nonDamaging
                        "priority": Number,                    # move's priority bracket
                        "anomaly": String,                     # null, if the move does nothing special. Else a string (empty, if no additional info) suggesting highlighting.
                        "attacks": [
                            {
                                "kind": String,                # normal, status, ohko or notVisuable.
                                "eff": String,                 # super, normal, weak or not
                                "accuracy": Number,            # final accuracy (0-100), can be null if no modifier (=can't miss)
                                "speed": Number,               # final speed value. Used to determine faster pokemon. NOTE: Also consider priority value
                                "damage": [Number, Number]     # [min, max] or null if not applicable
                            }, ...                             # for each opponent pokemon
                        ]
                    }
                ]
            }, ...                                             # for each pokemon
        ],
        "red": ...                                             # same as above
    }
    '''
    data = buildDictMatch(blues, reds, env)
    
    dic = {'blue': [], 'red': []}
    
    for flagBlue in (True, False):
        for i, p in enumerate(blues if flagBlue else reds):
            poke = {}
            poke['id'] = p.natID
            poke['name'] = p.name
            poke['type1'] = p.type1
            poke['type2'] = p.type2
            poke['gender'] = p.gender
            poke['ability'] = p.ability
            poke['ability_description'] = 'DUMMY'  # TODO
            poke['ability_visuable'] = p.abilityVisuable
            poke['stats'] = {}
            poke['stats']['hp'] = p.HP
            poke['stats']['atk'] = p.ATK.base
            poke['stats']['def'] = p.DEF.base
            poke['stats']['spa'] = p.SPA.base
            poke['stats']['spd'] = p.SPD.base
            poke['stats']['spe'] = p.SPE.base
            poke['moves'] = []
            for im, m in enumerate(p.moves):
                move = {}
                move['name'] = m.name
                move['description'] = 'DUMMY'  # TODO
                move['type'] = m.type
                move['pp'] = m.pp
                move['power'] = m.power
                move['accuracy'] = m.accuracy
                move['category'] = m.category
                move['priority'] = m.priority
                move['anomaly'] = m.anomaly
                if flagBlue:
                    move['attacks'] = [data[i][X]['blue'][im] for X in range(len(reds))]
                else:
                    move['attacks'] = [data[X][i]['red'][im] for X in range(len(blues))]
                poke['moves'].append(move)
            (dic['blue'] if flagBlue else dic['red']).append(poke)
                
    return dic
    
