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


class TppVisuAbilityTests(unittest.TestCase):
    
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

    def test_ability_adaptability(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="adaptability")
        pass
    def test_ability_aftermath(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="aftermath")
        pass
    def test_ability_air_lock(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="air lock")
        pass
    def test_ability_anger_point(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="anger point")
        pass
    def test_ability_anticipation(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="anticipation")
        pass
    def test_ability_arena_trap(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="arena trap")
        pass
    def test_ability_bad_dreams(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="bad dreams")
        pass
    def test_ability_battle_armor(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="battle armor")
        pass
    def test_ability_blaze(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="blaze")
        pass
    def test_ability_cacophony(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="cacophony")
        pass
    def test_ability_chlorophyll(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="chlorophyll")
        pass
    def test_ability_clear_body(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="clear body")
        pass
    def test_ability_cloud_nine(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="cloud nine")
        pass
    def test_ability_color_change(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="color change")
        pass
    def test_ability_compound_eyes(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="compound eyes")
        pass
    def test_ability_cute_charm(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="cute charm")
        pass
    def test_ability_damp(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="damp")
        pass
    def test_ability_download(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="download")
        pass
    def test_ability_drizzle(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="drizzle")
        pass
    def test_ability_drought(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="drought")
        pass
    def test_ability_dry_skin(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="dry skin")
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        watermove = self.genMove(type="water",power=70)
        firemove = self.genMove(type="fire",power=70)
        # self.assertEqual(calcMove(watermove, attackingmon, p, self.genEnv()).damage, (0,0)) #How do you want to implement healing the opponent, damage-wise?
        self.assertEqual(calcMove(firemove, attackingmon, p, self.genEnv()).damage, self.getDamage(70,100,100,1.25))
    def test_ability_early_bird(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="early bird")
        pass
    def test_ability_effect_spore(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="effect spore")
        pass
    def test_ability_filter(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="filter")
        pass
    def test_ability_flame_body(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="flame body")
        pass
    def test_ability_flash_fire(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="flash fire")
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        firemove = self.genMove(type="fire",power=70)
        self.assertEqual(calcMove(firemove, attackingmon, p, self.genEnv()).damage, (0,0))
        #after this, fire attacks are 1.5x, but others aren't
        self.assertEqual(calcMove(firemove, p, attackingmon, self.genEnv()).damage, self.getDamage(70,100,100,1.5))
        self.assertEqual(calcMove(self.genMove(power=70), p, attackingmon, self.genEnv()).damage, self.getDamage(70,100,100))
    def test_ability_flower_gift(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="flower gift")
        pass
    def test_ability_forecast(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="forecast")
        pass
    def test_ability_forewarn(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="forewarn")
        pass
    def test_ability_frisk(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="frisk")
        pass
    def test_ability_gluttony(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="gluttony")
        pass
    def test_ability_guts(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="guts")
        pass
    def test_ability_heatproof(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="heatproof")
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        firemove = self.genMove(type="fire",power=70)
        self.assertEqual(calcMove(firemove, attackingmon, p, self.genEnv()).damage, self.getDamage(70,100,100,0.5))
    def test_ability_honey_gather(self):
        pass #useless
    def test_ability_huge_power(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="huge power")
        pass
    def test_ability_hustle(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="hustle")
        pass
    def test_ability_hydration(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="hydration")
        pass
    def test_ability_hyper_cutter(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="hyper cutter")
        pass
    def test_ability_ice_body(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="ice body")
        pass
    def test_ability_illuminate(self):
        pass #useless
    def test_ability_immunity(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="immunity")
        pass
    def test_ability_inner_focus(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="inner focus")
        pass
    def test_ability_insomnia(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="insomnia")
        pass
    def test_ability_intimidate(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="intimidate")
        pass
    def test_ability_iron_fist(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="iron fist")
        pass
    def test_ability_keen_eye(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="keen eye")
        pass
    def test_ability_klutz(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="klutz")
        pass
    def test_ability_leaf_guard(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="leaf guard")
        pass
    def test_ability_levitate(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="levitate")
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        groundmove = self.genMove(type="ground",power=70)
        self.assertEqual(calcMove(groundmove, attackingmon, p, self.genEnv()).damage, self.getDamage(70,100,100,0.0))
        #But can still be hit through Mold Breaker!
        moldbreakimon = self.genPkmn(stats=self.genStats(ATK=100),ability="mold breaker")
        self.assertEqual(calcMove(groundmove, moldbreakimon, p, self.genEnv()).damage, self.getDamage(70,100,100))
    def test_ability_lightning_rod(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="lightning rod")
        pass
    def test_ability_limber(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="limber")
        pass
    def test_ability_liquid_ooze(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="liquid ooze")
        pass
    def test_ability_magic_guard(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="magic guard")
        pass
    def test_ability_magma_armor(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="magma armor")
        pass
    def test_ability_magnet_pull(self):
        pass #this only affects trainer switches; which we don't have in PBR.
    def test_ability_marvel_scale(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="marvel scale")
        pass
    def test_ability_mold_breaker(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="mold breaker")
        pass
    def test_ability_motor_drive(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="motor drive")
        pass
    def test_ability_multitype(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="multitype")
        pass
    def test_ability_natural_cure(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="natural cure")
        pass
    def test_ability_no_guard(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="no guard")
        pass
    def test_ability_normalize(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="normalize")
        pass
    def test_ability_oblivious(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="oblivious")
        pass
    def test_ability_overgrow(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="overgrow")
        pass
    def test_ability_own_tempo(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="own tempo")
        pass
    def test_ability_poison_heal(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="poison heal")
        pass
    def test_ability_poison_point(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="poison point")
        pass
    def test_ability_pressure(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="pressure")
        pass
    def test_ability_pure_power(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="pure power")
        pass
    def test_ability_quick_feet(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="quick feet")
        pass
    def test_ability_rain_dish(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="rain dish")
        pass
    def test_ability_reckless(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="reckless")
        pass
    def test_ability_rivalry(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="rivalry")
        pass
    def test_ability_rock_head(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="rock head")
        pass
    def test_ability_rough_skin(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="rough skin")
        pass
    def test_ability_sand_stream(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="sand stream")
        pass
    def test_ability_sand_veil(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="sand veil")
        pass
    def test_ability_scrappy(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="scrappy")
        pass
    def test_ability_serene_grace(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="serene grace")
        pass
    def test_ability_shadow_tag(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="shadow tag")
        pass
    def test_ability_shed_skin(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="shed skin")
        pass
    def test_ability_shell_armor(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="shell armor")
        pass
    def test_ability_shield_dust(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="shield dust")
        pass
    def test_ability_simple(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="simple")
        pass
    def test_ability_skill_link(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="skill link")
        pass
    def test_ability_slow_start(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="slow start")
        pass
    def test_ability_sniper(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="sniper")
        pass
    def test_ability_snow_cloak(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="snow cloak")
        pass
    def test_ability_snow_warning(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="snow warning")
        pass
    def test_ability_solar_power(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="solar power")
        pass
    def test_ability_solid_rock(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="solid rock")
        pass
    def test_ability_soundproof(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="soundproof")
        pass
    def test_ability_speed_boost(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="speed boost")
        pass
    def test_ability_stall(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="stall")
        pass
    def test_ability_static(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="static")
        pass
    def test_ability_steadfast(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="steadfast")
        pass
    def test_ability_stench(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="stench")
        pass
    def test_ability_sticky_hold(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="sticky hold")
        pass
    def test_ability_sturdy(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="sturdy")
        pass
    def test_ability_suction_cups(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="suction cups")
        pass
    def test_ability_super_luck(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="super luck")
        pass
    def test_ability_swarm(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="swarm")
        pass
    def test_ability_swift_swim(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="swift swim")
        pass
    def test_ability_synchronize(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="synchronize")
        pass
    def test_ability_tangled_feet(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="tangled feet")
        pass
    def test_ability_technician(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="technician")
        pass
    def test_ability_thick_fat(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="thick fat")
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        firemove = self.genMove(type="fire",power=70)
        self.assertEqual(calcMove(firemove, attackingmon, p, self.genEnv()).damage, self.getDamage(70,100,100,0.5))
        icemove = self.genMove(type="ice",power=70)
        self.assertEqual(calcMove(icemove, attackingmon, p, self.genEnv()).damage, self.getDamage(70,100,100,0.5))
    def test_ability_tinted_lens(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="tinted lens")
        pass
    def test_ability_torrent(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="torrent")
        pass
    def test_ability_trace(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="trace")
        pass
    def test_ability_truant(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="truant")
        pass
    def test_ability_unaware(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="unaware")
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        move = self.genMove(type="normal",power=70)
        self.assertEqual(calcMove(move, p, attackingmon,  self.genEnv()).damage, self.getDamage(70,100,100))
        #Who cares about stat changes? Not freaking Bidoof, that's who.
        attackingmon.ATK.stageAdd(1)
        attackingmon.DEF.stageAdd(2)
        attackingmon.SPA.stageAdd(3)
        attackingmon.SPD.stageAdd(4)
        attackingmon.SPE.stageAdd(5)
        self.assertEqual(calcMove(move, p, attackingmon,  self.genEnv()).damage, self.getDamage(70,100,100))

        #Accuracy? Who needs accuracy when you're FREAKING BIDOOF?
        m = self.genMove(name='Blizzard', accuracy=70)
        self.assertEqual(calcMove(m, attackingmon, p, self.genEnv()).accuracy, 100)

        pass
    def test_ability_unburden(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="unburden")
        pass
    def test_ability_vital_spirit(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="vital spirit")
        pass
    def test_ability_volt_absorb(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="volt absorb")
        pass
    def test_ability_water_absorb(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="water absorb")
        pass
    def test_ability_water_veil(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="water veil")
        pass
    def test_ability_white_smoke(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="white smoke")
        pass
    def test_ability_wonder_guard(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100, SPA=100, SPD=100, SPE=100),ability="wonder guard",type="grass")
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        nveffective = self.genMove(type="water",power=70)
        supereffective = self.genMove(type="fire",power=70)
        normaleffective = self.genMove(type="normal",power=70)
        self.assertEqual(calcMove(nveffective, attackingmon, p, self.genEnv()).damage, self.getDamage(70,100,100,0))
        self.assertEqual(calcMove(supereffective, attackingmon, p, self.genEnv()).damage, self.getDamage(70,100,100))
        self.assertEqual(calcMove(normaleffective, attackingmon, p, self.genEnv()).damage, self.getDamage(70,100,100,0))
        #todo: assert that non-effective move that poisons still does damage

if __name__ == '__main__':
    unittest.main()
    