'''
Created on 05.07.14

@author: Hlixed
'''

import unittest

from tppVisu.move import MoveCategory, Move
from tppVisu.pokemon import Pokemon, Gender
from tppVisu.util import Stats, Environment
from tppVisu.calculator import Eff, calcSetup


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

    def test_ability_adaptability(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="adaptability")
        pass
    def test_ability_aftermath(self):
        pass #Not visualizeable; The damage isn't added onto any move
    def test_ability_air_lock(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="air lock")
        pass
    def test_ability_anger_point(self):
        pass #Not visualizeable; who knows when crits happen?
    def test_ability_anticipation(self):
        pass #Not visualizeable
    def test_ability_arena_trap(self):
        pass #Not visualizeable; Baton Pass etc. still work
    def test_ability_bad_dreams(self):
        pass #Not visualizeable
    def test_ability_battle_armor(self):
        pass #Not visualizeable; Who knows when crits happen?
    def test_ability_blaze(self):
        pass #Not visualizeable
    def test_ability_cacophony(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="cacophony")
        pass
    def test_ability_chlorophyll(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="chlorophyll")
        pass
    def test_ability_clear_body(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="clear body")
        pass
    def test_ability_cloud_nine(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="cloud nine")
        pass
    def test_ability_color_change(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="color change")
        pass
    def test_ability_compound_eyes(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="compound eyes")
        pass
    def test_ability_cute_charm(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="cute charm")
        pass
    def test_ability_damp(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="damp")
        pass
    def test_ability_download(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="download")
        pass
    def test_ability_drizzle(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="drizzle")
        pass
    def test_ability_drought(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="drought")
        pass
    def test_ability_dry_skin(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="dry skin")
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        watermove = self.genMove(type="water",power=70)
        firemove = self.genMove(type="fire",power=70)
        attackingmon.moves = [watermove,firemove]
        
        attackdamage = calcSetup(attackingmon, p, self.genEnv()).blues
        self.assertNotEffective(attackdamage[0]) #water moves heal
        self.assertEqual(attackdamage[1].damage, self.getDamage(70,100,100,1.25)) #fire moves do more
    def test_ability_early_bird(self):
        pass #Not visualizeable
    def test_ability_effect_spore(self):
        pass #Not visualizeable
    def test_ability_filter(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="filter")
        pass
    def test_ability_flame_body(self):
        pass #Non-visualizable
    def test_ability_flash_fire(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="flash fire")
        attackingmon = self.genPkmn(stats=self.genStats(),moves=[self.genMove(type="fire",power=70)])
        self.assertNotEffective(calcSetup(attackingmon,p,self.genEnv()).blues[0])
        #after this, fire attacks are 1.5x, but this isn't visualizable
    def test_ability_flower_gift(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="flower gift")
        pass
    def test_ability_forecast(self):
        pass #Not visualizeable; it's freaking castform.
    def test_ability_forewarn(self):
        pass #Not visualizeable, not to mention kinda useless in PBR
    def test_ability_frisk(self):
        pass #Not visualizeable
    def test_ability_gluttony(self):
        pass #Not visualizeable; This is PBR; nobody's holding berries
    def test_ability_guts(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="guts")
        pass
    def test_ability_heatproof(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="heatproof")
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        p.moves = [self.genMove(type="fire",power=70)]
        d1,d2,env = calcSetup(p,attackingmon,self.genEnv())
        self.assertEqual(d1[0].damage, self.getDamage(70,100,100,0.5))
    def test_ability_honey_gather(self):
        pass #useless
    def test_ability_huge_power(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="huge power")
        pass
    def test_ability_hustle(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="hustle")
        pass
    def test_ability_hydration(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="hydration")
        pass
    def test_ability_hyper_cutter(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="hyper cutter")
        pass
    def test_ability_ice_body(self):
        pass #Not visualizeable
    def test_ability_illuminate(self):
        pass #useless
    def test_ability_immunity(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="immunity")
        pass
    def test_ability_inner_focus(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="inner focus")
        pass
    def test_ability_insomnia(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="insomnia")
        pass
    def test_ability_intimidate(self):
        pass #Not visualizeable
    def test_ability_iron_fist(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="iron fist",type1="fire") # prevent STAB
        m = self.genMove(name="Thunder Punch",power=70)
        m2 = self.genMove(name="Not Thunder Punch",power=70)
        self.assertEqual(m.isPunchingMove(),True)
        self.assertEqual(m2.isPunchingMove(),False)
        p.moves = [m, m2] # don't just append. array is not empty by default, has a 'Testmove'
        d1,d2,env = calcSetup(p, self.genPkmn(), self.genEnv())
        self.assertEqual(d1[0].damage, self.getDamage(70*1.2,100,100)) # increases base power
        self.assertEqual(d1[1].damage, self.getDamage(70,100,100))
    def test_ability_keen_eye(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="keen eye")
        m = self.genMove(name="Sand Attack")
        d1,d2,env = calcSetup(p,self.genPkmn(moves=[m]),self.genEnv())
        self.assertEqual(d2[0].eff, Eff.NOT)
        pass
    def test_ability_klutz(self):
        pass #Not visualizeable; nobody cares about items
    def test_ability_leaf_guard(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="leaf guard")
        pass
    def test_ability_levitate(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="levitate")
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        groundmove = self.genMove(type="ground",power=70)
        attackingmon.moves = [groundmove]
        pdamage,attackdamage,env = calcSetup(p, attackingmon, self.genEnv())
        self.assertEqual(attackdamage[0].eff, Eff.NOT)
        #But can still be hit through Mold Breaker!
        moldbreakimon = self.genPkmn(stats=self.genStats(ATK=100),ability="mold breaker")
        moldbreakimon.moves = [groundmove]
        pdamage,attackdamage,env = calcSetup(p, moldbreakimon, self.genEnv())
        self.assertEqual(attackdamage[0].eff, Eff.NORMAL)
    def test_ability_lightning_rod(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="lightning rod")
        pass
    def test_ability_limber(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="limber")
        pass
    def test_ability_liquid_ooze(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="liquid ooze")
        pass
    def test_ability_magic_guard(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="magic guard")
        pass
    def test_ability_magma_armor(self):
        pass #Not visualizeable; it won't actually disable any moves since there's no Toxic for frz
    def test_ability_magnet_pull(self):
        pass #this only affects trainer switches; which we don't have in PBR.
    def test_ability_marvel_scale(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="marvel scale")
        pass
    def test_ability_mold_breaker(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="mold breaker")
        pass
    def test_ability_motor_drive(self):
        pass #Non visualizeable; no way of knowing what attack is used
    def test_ability_multitype(self):
        pass #Not visualizeable; we all know how Arceus works
    def test_ability_natural_cure(self):
        pass #Not visualizeable; switching is overrated anyways
    def test_ability_no_guard(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="no guard")
        p2 = self.genPkmn(stats=self.genStats(ATK=100,DEF=100))
        m = self.genMove(accuracy=10)
        p.moves.append(m)
        p2.moves.append(m)
        pdamage,attackdamage,env = calcSetup(p, p2, self.genEnv())
        self.assertEqual(pdamage[0].accuracy, None)
        self.assertEqual(attackdamage[0].accuracy, None)
    def test_ability_normalize(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="normalize")
        pass
    def test_ability_oblivious(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="oblivious")
        pass
    def test_ability_overgrow(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="overgrow")
        pass
    def test_ability_own_tempo(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="own tempo")
        pass
    def test_ability_poison_heal(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="poison heal")
        pass
    def test_ability_poison_point(self):
        pass # Not visualizeable
    def test_ability_pressure(self):
        pass #Pretty much useless.
    def test_ability_pure_power(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="pure power")
        pass
    def test_ability_quick_feet(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="quick feet")
        pass
    def test_ability_rain_dish(self):
        pass #Not visualizeable; HP over time isn't implemented
    def test_ability_reckless(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="reckless")
        pass
    def test_ability_rivalry(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="rivalry",gender=Gender.male)
        if not p.abilityVisuable:
            return # rivalry doesn't work as a design choice
        p2 = self.genPkmn(gender=Gender.male)
        m = self.genMove(power=70)
        p.moves = [m]
        pdamage,attackdamage,env = calcSetup(p, p2, self.genEnv())
        self.assertEqual(pdamage[0].damage, self.getDamage(70,100,100,1.25))
        
        p2.gender = Gender.female
        pdamage,attackdamage,env = calcSetup(p, p2, self.genEnv())
        self.assertEqual(pdamage[0].damage, self.getDamage(70,100,100,0.75))
        
        p2.gender = Gender.none
        pdamage,attackdamage,env = calcSetup(p, p2, self.genEnv())
        self.assertEqual(pdamage[0].damage, self.getDamage(70,100,100,1))
    def test_ability_rock_head(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="rock head")
        pass
    def test_ability_rough_skin(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="rough skin")
        pass
    def test_ability_sand_stream(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="sand stream")
        pass
    def test_ability_sand_veil(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="sand veil")
        pass
    def test_ability_scrappy(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="scrappy")
        pass
    def test_ability_serene_grace(self):
        pass #Not visualizeable; we don't test for secondary effects
    def test_ability_shadow_tag(self):
        pass #Not visualizeable; Baton pass, etc. still work
    def test_ability_shed_skin(self):
        pass #Not visualizeable; It's random!
    def test_ability_shell_armor(self):
        pass #Not visualizeable; we don't know about crits
    def test_ability_shield_dust(self):
        pass #Not visualizeable; secondary effects are random
    def test_ability_simple(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="simple")
        pass
    def test_ability_skill_link(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="skill link")
        pass
    def test_ability_slow_start(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="slow start")
        pass
    def test_ability_sniper(self):
        pass #Not visualizeable; Crits? What are those?
    def test_ability_snow_cloak(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="snow cloak")
        pass
    def test_ability_snow_warning(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="snow warning")
        pass
    def test_ability_solar_power(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="solar power")
        pass
    def test_ability_solid_rock(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="solid rock")
        pass
    def test_ability_soundproof(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="soundproof")
        p2 = self.genPkmn(stats=self.genStats(ATK=100, DEF=100))
        soundm = self.genMove(name="Uproar",power=70)
        notsound = self.genMove(name="Tackle",power=70)
        self.assertEqual(soundm.isSoundMove(), True)
        self.assertEqual(notsound.isSoundMove(), False)
        
        p2.moves = [notsound,soundm]
        
        pdamage,attackdamage,env = calcSetup(p, p2, self.genEnv())
        self.assertNormalEffective(attackdamage[0])
        self.assertNotEffective(attackdamage[1])
    def test_ability_speed_boost(self):
        pass  #Non-visualizable
    def test_ability_stall(self):
        pass #Non-visualizeable
    def test_ability_storm_drain(self):
        pass #Non-visualizeable
    def test_ability_static(self):
        pass #Not visualizable
    def test_ability_steadfast(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="steadfast")
        pass
    def test_ability_stench(self):
        pass #Not visualizeable
    def test_ability_sticky_hold(self):
        pass #Not visualizeable
    def test_ability_sturdy(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="sturdy")
        pass
    def test_ability_suction_cups(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="suction cups")
        pass
    def test_ability_super_luck(self):
        pass #Not visualizeable
    def test_ability_swarm(self):
        pass #Not visualizeable
    def test_ability_swift_swim(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="swift swim")
        pass
    def test_ability_synchronize(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="synchronize")
        pass
    def test_ability_tangled_feet(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="tangled feet")
        pass
    def test_ability_technician(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="technician")
        pass
    def test_ability_thick_fat(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="thick fat")
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        

        firemove = self.genMove(type="fire",power=70)
        icemove = self.genMove(type="ice",power=70)
        
        attackingmon.moves = [firemove,icemove]
        
        pdamage,attackdamage,env = calcSetup(p, attackingmon, self.genEnv())
        self.assertEqual(attackdamage[0].damage,self.getDamage(70,100,100,0.5))
        self.assertEqual(attackdamage[1].damage, self.getDamage(70,100,100,0.5))
    def test_ability_tinted_lens(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="tinted lens")
        pass
    def test_ability_torrent(self):
        pass #Not visualizeable
    def test_ability_trace(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="trace")
        pass
    def test_ability_truant(self):
        pass #Not visualizeable; how do you visualize not attacking every other turn?
    def test_ability_unaware(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="unaware",type1="dragon") # prevent STAB
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        move = self.genMove(type="normal",power=70)
        m2 = self.genMove(name='Blizzard', accuracy=70)
        
        p.moves = [move,m2]
        attackingmon.moves = [move]
        pdamage,attackdamage,env = calcSetup(p, attackingmon, self.genEnv())
        self.assertEqual(pdamage[0].damage,self.getDamage(70,100,100))
        #Who cares about stat changes? Not freaking Bidoof, that's who.
        attackingmon.ATK.stageAdd(1)
        attackingmon.DEF.stageAdd(2)
        attackingmon.SPA.stageAdd(3)
        attackingmon.SPD.stageAdd(4)
        attackingmon.SPE.stageAdd(5)
        attackingmon.EVA.stageAdd(6)
        pdamage,attackdamage,env = calcSetup(p, attackingmon, self.genEnv())
        self.assertEqual(pdamage[0].damage, self.getDamage(70,100,100))

        #Accuracy? Who needs accuracy when you're FREAKING BIDOOF?
        self.assertEqual(pdamage[1].accuracy, 70) # base accuracy is kept
        
    def test_ability_unburden(self):
        pass #Not visualizeable; in PBR Drifloon and Drifblim don't hold items
    def test_ability_vital_spirit(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="vital spirit")
        pass
    def test_ability_volt_absorb(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="volt absorb")
        p2 = self.genPkmn(stats=self.genStats(ATK=100, DEF=100))
        m = self.genMove(type="electric",power=70)
        p2.moves = [m]
        
        self.assertNotEffective(calcSetup( p2, p, self.genEnv()).blues[0])
    def test_ability_water_absorb(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="water absorb")
        p2 = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),moves=[self.genMove(type="water",power=70)])
        
        self.assertNotEffective(calcSetup( p2, p, self.genEnv()).blues[0])
    def test_ability_water_veil(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="water veil")
        p2 = self.genPkmn(stats=self.genStats(ATK=100, DEF=100))
        m = self.genMove(name="Will-o-Wisp",category=MoveCategory.nonDamaging)
        p2.moves = [m]
        
        self.assertNotEffective(calcSetup(p2, p, self.genEnv()).blues[0])
    def test_ability_white_smoke(self):
        #p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="white smoke")
        pass
    def test_ability_wonder_guard(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="wonder guard",type1="grass")
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        nveffective = self.genMove(type="water",power=70)
        supereffective = self.genMove(type="fire",power=70)
        normaleffective = self.genMove(type="normal",power=70)
        attackingmon.moves=[nveffective,supereffective,normaleffective]
        
        attackdamages = calcSetup(attackingmon,p,self.genEnv()).blues
        self.assertEqual(attackdamages[0].damage, self.getDamage(70,100,100,0)) #nveffective won't hit
        self.assertEqual(attackdamages[1].damage, self.getDamage(70,100,100,2)) #super will hit
        self.assertEqual(attackdamages[2].damage, self.getDamage(70,100,100,0)) #normal effectiveness won't hit
        #todo: assert that non-effective move that poisons still does damage

if __name__ == '__main__':
    unittest.main()
    
