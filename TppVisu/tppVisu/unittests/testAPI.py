'''
Created on 28.04.2015

@author: Felk
'''
from __future__ import division

import unittest

from tppVisu.move import MoveCategory
from tppVisu.api import buildDictSetup
import json
from tppVisu.unittests.visuUnittest import VisuTestCase


class TppVisuApiTests(VisuTestCase):
    
    def test_json1(self):
        p1 = self.genPkmn(moves=[self.genMove(category=MoveCategory.nonDamaging), self.genMove(category=MoveCategory.special)])
        dic = buildDictSetup(p1, self.genPkmn(), self.genEnv())
        self.assertEqual(json.dumps(dic, sort_keys=True), '{"blue": [{"accuracy": 100, "damage": null, "eff": "normal", "kind": "status", "speed": 100}, {"accuracy": 100, "damage": [109, 129], "eff": "normal", "kind": "normal", "speed": 100}], "red": [{"accuracy": 100, "damage": [109, 129], "eff": "normal", "kind": "normal", "speed": 100}], "weather": "none"}')
    

if __name__ == '__main__':
    unittest.main()
    
