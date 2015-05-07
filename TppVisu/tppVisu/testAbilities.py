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
        pass
    def test_ability_aftermath(self):
        pass
    def test_ability_air_lock(self):
        pass
    def test_ability_anger_point(self):
        pass
    def test_ability_anticipation(self):
        pass
    def test_ability_arena_trap(self):
        pass
    def test_ability_bad_dreams(self):
        pass
    def test_ability_battle_armor(self):
        pass
    def test_ability_blaze(self):
        pass
    def test_ability_cacophony(self):
        pass
    def test_ability_chlorophyll(self):
        pass
    def test_ability_clear_body(self):
        pass
    def test_ability_cloud_nine(self):
        pass
    def test_ability_color_change(self):
        pass
    def test_ability_compound_eyes(self):
        pass
    def test_ability_cute_charm(self):
        pass
    def test_ability_damp(self):
        pass
    def test_ability_download(self):
        pass
    def test_ability_drizzle(self):
        pass
    def test_ability_drought(self):
        pass
    def test_ability_dry_skin(self):
        pass
    def test_ability_early_bird(self):
        pass
    def test_ability_effect_spore(self):
        pass
    def test_ability_filter(self):
        pass
    def test_ability_flame_body(self):
        pass
    def test_ability_flash_fire(self):
        pass
    def test_ability_flower_gift(self):
        pass
    def test_ability_forecast(self):
        pass
    def test_ability_forewarn(self):
        pass
    def test_ability_frisk(self):
        pass
    def test_ability_gluttony(self):
        pass
    def test_ability_guts(self):
        pass
    def test_ability_heatproof(self):
        pass
    def test_ability_honey_gather(self):
        pass
    def test_ability_huge_power(self):
        pass
    def test_ability_hustle(self):
        pass
    def test_ability_hydration(self):
        pass
    def test_ability_hyper_cutter(self):
        pass
    def test_ability_ice_body(self):
        pass
    def test_ability_illuminate(self):
        pass
    def test_ability_immunity(self):
        pass
    def test_ability_inner_focus(self):
        pass
    def test_ability_insomnia(self):
        pass
    def test_ability_intimidate(self):
        pass
    def test_ability_iron_fist(self):
        pass
    def test_ability_keen_eye(self):
        pass
    def test_ability_klutz(self):
        pass
    def test_ability_leaf_guard(self):
        pass
    def test_ability_levitate(self):
        pass
    def test_ability_lightning_rod(self):
        pass
    def test_ability_limber(self):
        pass
    def test_ability_liquid_ooze(self):
        pass
    def test_ability_magic_guard(self):
        pass
    def test_ability_magma_armor(self):
        pass
    def test_ability_magnet_pull(self):
        pass
    def test_ability_marvel_scale(self):
        pass
    def test_ability_minus(self):
        pass
    def test_ability_mold_breaker(self):
        pass
    def test_ability_motor_drive(self):
        pass
    def test_ability_multitype(self):
        pass
    def test_ability_natural_cure(self):
        pass
    def test_ability_no_guard(self):
        pass
    def test_ability_normalize(self):
        pass
    def test_ability_oblivious(self):
        pass
    def test_ability_overgrow(self):
        pass
    def test_ability_own_tempo(self):
        pass
    def test_ability_pickup(self):
        pass
    def test_ability_plus(self):
        pass
    def test_ability_poison_heal(self):
        pass
    def test_ability_poison_point(self):
        pass
    def test_ability_pressure(self):
        pass
    def test_ability_pure_power(self):
        pass
    def test_ability_quick_feet(self):
        pass
    def test_ability_rain_dish(self):
        pass
    def test_ability_reckless(self):
        pass
    def test_ability_rivalry(self):
        pass
    def test_ability_rock_head(self):
        pass
    def test_ability_rough_skin(self):
        pass
    def test_ability_run_away(self):
        pass
    def test_ability_sand_stream(self):
        pass
    def test_ability_sand_veil(self):
        pass
    def test_ability_scrappy(self):
        pass
    def test_ability_serene_grace(self):
        pass
    def test_ability_shadow_tag(self):
        pass
    def test_ability_shed_skin(self):
        pass
    def test_ability_shell_armor(self):
        pass
    def test_ability_shield_dust(self):
        pass
    def test_ability_simple(self):
        pass
    def test_ability_skill_link(self):
        pass
    def test_ability_slow_start(self):
        pass
    def test_ability_sniper(self):
        pass
    def test_ability_snow_cloak(self):
        pass
    def test_ability_snow_warning(self):
        pass
    def test_ability_solar_power(self):
        pass
    def test_ability_solid_rock(self):
        pass
    def test_ability_soundproof(self):
        pass
    def test_ability_speed_boost(self):
        pass
    def test_ability_stall(self):
        pass
    def test_ability_static(self):
        pass
    def test_ability_steadfast(self):
        pass
    def test_ability_stench(self):
        pass
    def test_ability_sticky_hold(self):
        pass
    def test_ability_storm_drain(self):
        pass
    def test_ability_sturdy(self):
        pass
    def test_ability_suction_cups(self):
        pass
    def test_ability_super_luck(self):
        pass
    def test_ability_swarm(self):
        pass
    def test_ability_swift_swim(self):
        pass
    def test_ability_synchronize(self):
        pass
    def test_ability_tangled_feet(self):
        pass
    def test_ability_technician(self):
        pass
    def test_ability_thick_fat(self):
        pass
    def test_ability_tinted_lens(self):
        pass
    def test_ability_torrent(self):
        pass
    def test_ability_trace(self):
        pass
    def test_ability_truant(self):
        pass
    def test_ability_unaware(self):
        pass
    def test_ability_unburden(self):
        pass
    def test_ability_vital_spirit(self):
        pass
    def test_ability_volt_absorb(self):
        pass
    def test_ability_water_absorb(self):
        pass
    def test_ability_water_veil(self):
        pass
    def test_ability_white_smoke(self):
        pass
    def test_ability_wonder_guard(self):
        pass

if __name__ == '__main__':
    unittest.main()
    
