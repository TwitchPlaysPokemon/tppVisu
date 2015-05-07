'''
Created on 05.07.14

@author: Hlixed
'''

import unittest

from tppVisu.move import MoveCategory, Move
from tppVisu.pokemon import Pokemon, Gender
from tppVisu.tables.typeEffs import getEff
from tppVisu.util import Stats, Environment
from tppVisu.calculator import Eff, calcMove, Kind


class TppVisuTests(unittest.TestCase):
    
    def genStats(self, HP=100, ATK=100, DEF=100, SPA=100, SPD=100, SPE=100):
        return Stats(HP, ATK, DEF, SPA, SPD, SPE)
    
    def genMove(self, name='Testmove', type='normal', category=MoveCategory.physical, power=100, pp=10, accuracy=100):
        return Move(name, 'For unittests.', type, category, power, pp, accuracy)
    
    def genPkmn(self, name='Testpokemon', type1='normal', type2=None,
                   stats=None,
                   moves=None,
                   gender=Gender.male,
                   ability="Testability"):
        return Pokemon(0, name, type1, type2,
                       stats if stats != None else self.genStats(),
                       moves if moves != None else [self.genMove()],
                       gender, ability)
        
    def getDamage(self, power, ATK, DEF, mult=1):
        dmg = ((210/250) * (ATK/DEF) * power + 2) * mult
        return (dmg*0.85, dmg)
        
    def genEnv(self, weather='none'):
        return Environment(weather)
        
    def assertNotEffective(self, result):
        self.assertEqual(result.eff, Eff.NOT)
        
    def assertWeakEffective(self, result):
        self.assertEqual(result.eff, Eff.WEAK)
        
    def assertNormalEffective(self, result):
        self.assertEqual(result.eff, Eff.NORMAL)
        
    def assertSuperEffective(self, result):
        self.assertEqual(result.eff, Eff.SUPER)
    
    def test_stats1(self):
        p = self.genPkmn(stats=self.genStats(HP=100, ATK=90, DEF=80, SPA=70, SPD=60, SPE=50))
        self.assertEqual(p.HP, 100)
        self.assertEqual(p.ATK.get(), 90)
        self.assertEqual(p.DEF.get(), 80)
        self.assertEqual(p.SPA.get(), 70)
        self.assertEqual(p.SPD.get(), 60)
        self.assertEqual(p.SPE.get(), 50)
        
    def test_stats2(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100))
        p.ATK.stageAdd(1)
        p.DEF.stageAdd(2)
        p.SPA.stageAdd(3)
        p.SPD.stageAdd(4)
        p.SPE.stageAdd(5)
        self.assertEqual(p.ATK.get(), 150)
        self.assertEqual(p.DEF.get(), 200)
        self.assertEqual(p.SPA.get(), 250)
        self.assertEqual(p.SPD.get(), 300)
        self.assertEqual(p.SPE.get(), 350)
        p.ATK.stageAdd(5)
        self.assertEqual(p.ATK.get(), 400)

    def test_ability_Adaptability(self):
        pass
    def test_ability_Aftermath(self):
        pass
    def test_ability_Air Lock(self):
        pass
    def test_ability_Anger Point(self):
        pass
    def test_ability_Anticipation(self):
        pass
    def test_ability_Arena Trap(self):
        pass
    def test_ability_Bad Dreams(self):
        pass
    def test_ability_Battle Armor(self):
        pass
    def test_ability_Blaze(self):
        pass
    def test_ability_Cacophony(self):
        pass
    def test_ability_Chlorophyll(self):
        pass
    def test_ability_Clear Body(self):
        pass
    def test_ability_Cloud Nine(self):
        pass
    def test_ability_Color Change(self):
        pass
    def test_ability_Compound Eyes(self):
        pass
    def test_ability_Cute Charm(self):
        pass
    def test_ability_Damp(self):
        pass
    def test_ability_Download(self):
        pass
    def test_ability_Drizzle(self):
        pass
    def test_ability_Drought(self):
        pass
    def test_ability_Dry Skin(self):
        pass
    def test_ability_Early Bird(self):
        pass
    def test_ability_Effect Spore(self):
        pass
    def test_ability_Filter(self):
        pass
    def test_ability_Flame Body(self):
        pass
    def test_ability_Flash Fire(self):
        pass
    def test_ability_Flower Gift(self):
        pass
    def test_ability_Forecast(self):
        pass
    def test_ability_Forewarn(self):
        pass
    def test_ability_Frisk(self):
        pass
    def test_ability_Gluttony(self):
        pass
    def test_ability_Guts(self):
        pass
    def test_ability_Heatproof(self):
        pass
    def test_ability_Honey Gather(self):
        pass
    def test_ability_Huge Power(self):
        pass
    def test_ability_Hustle(self):
        pass
    def test_ability_Hydration(self):
        pass
    def test_ability_Hyper Cutter(self):
        pass
    def test_ability_Ice Body(self):
        pass
    def test_ability_Illuminate(self):
        pass
    def test_ability_Immunity(self):
        pass
    def test_ability_Inner Focus(self):
        pass
    def test_ability_Insomnia(self):
        pass
    def test_ability_Intimidate(self):
        pass
    def test_ability_Iron Fist(self):
        pass
    def test_ability_Keen Eye(self):
        pass
    def test_ability_Klutz(self):
        pass
    def test_ability_Leaf Guard(self):
        pass
    def test_ability_Levitate(self):
        pass
    def test_ability_Lightning Rod(self):
        pass
    def test_ability_Limber(self):
        pass
    def test_ability_Liquid Ooze(self):
        pass
    def test_ability_Magic Guard(self):
        pass
    def test_ability_Magma Armor(self):
        pass
    def test_ability_Magnet Pull(self):
        pass
    def test_ability_Marvel Scale(self):
        pass
    def test_ability_Minus(self):
        pass
    def test_ability_Mold Breaker(self):
        pass
    def test_ability_Motor Drive(self):
        pass
    def test_ability_Multitype(self):
        pass
    def test_ability_Natural Cure(self):
        pass
    def test_ability_No Guard(self):
        pass
    def test_ability_Normalize(self):
        pass
    def test_ability_Oblivious(self):
        pass
    def test_ability_Overgrow(self):
        pass
    def test_ability_Own Tempo(self):
        pass
    def test_ability_Pickup(self):
        pass
    def test_ability_Plus(self):
        pass
    def test_ability_Poison Heal(self):
        pass
    def test_ability_Poison Point(self):
        pass
    def test_ability_Pressure(self):
        pass
    def test_ability_Pure Power(self):
        pass
    def test_ability_Quick Feet(self):
        pass
    def test_ability_Rain Dish(self):
        pass
    def test_ability_Reckless(self):
        pass
    def test_ability_Rivalry(self):
        pass
    def test_ability_Rock Head(self):
        pass
    def test_ability_Rough Skin(self):
        pass
    def test_ability_Run Away(self):
        pass
    def test_ability_Sand Stream(self):
        pass
    def test_ability_Sand Veil(self):
        pass
    def test_ability_Scrappy(self):
        pass
    def test_ability_Serene Grace(self):
        pass
    def test_ability_Shadow Tag(self):
        pass
    def test_ability_Shed Skin(self):
        pass
    def test_ability_Shell Armor(self):
        pass
    def test_ability_Shield Dust(self):
        pass
    def test_ability_Simple(self):
        pass
    def test_ability_Skill Link(self):
        pass
    def test_ability_Slow Start(self):
        pass
    def test_ability_Sniper(self):
        pass
    def test_ability_Snow Cloak(self):
        pass
    def test_ability_Snow Warning(self):
        pass
    def test_ability_Solar Power(self):
        pass
    def test_ability_Solid Rock(self):
        pass
    def test_ability_Soundproof(self):
        pass
    def test_ability_Speed Boost(self):
        pass
    def test_ability_Stall(self):
        pass
    def test_ability_Static(self):
        pass
    def test_ability_Steadfast(self):
        pass
    def test_ability_Stench(self):
        pass
    def test_ability_Sticky Hold(self):
        pass
    def test_ability_Storm Drain(self):
        pass
    def test_ability_Sturdy(self):
        pass
    def test_ability_Suction Cups(self):
        pass
    def test_ability_Super Luck(self):
        pass
    def test_ability_Swarm(self):
        pass
    def test_ability_Swift Swim(self):
        pass
    def test_ability_Synchronize(self):
        pass
    def test_ability_Tangled Feet(self):
        pass
    def test_ability_Technician(self):
        pass
    def test_ability_Thick Fat(self):
        pass
    def test_ability_Tinted Lens(self):
        pass
    def test_ability_Torrent(self):
        pass
    def test_ability_Trace(self):
        pass
    def test_ability_Truant(self):
        pass
    def test_ability_Unaware(self):
        pass
    def test_ability_Unburden(self):
        pass
    def test_ability_Vital Spirit(self):
        pass
    def test_ability_Volt Absorb(self):
        pass
    def test_ability_Water Absorb(self):
        pass
    def test_ability_Water Veil(self):
        pass
    def test_ability_White Smoke(self):
        pass
    def test_ability_Wonder Guard(self):
        pass

if __name__ == '__main__':
    unittest.main()
    
