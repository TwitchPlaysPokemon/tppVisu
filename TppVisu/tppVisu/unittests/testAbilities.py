'''
Created on 05.07.14

@author: Hlixed
'''
from __future__ import division, print_function

import unittest

from tppVisu.calculator import calcSetup
from tppVisu.move import MoveCategory
from tppVisu.pokemon import Gender
from tppVisu.unittests.visuUnittest import VisuTestCase
from tppVisu.util import Eff


class TppVisuAbilityTests(VisuTestCase):

    def test_ability_adaptability(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="adaptability", type1="fire")
        p.moves = [self.genMove(power=70, type="fire"), self.genMove(power=70, type="normal")]
        pdamage = calcSetup(p, self.genPkmn(), self.genEnv()).blues
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 100, 100, 2))
        self.assertEqual(pdamage[1].damage, self.getDamage(70, 100, 100))
    def test_ability_aftermath(self):
        pass  # Not visualizeable; The damage isn't added onto any move
    def test_ability_air_lock(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="air lock")
        p2 = self.genPkmn()
        p2.moves = [self.genMove(name="Rain Dance")]
        pdamage, attackdamage, env = calcSetup(p, p2, self.genEnv(weather="Rain"))
        
        # NOTE I read that Air Lock does only negate the effects, but these attacks would still work, right? (same as cloud none)
        self.assertNotEffective(attackdamage[0])
        self.assertEqual(env.weather, "none")  # maybe not technically correct, but close enough

    def test_ability_anger_point(self):
        pass  # Not visualizeable; who knows when crits happen?
    def test_ability_anticipation(self):
        pass  # Not visualizeable
    def test_ability_arena_trap(self):
        pass  # Not visualizeable; Baton Pass etc. still work
    def test_ability_bad_dreams(self):
        pass  # Not visualizeable
    def test_ability_battle_armor(self):
        pass  # Not visualizeable; Who knows when crits happen?
    def test_ability_blaze(self):
        pass  # Not visualizeable
    def test_ability_cacophony(self):
        pass  # It's an unused ability!
    def test_ability_chlorophyll(self):
        pass  # Not visualizeable; it affects speed
    def test_ability_clear_body(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="clear body")
        p2 = self.genPkmn(stats=self.genStats(ATK=100))
        p2.moves = [self.genMove(name="Swagger"), self.genMove(name="Growl")]
        d2 = calcSetup(p2, p, self.genEnv()).blues
        self.assertNormalEffective(d2[0])
        self.assertNotEffective(d2[1])
        
        p2.ability = "Mold Breaker"
        d2 = calcSetup(p2, p, self.genEnv()).blues
        self.assertNormalEffective(d2[0])
        self.assertNormalEffective(d2[1])
    def test_ability_cloud_nine(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="cloud nine")
        p2 = self.genPkmn()
        p2.moves = [self.genMove(name="Rain Dance")]
        pdamage, attackdamage, env = calcSetup(p, p2, self.genEnv(weather="Rain"))
        
        # NOTE I read that Cloud Nine does only negate the effects, but these attacks would still work, right? (same as Air Lock)
        self.assertNotEffective(attackdamage[0])
        self.assertEqual(env.weather, "none")  # maybe not technically correct, but close enough
    def test_ability_color_change(self):
        pass  # Not visualizeable
    def test_ability_compound_eyes(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="compound eyes")
        p2 = self.genPkmn(stats=self.genStats(ATK=100, DEF=100))
        m = self.genMove(accuracy=10)
        p.moves = [self.genMove(accuracy=10), self.genMove(accuracy=80)]
        pdamage = calcSetup(p, p2, self.genEnv()).blues
        self.assertEqual(pdamage[0].accuracy, 10 * 1.3) 
        self.assertEqual(pdamage[1].accuracy, 100)  # Upper cap of 100
    def test_ability_cute_charm(self):
        pass  # Not visualizeable
    def test_ability_damp(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="damp")
        p2 = self.genPkmn(stats=self.genStats(ATK=100))
        p2.moves = [self.genMove(name="Selfdestruct"), self.genMove(name="Tackle")]
        d2 = calcSetup(p2, p, self.genEnv()).blues
        self.assertNotEffective(d2[0])
        self.assertNormalEffective(d2[1])
        # It also prevents aftermath, but we can't test for that
    def test_ability_download(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="download", type1="dragon")
        p.moves = [self.genMove(power=70, category=MoveCategory.physical), self.genMove(power=70, category=MoveCategory.special)]
 
        # SPD lower: SPA raised to *1.5
        pdamage = calcSetup(p, self.genPkmn(stats=self.genStats(DEF=100, SPD=80)), self.genEnv()).blues
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 100, 100))
        self.assertEqual(pdamage[1].damage, self.getDamage(70, 100 * 1.5, 80))
        
        # DEF lower: ATK raised to *1.5
        pdamage = calcSetup(p, self.genPkmn(stats=self.genStats(DEF=80, SPD=100)), self.genEnv()).blues
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 100 * 1.5, 80))
        self.assertEqual(pdamage[1].damage, self.getDamage(70, 100, 100))
        
        # DEF = SPD: SPA raised to *1.5
        pdamage = calcSetup(p, self.genPkmn(stats=self.genStats(DEF=100, SPD=100)), self.genEnv()).blues
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 100, 100))
        self.assertEqual(pdamage[1].damage, self.getDamage(70, 100 * 1.5, 100))
    def test_ability_drizzle(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="drizzle")
        env = calcSetup(p, self.genPkmn(), self.genEnv()).env
        
        self.assertEqual(env.weather, "rain")
    def test_ability_drought(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="drought")
        env = calcSetup(p, self.genPkmn(), self.genEnv()).env
        
        self.assertEqual(env.weather, "sun")
    def test_ability_dry_skin(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="dry skin")
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        watermove = self.genMove(type="water", power=70)
        firemove = self.genMove(type="fire", power=70)
        attackingmon.moves = [watermove, firemove]
        
        attackdamage = calcSetup(attackingmon, p, self.genEnv()).blues
        self.assertNotEffective(attackdamage[0])  # water moves heal
        self.assertEqual(attackdamage[1].damage, self.getDamage(70, 100, 100, 1.25))  # fire moves do more
    def test_ability_early_bird(self):
        pass  # Not visualizeable
    def test_ability_effect_spore(self):
        pass  # Not visualizeable
    def test_ability_filter(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="filter", type1="grass", type2="bug")

        attackingmon = self.genPkmn(stats=self.genStats(ATK=100), type1='dragon')  # prevent STAB
        
        nveffective = self.genMove(type="water", power=70)
        fourxeffective = self.genMove(type="fire", power=70)
        supereffective = self.genMove(type="poison", power=70)
        normaleffective = self.genMove(type="normal", power=70)
        attackingmon.moves = [nveffective, supereffective, normaleffective, fourxeffective]
        
        attackdamages = calcSetup(attackingmon, p, self.genEnv()).blues
        self.assertEqual(attackdamages[0].damage, self.getDamage(70, 100, 100, 0.5))  # not very: unaffected
        self.assertEqual(attackdamages[1].damage, self.getDamage(70, 100, 100, 1.5))  # super: 1.5x instead of 2
        self.assertEqual(attackdamages[2].damage, self.getDamage(70, 100, 100, 1))  # normal: 1x
        self.assertEqual(attackdamages[3].damage, self.getDamage(70, 100, 100, 3))  # 4x effective: 3x instead of 4
    def test_ability_flame_body(self):
        pass  # Non-visualizable
    def test_ability_flash_fire(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="flash fire")
        attackingmon = self.genPkmn(stats=self.genStats(), moves=[self.genMove(type="fire", power=70)])
        self.assertNotEffective(calcSetup(attackingmon, p, self.genEnv()).blues[0])
        # after this, fire attacks are 1.5x, but this isn't visualizable
    def test_ability_flower_gift(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="flower gift", moves=[self.genMove(power=70, category=MoveCategory.physical)], type1="dragon")
        p2 = self.genPkmn(moves=[self.genMove(power=70, category=MoveCategory.special)], type1="dragon")
        pdamage, attackdamage, env = calcSetup(p, p2, self.genEnv())
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 100, 100))
        self.assertEqual(attackdamage[0].damage, self.getDamage(70, 100, 100))
        
        pdamage, attackdamage, env = calcSetup(p, p2, self.genEnv(weather="sun"))
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 100 * 1.5, 100))  # Attack * 1.5
        self.assertEqual(attackdamage[0].damage, self.getDamage(70, 100, 100 * 1.5))  # Spdef * 1.5
    def test_ability_forecast(self):
        pass  # Not visualizeable; it's freaking castform.
    def test_ability_forewarn(self):
        pass  # Not visualizeable, not to mention kinda useless in PBR
    def test_ability_frisk(self):
        pass  # Not visualizeable
    def test_ability_gluttony(self):
        pass  # Not visualizeable; This is PBR; nobody's holding berries
    def test_ability_guts(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="guts", moves=[self.genMove(power=70)], type1="dragon")
        self.assertEqual(p.hasStatusCondition(), False)
        pdamage = calcSetup(p, self.genPkmn(), self.genEnv()).blues
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 100, 100))
        
        p.status = "brn"
        self.assertEqual(p.hasStatusCondition(), True)
        pdamage = calcSetup(p, self.genPkmn(), self.genEnv()).blues
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 100 * 1.5, 100))  # No attack drop from burn
        
    def test_ability_heatproof(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="heatproof")
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        p.moves = [self.genMove(type="fire", power=70)]
        d1, d2, env = calcSetup(p, attackingmon, self.genEnv())
        self.assertEqual(d1[0].damage, self.getDamage(70, 100, 100, 0.5))
    def test_ability_honey_gather(self):
        pass  # useless
    def test_ability_huge_power(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="huge power", type1="fire")
        p.moves = [self.genMove(power=70, category=MoveCategory.physical), self.genMove(power=70, category=MoveCategory.special)]
        pdamage = calcSetup(p, self.genPkmn(), self.genEnv()).blues
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 100 * 2, 100))
        self.assertEqual(pdamage[1].damage, self.getDamage(70, 100, 100))
    def test_ability_hustle(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="hustle", type1="dragon")
        p.moves = [self.genMove(power=70, category=MoveCategory.physical, accuracy=100), self.genMove(power=70, category=MoveCategory.special, accuracy=100)]
        pdamage = calcSetup(p, self.genPkmn(), self.genEnv()).blues
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 100 * 1.5, 100))
        self.assertEqual(pdamage[0].accuracy, 100 * 0.8)
        self.assertEqual(pdamage[1].damage, self.getDamage(70, 100, 100))  # spatk isnt boosted
        self.assertEqual(pdamage[1].accuracy, 100)
    def test_ability_hydration(self):
        # In rain, status conditions go away
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="hydration")
        p2 = self.genPkmn(moves=[self.genMove(name="Thunder Wave")])
        attackdamage = calcSetup(p, p2, self.genEnv()).reds
        self.assertNormalEffective(attackdamage[0])
        
        attackdamage = calcSetup(p, p2, self.genEnv(weather="rain")).reds
        self.assertNotEffective(attackdamage[0])
    def test_ability_hyper_cutter(self): 
        # Attack cannot be reduced
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="hyper cutter")
        p2 = self.genPkmn(moves=[self.genMove(name="Growl"), self.genMove(name="Swagger")])
        attackdamage = calcSetup(p, p2, self.genEnv()).reds
        self.assertNotEffective(attackdamage[0])
        self.assertNormalEffective(attackdamage[1])
    def test_ability_ice_body(self):
        pass  # Not visualizeable
    def test_ability_illuminate(self):
        pass  # useless
    def test_ability_immunity(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="immunity")
        p2 = self.genPkmn(moves=[self.genMove(name="Toxic")])
        attackdamage = calcSetup(p, p2, self.genEnv()).reds
        self.assertNotEffective(attackdamage[0])
    def test_ability_inner_focus(self):
        pass  # Not visualizeable; flinching is random!
    def test_ability_insomnia(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="insomnia")
        p2 = self.genPkmn(moves=[self.genMove(name="Spore")])
        p.moves = [self.genMove(name="Rest")]
        
        pdamage, attackdamage, env = calcSetup(p, p2, self.genEnv())
        self.assertNotEffective(pdamage[0])  # Rest won't work
        self.assertNotEffective(attackdamage[0])  # Spore won't put to sleep
    def test_ability_intimidate(self):
        pass  # Not visualizeable
    def test_ability_iron_fist(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="iron fist", type1="fire")  # prevent STAB
        m = self.genMove(name="Thunder Punch", power=70)
        m2 = self.genMove(name="Not Thunder Punch", power=70)
        self.assertEqual(m.isPunchingMove(), True)
        self.assertEqual(m2.isPunchingMove(), False)
        p.moves = [m, m2]  # don't just append. array is not empty by default, has a 'Testmove'
        d1 = calcSetup(p, self.genPkmn(), self.genEnv()).blues
        self.assertEqual(d1[0].damage, self.getDamage(70 * 1.2, 100, 100))  # increases base power
        self.assertEqual(d1[1].damage, self.getDamage(70, 100, 100))
    def test_ability_keen_eye(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="keen eye")
        m = self.genMove(name="Sand Attack")
        d1, d2, env = calcSetup(p, self.genPkmn(moves=[m]), self.genEnv())
        self.assertEqual(d2[0].eff, Eff.NOT)
    def test_ability_klutz(self):
        pass  # Not visualizeable; nobody cares about items
    def test_ability_leaf_guard(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="leaf guard")
        p2 = self.genPkmn(moves=[self.genMove(name="Thunder Wave"), self.genMove(name="Yawn"), self.genMove(name="Toxic")])
        attackdamage = calcSetup(p, p2, self.genEnv()).reds
        for atk in attackdamage:
            self.assertNormalEffective(atk)
        
        attackdamage = calcSetup(p, p2, self.genEnv(weather="sun")).reds
        for atk in attackdamage:
            self.assertNotEffective(atk)
    def test_ability_levitate(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="levitate")
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        groundmove = self.genMove(type="ground", power=70)
        attackingmon.moves = [groundmove]
        pdamage, attackdamage, env = calcSetup(p, attackingmon, self.genEnv())
        self.assertEqual(attackdamage[0].eff, Eff.NOT)
        # But can still be hit through Mold Breaker!
        moldbreakimon = self.genPkmn(stats=self.genStats(ATK=100), ability="mold breaker")
        moldbreakimon.moves = [groundmove]
        pdamage, attackdamage, env = calcSetup(p, moldbreakimon, self.genEnv())
        self.assertEqual(attackdamage[0].eff, Eff.NORMAL)
    def test_ability_lightning_rod(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="lightning rod")
        p2 = self.genPkmn(moves=[self.genMove(type="electric", accuracy=10), self.genMove(type='fire', accuracy=10)])
        attackdamage = calcSetup(p, p2, self.genEnv()).reds
        self.assertEqual(attackdamage[0].accuracy, None)
        self.assertEqual(attackdamage[1].accuracy, 10)
    def test_ability_limber(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="limber")
        p2 = self.genPkmn(moves=[self.genMove(name="Thunder Wave")])
        attackdamage = calcSetup(p, p2, self.genEnv()).reds
        self.assertNotEffective(attackdamage[0])
    def test_ability_liquid_ooze(self):
        pass  # Not visualizeable; draining moves still do damage to the defender
    def test_ability_magic_guard(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="magic guard")
        p2 = self.genPkmn(moves=[self.genMove(name="Toxic"), self.genMove(name="Curse"), self.genMove(name="Leech Seed")], type1="ghost")
        attackdamage = calcSetup(p, p2, self.genEnv()).reds
        for attack in attackdamage:
            self.assertNotEffective(attack)
    def test_ability_magma_armor(self):
        pass  # Not visualizeable; it won't actually disable any moves since there's no Toxic for frz
    def test_ability_magnet_pull(self):
        pass  # this only affects trainer switches; which we don't have in PBR.
    def test_ability_marvel_scale(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="marvel scale")
        p2 = self.genPkmn(moves=[self.genMove(name="Tackle", power=70)], type1="dragon")
        attackdamage = calcSetup(p, p2, self.genEnv()).reds
        self.assertEqual(attackdamage[0].damage, self.getDamage(70, 100, 100))
        
        p.status = "psn"
        self.assertEqual(p.hasStatusCondition(), True)
        
        attackdamage = calcSetup(p, p2, self.genEnv()).reds
        self.assertEqual(attackdamage[0].damage, self.getDamage(70, 100, 100 * 1.5))
    def test_ability_mold_breaker(self):
        pass  # It's worked into everyone else's tests
    def test_ability_motor_drive(self):
        pass  # Non visualizeable; no way of knowing what attack is used
    def test_ability_multitype(self):
        pass  # Not visualizeable; we all know how Arceus works
    def test_ability_natural_cure(self):
        pass  # Not visualizeable; switching is overrated anyways
    def test_ability_no_guard(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="no guard")
        p2 = self.genPkmn(stats=self.genStats(ATK=100, DEF=100))
        m = self.genMove(accuracy=10)
        p.moves = [m]
        p2.moves = [m]
        pdamage, attackdamage, env = calcSetup(p, p2, self.genEnv())
        self.assertEqual(pdamage[0].accuracy, None)
        self.assertEqual(attackdamage[0].accuracy, None)
    def test_ability_normalize(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="normalize", moves=[self.genMove(power=70, type="fire")])
        p2 = self.genPkmn(type1="ghost")
        
        pdamage = calcSetup(p, p2, self.genEnv()).blues
        # Fire should be able to hit ghost-types; with normalize it won't
        self.assertNotEffective(pdamage[0])
    
        # Test for STAB; the move remains a fire-type move
        p3 = self.genPkmn(type1="fire")
        pdamage = calcSetup(p, p3, self.genEnv()).blues
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 100, 100, 1.5))
    def test_ability_oblivious(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="oblivious", gender=Gender.male)
        p2 = self.genPkmn(moves=[self.genMove(name="attract")], gender=Gender.female)
        attackdamage = calcSetup(p, p2, self.genEnv()).reds
        self.assertNotEffective(attackdamage[0])
        # This ability also makes Cute Charm useless, but that's non-visualizeable
    def test_ability_overgrow(self):
        pass  # Non-visualizeable
    def test_ability_own_tempo(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="own tempo")
        p2 = self.genPkmn(moves=[self.genMove(name="Confuse Ray")])
        attackdamage = calcSetup(p, p2, self.genEnv()).reds
        self.assertNotEffective(attackdamage[0])
    def test_ability_poison_heal(self):
        pass  # Non-visualizeable
    def test_ability_poison_point(self):
        pass  # Not visualizeable
    def test_ability_pressure(self):
        pass  # Not visualizeable, not to mention pretty much useless.
    def test_ability_pure_power(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="pure power", moves=[self.genMove(power=70)], type1="fire")
        pdamage = calcSetup(p, self.genPkmn(), self.genEnv()).blues
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 200, 100))
    def test_ability_quick_feet(self):
        pass  # Not visualizeable; boosts speed by 50% when inflicted with status; prz speed drop negated
    def test_ability_rain_dish(self):
        pass  # Not visualizeable; HP over time isn't implemented
    def test_ability_reckless(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="reckless", type1="fire")
        p.moves = [self.genMove(name="Flare Blitz", power=70), self.genMove(name="Tackle", power=70)]
        self.assertEqual(p.moves[0].isRecoilMove(), True)
        pdamage = calcSetup(p, self.genPkmn(), self.genEnv()).blues
        self.assertEqual(pdamage[0].damage, self.getDamage(70 * 1.2, 100, 100))
        self.assertEqual(pdamage[1].damage, self.getDamage(70, 100, 100))
    def test_ability_rivalry(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="rivalry", gender=Gender.male)
        if not p.abilityVisuable:
            return  # rivalry doesn't work as a design choice
        p2 = self.genPkmn(gender=Gender.male)
        m = self.genMove(power=70)
        p.moves = [m]
        pdamage, attackdamage, env = calcSetup(p, p2, self.genEnv())
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 100, 100, 1.25))
        
        p2.gender = Gender.female
        pdamage, attackdamage, env = calcSetup(p, p2, self.genEnv())
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 100, 100, 0.75))
        
        p2.gender = Gender.none
        pdamage, attackdamage, env = calcSetup(p, p2, self.genEnv())
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 100, 100, 1))
    def test_ability_rock_head(self):
        pass  # Non-visualizeable; protects against recoil
    def test_ability_rough_skin(self):
        pass  # Non-visualizeable; causes damage on physical moves
    def test_ability_sand_stream(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="sand stream")
        env = calcSetup(p, self.genPkmn(), self.genEnv()).env
        
        self.assertEqual(env.weather, "sandstorm")
    def test_ability_sand_veil(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="sand veil")
        p2 = self.genPkmn(moves=[self.genMove(accuracy=100), self.genMove(accuracy=50)])
        attackdamage = calcSetup(p, p2, self.genEnv()).reds
        self.assertEqual(attackdamage[0].accuracy, 100)
        self.assertEqual(attackdamage[1].accuracy, 50)
        
        attackdamage = calcSetup(p, p2, self.genEnv(weather="sandstorm")).reds
        self.assertEqual(attackdamage[0].accuracy, int(100 * 1 / (1.2)))
        self.assertEqual(attackdamage[1].accuracy, int(50 * 1 / (1.2)))
    def test_ability_scrappy(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="scrappy", type1="ghost")
        p2 = self.genPkmn(type1="ghost")
        m = self.genMove(power=70, type="normal")
        p2.moves = [m]
        p.moves = [m]
        
        pdamage, attackdamage, env = calcSetup(p, p2, self.genEnv())
        
        self.assertNormalEffective(pdamage[0])  # p can hit ghost-type p2 with Scrappy
        self.assertNotEffective(attackdamage[0])  # p2 can't hit a ghost without Scrappy
    def test_ability_serene_grace(self):
        pass  # Not visualizeable; we don't test for secondary effects
    def test_ability_shadow_tag(self):
        pass  # Not visualizeable; Baton pass, etc. still work
    def test_ability_shed_skin(self):
        pass  # Not visualizeable; It's random!
    def test_ability_shell_armor(self):
        pass  # Not visualizeable; we don't know about crits
    def test_ability_shield_dust(self):
        pass  # Not visualizeable; secondary effects are random
    def test_ability_simple(self):
        pass  # Not visualizeable; doesn't actually disable any moves, just increases their stat gains/losses
    def test_ability_skill_link(self):
        # This ability makes multi-hitting moves always hit 5 times.
        # This test assumes that normally, the least damage is calculated with 2 hits, and most is with 5.
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="skill link", type1="fire")
        m = self.genMove(name="Fury Swipes", power=18)
        p.moves = [m]
        d1 = calcSetup(p, self.genPkmn(), self.genEnv()).blues
        # dmg is rounded after every step => sum single values
        dmg = self.getDamage(18, 100, 100)
        dmg = tuple(D * 5 for D in dmg)
        self.assertEqual(d1[0].damage, dmg)
    def test_ability_slow_start(self):
        pass  # Not visualizeable
    def test_ability_sniper(self):
        pass  # Not visualizeable; Crits? What are those?
    def test_ability_snow_cloak(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="snow cloak")
        p2 = self.genPkmn(moves=[self.genMove(accuracy=100), self.genMove(accuracy=50)])
        attackdamage = calcSetup(p, p2, self.genEnv()).reds
        self.assertEqual(attackdamage[0].accuracy, 100)
        self.assertEqual(attackdamage[1].accuracy, 50)
        
        attackdamage = calcSetup(p, p2, self.genEnv(weather="hail")).reds
        self.assertEqual(attackdamage[0].accuracy, int(100 * 1 / (1.2)))
        self.assertEqual(attackdamage[1].accuracy, int(50 * 1 / (1.2)))
    def test_ability_snow_warning(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="snow warning")
        env = calcSetup(p, self.genPkmn(), self.genEnv()).env
        
        self.assertEqual(env.weather, "hail")
    def test_ability_solar_power(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="solar power", moves=[self.genMove(power=70, category=MoveCategory.special)], type1="dragon")
        p2 = self.genPkmn()
        pdamage = calcSetup(p, p2, self.genEnv()).blues
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 100, 100))
        
        pdamage = calcSetup(p, p2, self.genEnv(weather="sun")).blues
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 100 * 1.5, 100))  # SpAttack * 1.5
    def test_ability_solid_rock(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="solid rock", type1="grass", type2="bug")
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100), type1="ghost")  # prevent STAB
        nveffective = self.genMove(type="water", power=70)
        fourxeffective = self.genMove(type="fire", power=70)
        supereffective = self.genMove(type="poison", power=70)
        normaleffective = self.genMove(type="normal", power=70)
        attackingmon.moves = [nveffective, supereffective, normaleffective, fourxeffective]
        
        attackdamages = calcSetup(attackingmon, p, self.genEnv()).blues
        self.assertEqual(attackdamages[0].damage, self.getDamage(70, 100, 100, 0.5))  # not very: unaffected
        self.assertEqual(attackdamages[1].damage, self.getDamage(70, 100, 100, 1.5))  # super: 1.5x instead of 2
        self.assertEqual(attackdamages[2].damage, self.getDamage(70, 100, 100, 1))  # normal: 1x
        self.assertEqual(attackdamages[3].damage, self.getDamage(70, 100, 100, 3))  # 4x effective: 3x instead of 4
    def test_ability_soundproof(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="soundproof")
        p2 = self.genPkmn(stats=self.genStats(ATK=100, DEF=100))
        soundm = self.genMove(name="Uproar", power=70)
        notsound = self.genMove(name="Tackle", power=70)
        self.assertEqual(soundm.isSoundMove(), True)
        self.assertEqual(notsound.isSoundMove(), False)
        
        p2.moves = [notsound, soundm]
        
        pdamage, attackdamage, env = calcSetup(p, p2, self.genEnv())
        self.assertNormalEffective(attackdamage[0])
        self.assertNotEffective(attackdamage[1])
    def test_ability_speed_boost(self):
        pass  # Non-visualizable
    def test_ability_stall(self):
        pass  # Non-visualizeable
    def test_ability_storm_drain(self):
        pass  # Non-visualizeable
    def test_ability_static(self):
        pass  # Not visualizable
    def test_ability_steadfast(self):
        pass  # Not visualizeable; the ability raises speed when flinched
    def test_ability_stench(self):
        pass  # Not visualizeable
    def test_ability_sticky_hold(self):
        pass  # Not visualizeable
    def test_ability_sturdy(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="sturdy")
        p2 = self.genPkmn(moves=[self.genMove(name="Guillotine"), self.genMove(power=99999, name="OVERPOWEREDNONCANONICALMEGALASEROFDOOM")])
        attackdamage = calcSetup(p2, p, self.genEnv()).blues
        self.assertEqual(p2.moves[0].isOHKOMove(), True)
        
        self.assertNotEffective(attackdamage[0])
        
        # Gen 4 sturdy doesn't protect against non-OHKO but over 100% damage moves; that's gen V
        self.assertNormalEffective(attackdamage[1]) 
        
    def test_ability_suction_cups(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="suction cups")
        m = self.genMove(name="Whirlwind")
        m2 = self.genMove(name="Roar")
        d2 = calcSetup(p, self.genPkmn(moves=[m, m2]), self.genEnv()).reds
        self.assertEqual(d2[0].eff, Eff.NOT)
        self.assertEqual(d2[1].eff, Eff.NOT)
    def test_ability_super_luck(self):
        pass  # Not visualizeable
    def test_ability_swarm(self):
        pass  # Not visualizeable
    def test_ability_swift_swim(self):
        # p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100),ability="swift swim")
        pass  # Potentially non-visualizeable; has to do with speed
    def test_ability_synchronize(self):
        pass  # Not visualizeable; although an argument could be made to disable toxic, etc.
    def test_ability_tangled_feet(self):
        pass  # Not visualizeable; raises evasion when confused
    def test_ability_technician(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="technician", type1="dragon")
        p2 = self.genPkmn(stats=self.genStats(ATK=100))
        p.moves = [self.genMove(power=50), self.genMove(power=60), self.genMove(power=70)]
        
        pdamages = calcSetup(p, p2, self.genEnv()).blues
        self.assertEqual(pdamages[0].damage, self.getDamage(50 * 1.5, 100, 100))  # rounding errors? Should not happen, weird
        self.assertEqual(pdamages[1].damage, self.getDamage(60 * 1.5, 100, 100))
        self.assertEqual(pdamages[2].damage, self.getDamage(70, 100, 100))
    def test_ability_thick_fat(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="thick fat")
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        

        firemove = self.genMove(type="fire", power=70)
        icemove = self.genMove(type="ice", power=70)
        
        attackingmon.moves = [firemove, icemove]
        
        pdamage, attackdamage, env = calcSetup(p, attackingmon, self.genEnv())
        self.assertEqual(attackdamage[0].damage, self.getDamage(70, 100, 100, 0.5))
        self.assertEqual(attackdamage[1].damage, self.getDamage(70, 100, 100, 0.5))
    def test_ability_tinted_lens(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="tinted lens", type1="dragon")  # prevent STAB)
        p2 = self.genPkmn(stats=self.genStats(DEF=100), type1="steel", type2="flying")
        
        nveffective = self.genMove(type="steel", power=70)
        fourxneffective = self.genMove(type="bug", power=70)
        normaleffective = self.genMove(type="normal", power=70)
        p.moves = [nveffective, fourxneffective, normaleffective]
        
        pdamages = calcSetup(p, p2, self.genEnv()).blues
        self.assertEqual(pdamages[0].damage, self.getDamage(70, 100, 100, 1))  # not very: 1x instead of .5
        self.assertEqual(pdamages[1].damage, self.getDamage(70, 100, 100, 0.5))  # doubly resisted: 0.5x instead of .25
        self.assertEqual(pdamages[2].damage, self.getDamage(70, 100, 100, 1))  # normal: 1x
    def test_ability_torrent(self):
        pass  # Not visualizeable
    def test_ability_trace(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="trace", type1="normal")
        # Test #1: Wonder Guard
        wondermon = self.genPkmn(ability="wonder guard", moves=[self.genMove(type="normal"), self.genMove(type="fighting")])
        
        attackdamages = calcSetup(p, wondermon, self.genEnv()).reds
        self.assertNotEffective(attackdamages[0])
        self.assertSuperEffective(attackdamages[1])
        
        # Test #2: Vital Spirit should prevent sleep
        vitalmon = self.genPkmn(ability="vital spirit", moves=[self.genMove(name="Spore")])
        attackdamages = calcSetup(p, wondermon, self.genEnv()).reds
        self.assertNotEffective(attackdamages[0])
        
        # Test #3: Technician
        technimon = self.genPkmn(ability="technician")
        p.moves = [self.genMove(power=50), self.genMove(power=60), self.genMove(power=70)]
        
        p.type1 = "fire"  # avoid STAB
        pdamages = calcSetup(p, technimon, self.genEnv()).blues
        self.assertEqual(pdamages[0].damage, self.getDamage(50 * 1.5, 100, 100))
        self.assertEqual(pdamages[1].damage, self.getDamage(60 * 1.5, 100, 100))
        self.assertEqual(pdamages[2].damage, self.getDamage(70, 100, 100))
        
        # Test #4: Tracing Trace doesn't cause an infinite loop of death
        tracimon = self.genPkmn(ability="technician")
        try:
            calcSetup(p, tracimon, self.genEnv()).blues
        except RuntimeError as e:
            # oops
            self.assertIsNone(e)
    def test_ability_truant(self):
        pass  # Not visualizeable; how do you visualize not attacking every other turn?
    def test_ability_unaware(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="unaware", type1="dragon")  # prevent STAB
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        move = self.genMove(type="normal", power=70)
        m2 = self.genMove(name='Blizzard', accuracy=70)
        
        p.moves = [move, m2]
        attackingmon.moves = [move]
        pdamage = calcSetup(p, attackingmon, self.genEnv()).blues
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 100, 100))
        # Who cares about stat changes? Not freaking Bidoof, that's who.
        attackingmon.ATK.stageAdd(1)
        attackingmon.DEF.stageAdd(2)
        attackingmon.SPA.stageAdd(3)
        attackingmon.SPD.stageAdd(4)
        attackingmon.SPE.stageAdd(5)
        attackingmon.EVA.stageAdd(6)
        pdamage = calcSetup(p, attackingmon, self.genEnv()).blues
        self.assertEqual(pdamage[0].damage, self.getDamage(70, 100, 100))

        # Accuracy? Who needs accuracy when you're FREAKING BIDOOF?
        self.assertEqual(pdamage[1].accuracy, 70)  # base accuracy is kept
        
    def test_ability_unburden(self):
        pass  # Not visualizeable; in PBR Drifloon and Drifblim don't hold items
    def test_ability_vital_spirit(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="vital spirit")
        p2 = self.genPkmn(moves=[self.genMove(name="Spore")])
        p.moves = [self.genMove(name="Rest")]
        
        pdamage, attackdamage, env = calcSetup(p, p2, self.genEnv())
        self.assertNotEffective(pdamage[0])  # Rest won't work
        self.assertNotEffective(attackdamage[0])  # Spore won't put to sleep
    def test_ability_volt_absorb(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="volt absorb")
        p2 = self.genPkmn(stats=self.genStats(ATK=100, DEF=100))
        m = self.genMove(type="electric", power=70)
        p2.moves = [m]
        
        self.assertNotEffective(calcSetup(p2, p, self.genEnv()).blues[0])
    def test_ability_water_absorb(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="water absorb")
        p2 = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), moves=[self.genMove(type="water", power=70)])
        
        self.assertNotEffective(calcSetup(p2, p, self.genEnv()).blues[0])
    def test_ability_water_veil(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="water veil")
        p2 = self.genPkmn(stats=self.genStats(ATK=100, DEF=100))
        m = self.genMove(name="Will-o-Wisp", category=MoveCategory.nonDamaging)
        p2.moves = [m]
        
        self.assertNotEffective(calcSetup(p2, p, self.genEnv()).blues[0])
    def test_ability_white_smoke(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="white smoke")
        p2 = self.genPkmn(stats=self.genStats(ATK=100))
        p2.moves = [self.genMove(name="Swagger"), self.genMove(name="Growl")]
        d2 = calcSetup(p2, p, self.genEnv()).blues
        self.assertNormalEffective(d2[0])
        self.assertNotEffective(d2[1])
        
        p2.ability = "Mold Breaker"
        d2 = calcSetup(p2, p, self.genEnv()).blues
        self.assertNormalEffective(d2[0])
        self.assertNormalEffective(d2[1])
    def test_ability_wonder_guard(self):
        p = self.genPkmn(stats=self.genStats(ATK=100, DEF=100), ability="wonder guard", type1="grass")
        attackingmon = self.genPkmn(stats=self.genStats(ATK=100))
        nveffective = self.genMove(type="water", power=70)
        supereffective = self.genMove(type="fire", power=70)
        normaleffective = self.genMove(type="normal", power=70)
        attackingmon.moves = [nveffective, supereffective, normaleffective]
        
        attackdamages = calcSetup(attackingmon, p, self.genEnv()).blues
        self.assertEqual(attackdamages[0].damage, self.getDamage(70, 100, 100, 0))  # nveffective won't hit
        self.assertEqual(attackdamages[1].damage, self.getDamage(70, 100, 100, 2))  # super will hit
        self.assertEqual(attackdamages[2].damage, self.getDamage(70, 100, 100, 0))  # normal effectiveness won't hit
        # todo: assert that non-effective move that poisons still does damage

if __name__ == '__main__':
    unittest.main()
