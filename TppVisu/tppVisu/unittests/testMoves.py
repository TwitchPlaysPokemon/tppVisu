'''
Created on 09.05.2015

@author: Felk
'''

import unittest

from tppVisu.calculator import Eff, calcSetup, Kind
from tppVisu.move import MoveCategory, Move
from tppVisu.pokemon import Pokemon, Gender
from tppVisu.util import Stats, Environment


class TppVisuMoveTests(unittest.TestCase):
    
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
        return (int(dmg*0.85), int(dmg))
     
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
    
    def test_move_arm_thrust(self):
        p1 = self.genPkmn(stats=self.genStats(ATK=332), type1="dragon", moves=[self.genMove(name='Arm Thrust', power=15)]) # no stab
        p2 = self.genPkmn(stats=self.genStats(DEF=223))
        dmg1 = self.getDamage(15, 332, 223)[0] * 2
        dmg2 = self.getDamage(15, 332, 223)[1] * 5
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, (dmg1, dmg2))
        
        
    def test_move_attract(self):
        p1 = self.genPkmn(gender=Gender.male, moves=[self.genMove(name='Attract')])
        p2 = self.genPkmn(gender=Gender.male)
        self.assertNotEffective(calcSetup(p1, p2, self.genEnv()).blues[0])
        p2.gender = Gender.female
        self.assertNormalEffective(calcSetup(p1, p2, self.genEnv()).blues[0])
        p1.gender = Gender.none
        self.assertNotEffective(calcSetup(p1, p2, self.genEnv()).blues[0])
        
    def test_move_blizzard(self):
        self.assertEqual(calcSetup(self.genPkmn(moves=[self.genMove(name='Blizzard', accuracy=70)]), self.genPkmn(), self.genEnv()).blues[0].accuracy, 70)
        self.assertEqual(calcSetup(self.genPkmn(moves=[self.genMove(name='Blizzard', accuracy=70)]), self.genPkmn(), self.genEnv(weather='hail')).blues[0].accuracy, 100)
        
    def test_move_dragon_rage(self):
        m = self.genMove(name='Dragon Rage')
        self.assertEqual(calcSetup(self.genPkmn(moves=[m]), self.genPkmn(), self.genEnv()).blues[0].damage, (40, 40))

    def test_move_explosion(self):
        m = self.genMove(name='Explosion', power=250, type='normal')
        p1 = self.genPkmn(stats=self.genStats(ATK=123), type1='normal', moves=[m]) # stab
        p2 = self.genPkmn(stats=self.genStats(DEF=321), type1='normal')
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(500, 123, 321, 1.5))

    def test_move_facade(self):
        m = self.genMove(name='Facade', power=70, type='normal')
        p1 = self.genPkmn(stats=self.genStats(ATK=121), type1='fire', moves=[m]) # no stab
        p2 = self.genPkmn(stats=self.genStats(DEF=212), type1='normal')
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(70, 121, 212))
        p1.status = 'par'
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(140, 121, 212))

    def test_move_ohko(self):
        self.assertEqual(calcSetup(self.genPkmn(moves=[self.genMove(name='Fissure')]), self.genPkmn(), self.genEnv()).blues[0].kind, Kind.ohko)
        self.assertEqual(calcSetup(self.genPkmn(moves=[self.genMove(name='Guillotine')]), self.genPkmn(), self.genEnv()).blues[0].kind, Kind.ohko)
        self.assertEqual(calcSetup(self.genPkmn(moves=[self.genMove(name='Sheer Cold')]), self.genPkmn(), self.genEnv()).blues[0].kind, Kind.ohko)
        self.assertEqual(calcSetup(self.genPkmn(moves=[self.genMove(name='Horn Drill')]), self.genPkmn(), self.genEnv()).blues[0].kind, Kind.ohko)
        self.assertNotEqual(calcSetup(self.genPkmn(moves=[self.genMove(name='Seismic Toss')]), self.genPkmn(), self.genEnv()).blues[0].kind, Kind.ohko)

    def test_move_frustration(self):
        m = self.genMove(name='Frustration', power=42) # power should be ignored
        p1 = self.genPkmn(stats=self.genStats(ATK=79), type1='water', moves=[m])
        p2 = self.genPkmn(stats=self.genStats(DEF=163))
        p1.happiness = 68
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage((255 - 68) / 2.5, 79, 163))

    def test_move_return(self):
        m = self.genMove(name='Return', power=14) # power should be ignored
        p1 = self.genPkmn(stats=self.genStats(ATK=133), type1='water', moves=[m])
        p2 = self.genPkmn(stats=self.genStats(DEF=201))
        p1.happiness = 82
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(82 / 2.5, 133, 201))

    def test_move_grass_knot(self):
        m = self.genMove(name='Grass Knot')
        p1 = self.genPkmn(stats=self.genStats(ATK=99), type1='water', moves=[m])
        p2 = self.genPkmn(stats=self.genStats(DEF=166))
        p2.weight = 59
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(80, 99, 166))
        p2.weight = 0.6
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(20, 99, 166))
        p2.weight = 187
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(100, 99, 166))
        p2.weight = 347
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(120, 99, 166))
        p2.weight = 0.012
        self.assertNotEffective(calcSetup(p1, p2, self.genEnv()).blues[0])

    def test_move_gyro_ball(self):
        m = self.genMove(name='Gyro Ball')
        p1 = self.genPkmn(stats=self.genStats(ATK=99, SPE=204), type1='ground', moves=[m])
        p2 = self.genPkmn(stats=self.genStats(DEF=166, SPE=172))
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(25 * (172 / 204), 99, 166))
        p1.SPE.stageAdd(2)
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(25 * (172 / 408), 99, 166))
        p2.SPE.stageAdd(3)
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(25 * (430 / 408), 99, 166))

    def test_move_low_kick(self):
        m = self.genMove(name='Low Kick')
        p1 = self.genPkmn(stats=self.genStats(ATK=99), type1='water', moves=[m])
        p2 = self.genPkmn(stats=self.genStats(DEF=166))
        p2.weight = 59
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(80, 99, 166))
        p2.weight = 0.6
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(20, 99, 166))
        p2.weight = 187
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(100, 99, 166))
        p2.weight = 347
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(120, 99, 166))
        p2.weight = 0.012
        self.assertNotEffective(calcSetup(p1, p2, self.genEnv()).blues[0])

    def test_move_magnitude(self):
        m = self.genMove(name='Magnitude')
        p1 = self.genPkmn(type1='rock', stats=self.genStats(ATK=222), moves=[m])
        p2 = self.genPkmn(stats=self.genStats(DEF=333))
        damage = (self.getDamage(10, 222, 333)[0], self.getDamage(150, 222, 333)[1])
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, damage)

    def test_move_night_shade(self):
        m = self.genMove(name='Night Shade')
        p1 = self.genPkmn(moves=[m])
        self.assertEqual(calcSetup(p1, self.genPkmn(), self.genEnv()).blues[0].damage, (100, 100))
        p1.level=57
        self.assertEqual(calcSetup(p1, self.genPkmn(), self.genEnv()).blues[0].damage, (57, 57))
    
    def test_move_seismic_toss(self):
        m = self.genMove(name='Seismic Toss')
        p1 = self.genPkmn(moves=[m])
        p2 = self.genPkmn()
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, (100, 100))
        p2.level=39
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, (39, 39))

    def test_move_psywave(self):
        self.assertEqual(calcSetup(self.genPkmn(moves=[self.genMove(name='Psywave')]), self.genPkmn(), self.genEnv()).blues[0].damage, (50, 150))

    def test_move_punishment(self):
        m = self.genMove(name='Punishment')
        p1 = self.genPkmn(stats=self.genStats(ATK=85), type1='dark', moves=[m])
        p2 = self.genPkmn(stats=self.genStats(DEF=165, ATK=123, SPD=245, SPE=201))
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(60, 85, 165))
        p1.DEF.stageAdd(1)
        p2.ATK.stageAdd(1)
        p2.SPD.stageAdd(1)
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(100, 85, 165))
        p2.SPD.stageAdd(1)
        p2.SPE.stageAdd(-1)
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(120, 85, 165))
        p2.SPD.stageAdd(-2)
        p2.SPE.stageAdd(2)
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(100, 85, 165))

    def test_move_smelling_salts(self):
        m = self.genMove(name='Smelling Salts', power=60)
        p1 = self.genPkmn(stats=self.genStats(ATK=154), type1='dark', moves=[m])
        p2 = self.genPkmn(stats=self.genStats(DEF=235))
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(60, 154, 235))
        p2.status='par'
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, self.getDamage(120, 154, 235))

    def test_move_sonic_boom(self):
        self.assertEqual(calcSetup(self.genPkmn(moves=[self.genMove(name='Sonic Boom')]), self.genPkmn(), self.genEnv()).blues[0].damage, (20, 20))

    def test_move_thunder(self):
        m = self.genMove(name='Thunder', accuracy=70)
        p = self.genPkmn(moves=[m])
        self.assertEqual(calcSetup(p, self.genPkmn(), self.genEnv()).blues[0].accuracy, 70)
        self.assertEqual(calcSetup(p, self.genPkmn(), self.genEnv(weather='rain')).blues[0].accuracy, 100)
        self.assertEqual(calcSetup(p, self.genPkmn(), self.genEnv(weather='sun')).blues[0].accuracy, 50)
        self.assertEqual(calcSetup(p, self.genPkmn(), self.genEnv(weather='sandstorm')).blues[0].accuracy, 70)
        
    def test_move_triple_kick(self):
        # 3 hits with 10, 20, 30 base power
        m = self.genMove(name="Triple Kick", power=10, type='fighting')
        p1 = self.genPkmn(stats=self.genStats(ATK=190), moves=[m])
        p2 = self.genPkmn(stats=self.genStats(DEF=173), type1='normal')
        dmg1 = self.getDamage(10, 190, 173, 2)[0]
        dmg2 = self.getDamage(10, 190, 173, 2)[1] + self.getDamage(20, 190, 173, 2)[1] + self.getDamage(30, 190, 173, 2)[1]
        # TODO rounding error occurs
        self.assertEqual(calcSetup(p1, p2, self.genEnv()).blues[0].damage, (dmg1, dmg2))
        
    def test_move_weather_ball(self):
        m = self.genMove(name='Weather Ball', power=50)
        p1 = self.genPkmn(stats=self.genStats(ATK=70), moves=[m])
        p2 = self.genPkmn(stats=self.genStats(DEF=80))
        e = self.genEnv()
        self.assertEqual(calcSetup(p1, p2, e).blues[0].damage, self.getDamage(50, 70, 80, 1.5))
        e.weather = 'sun'
        self.assertEqual(calcSetup(p1, p2, e).blues[0].damage, self.getDamage(100, 70, 80, 1))
        #self.assertEqual(calcSetup(p1, p2, e).move.type, 'fire')
        e.weather = 'rain'
        self.assertEqual(calcSetup(p1, p2, e).blues[0].damage, self.getDamage(100, 70, 80, 1))
        #self.assertEqual(calcSetup(p1, p2, e).move.type, 'water')
        e.weather = 'hail'
        self.assertEqual(calcSetup(p1, p2, e).blues[0].damage, self.getDamage(100, 70, 80, 1))
        #self.assertEqual(calcSetup(p1, p2, e).move.type, 'ice')
        e.weather = 'sandstorm'
        self.assertEqual(calcSetup(p1, p2, e).blues[0].damage, self.getDamage(100, 70, 80, 1))
        #self.assertEqual(calcSetup(p1, p2, e).move.type, 'rock')
        e.weather = 'fog'
        self.assertEqual(calcSetup(p1, p2, e).blues[0].damage, self.getDamage(100, 70, 80, 1.5))
        #self.assertEqual(calcSetup(p1, p2, e).move.type, 'normal')
    

if __name__ == '__main__':
    unittest.main()
    
