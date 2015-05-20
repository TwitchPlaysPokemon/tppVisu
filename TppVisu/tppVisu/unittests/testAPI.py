'''
Created on 28.04.2015

@author: Felk
'''
from __future__ import division

import json
import unittest

from tppVisu.api import buildDictSetup, buildDictOldApi
from tppVisu.move import MoveCategory
from tppVisu.pokemon import Gender
from tppVisu.unittests.visuUnittest import VisuTestCase


class TppVisuApiTests(VisuTestCase):
    
    def test_json1(self):
        p1 = self.genPkmn(moves=[self.genMove(category=MoveCategory.nonDamaging), self.genMove(category=MoveCategory.special)])
        dic = buildDictSetup(p1, self.genPkmn(), self.genEnv())
        self.assertEqual(json.dumps(dic, sort_keys=True), '{"blue": [{"accuracy": 100, "damage": null, "eff": "normal", "kind": "status", "speed": 100}, {"accuracy": 100, "damage": [109, 129], "eff": "normal", "kind": "normal", "speed": 100}], "red": [{"accuracy": 100, "damage": [109, 129], "eff": "normal", "kind": "normal", "speed": 100}], "weather": "none"}')
    
    def test_jsonOld1(self):
        # testing "old php api" call. Use an actual old result as sample
        data = json.load(open('../oldApiSample.json'))
        
        blues = []
        reds = []
        limit = len(data['blue'])
        for i, p in enumerate(data['blue'] + data['red']):
            pkmn = {}
            t2 = p['type2'] if p['type2'] != '-' else None
            gender = Gender.none
            if p['gender'] == 'm': gender = Gender.male
            elif p['gender'] == 'f': gender = Gender.female
            pkmn = self.genPkmn(name=p['name'], id=p['id'], type1=p['type1'], type2=t2, gender=gender, ability=p['ability'],
                stats=self.genStats(p['stats']['hp'], p['stats']['atk'], p['stats']['def'], p['stats']['satk'], p['stats']['sdef'], p['stats']['spd']))
            pkmn.moves = []
            for m in p['moves']:
                category = MoveCategory.nonDamaging
                if m['category'] == 'physical': category = MoveCategory.physical
                elif m['category'] == 'special': category = MoveCategory.special
                elif m['category'] == 'ohko': category = MoveCategory.physical
                accuracy = m['accuracy'] if m['accuracy'] > 0 else None
                pkmn.moves.append(self.genMove(name=m['name'], type=m['type'], pp=m['pp'], power=m.get('power', None), accuracy=accuracy, category=category))
            (blues if i < limit else reds).append(pkmn)
            
        json.dump(buildDictOldApi(blues, reds, self.genEnv(weather='none')), open('../test.json', 'w+'), indent=4)
            
    

if __name__ == '__main__':
    unittest.main()
    
