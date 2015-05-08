'''
Created on 28.04.2015

@author: Felk
'''
from tppVisu.move import MoveCategory
from tppVisu.tables.moveAnomalies import MoveAnomaly
import tppVisu.pokemon

def call(abilityName, pkmn, opp, env):
    funcname = 'a_' + abilityName.lower().replace(' ', '_')
    try:
        globals()[funcname](pkmn, opp, env)
    except KeyError:
        pass

def isVisuable(abilityName):
    funcname = 'a_' + abilityName.lower().replace(' ', '_')
    return funcname in dir()

#####################################################
#         ABILITY   IMPLEMENTATIONS   BELOW         #
#####################################################

# sample method declaration. lowercase, prefixed with a_ and spaces written as _
# takes the user's and opponent's pokemon plus an environment (see util) as params.
def a_sample_ability(pkmn, opp, env):
    pass

def a_adaptability  (pkmn, opp, env):
    pkmn.stab = 2

def a_air_lock      (pkmn, opp, env):
    env.weather = 'none'

def a_chlorophyll   (pkmn, opp, env):
    if env.weather == 'sun':
        pkmn.SPE *= 2
    
def a_cloud_nine    (pkmn, opp, env):
    env.weather = 'none'

def a_compound_eyes (pkmn, opp, env):
    for move in pkmn.moves:
        move.accuracy *= 1.3;
    
def a_damp          (pkmn, opp, env):
    for move in pkmn.moves:
        if move.anomaly == MoveAnomaly.selfdestructing:
            move.disable()
    if not opp.breaksMold():
        for move in opp.moves:
            if move.anomaly == MoveAnomaly.selfdestructing:
                move.disable()

def a_download      (pkmn, opp, env):
    if opp.SPD.get() <= opp.DEF.get():
        pkmn.SPA.stageAdd(1)
    else:
        pkmn.ATK.stageAdd(1)

def a_drizzle       (pkmn, opp, env):
    env.weather = 'rain'

def a_drought       (pkmn, opp, env):
    env.weather = 'sun'

def a_dry_skin      (pkmn, opp, env):
    opp.typeMults.fire *= 1.25
    opp.typeMults.water = 0

def a_filter        (pkmn, opp, env):
    pkmn.effs.super *= 0.75
    opp.effs.super *= 0.75

def a_flash_fire    (pkmn, opp, env):
    opp.typeMults.fire = 0

def a_flower_gift   (pkmn, opp, env):
    if env.weather == 'sun':
        pkmn.ATK.stageAdd(1)
        pkmn.SPD.stageAdd(1)

def a_forecast      (pkmn, opp, env):
    if not opp.disablesWeather():
        if env.weather == 'sun':
            pkmn.type1 = 'fire'
        elif env.weather == 'hail':
            pkmn.type1 = 'ice'
        elif env.weather == 'rain':
            pkmn.type1 = 'water'

def a_guts          (pkmn, opp, env):
    if pkmn.hasStatusCondition():
        pkmn.ATK *= 1.5
        pkmn.brnMult = 1

def a_heatproof     (pkmn, opp, env):
    pkmn.typeMults.fire *= 0.5
    opp.typeMults.fire *= 0.5

def a_huge_power    (pkmn, opp, env):
    pkmn.ATK *= 2

def a_hustle        (pkmn, opp, env):
    pkmn.ATK *= 1.5
    for move in pkmn.moves:
        if move.category == MoveCategory.physical:
            move.accuracy *= 0.8

def a_immunity      (pkmn, opp, env):
    if pkmn.status == 'psn':
        pkmn.status = ''
    # propably not correctly implemented
    
def a_insomnia      (pkmn, opp, env):
    if not opp.breaksMold():
        for move in pkmn.moves:
            if move.name == 'Rest':
                move.disable()
        for move in opp.moves:
            if move.isSleepMove():
                move.disable()

def a_iron_fist     (pkmn, opp, env):
    for move in pkmn.moves:
        if move.isPunchingMove():
            move.power *= 1.2

def a_keen_eye      (pkmn, opp, env):
    if pkmn.ACC.stage < 0:
        pkmn.ACC.stage = 0
    # Not 100% correct I believe.

def a_leaf_guard    (pkmn, opp, env):
    if env.weather == 'sun':
        pkmn.status = ''
    # TODO check for moves that are 'not effective' now

def a_levitate      (pkmn, opp, env):
    if not opp.breaksMold():
        # without the 'Sand Attack' clause, this would be:
        # opp.typeMults.ground = 0
        for move in opp.moves:
            if move.type == 'ground' and move.name != 'Sand Attack':
                move.disable()

def a_lightning_rod (pkmn, opp, env):
    for move in opp.moves:
        if move.type == 'electric': move.accuracy = None

def a_limber        (pkmn, opp, env):
    if pkmn.status == 'par':
        pkmn.status = ''
    # propably not correctly implemented

def a_magma_armor   (pkmn, opp, env):
    if pkmn.status == 'frz':
        pkmn.status = ''
    # propably not correctly implemented

def a_marvel_scale  (pkmn, opp, env):
    if pkmn.hasStatusCondition():
        pkmn.DEF.stageAdd(1)

def a_no_guard      (pkmn, opp, env):
    for move in pkmn.moves:
        move.accuracy = None
    for move in opp.moves:
        move.accuracy = None

def a_normalize     (pkmn, opp, env):
    for move in pkmn.moves:
        move.type = 'normal'

def a_pure_power    (pkmn, opp, env):
    pkmn.ATK *= 2

def a_quick_feet    (pkmn, opp, env):
    if pkmn.hasStatusCondition() or pkmn.hasVolatileStatusCondition():
        pkmn.SPE *= 1.5
        pkmn.parMult = 1

def a_reckless      (pkmn, opp, env):
    for move in pkmn.moves:
        if move.anomaly == MoveAnomaly.recoiling:
            move.power *= 1.2

def a_rivalry       (pkmn, opp, env):
    if pkmn.gender == tppVisu.pokemon.Gender.none or opp.gender == tppVisu.pokemon.Gender.none:
        mult = 1
    elif pkmn.gender == opp.gender:
        mult = 1.25
    else:
        mult = 0.75
    for move in pkmn.moves:
        move.power *= mult

def a_sand_stream   (pkmn, opp, env):
    env.weather = 'sandstorm'

def a_sand_veil     (pkmn, opp, env):
    if env.weather == 'sandstorm':
        pkmn.EVA *= 1.2

#def a_scrappy       (pkmn, opp, env):
    # TODO make this
    # Scrappy causes Ghost-type Pokémon to be hit by damage-dealing Normal- and Fighting-type moves inflicted by the user.

def a_simple        (pkmn, opp, env):
    pkmn.ATK.increment *= 2
    pkmn.DEF.increment *= 2
    pkmn.SPA.increment *= 2
    pkmn.SPD.increment *= 2
    pkmn.SPE.increment *= 2
    pkmn.ACC.increment *= 2
    pkmn.EVA.increment *= 2

def a_skill_link    (pkmn, opp, env):
    for move in pkmn.moves:
        if move.minHits == 2 and move.maxHits == 5:
            move.minHits = 5

def a_snow_cloak    (pkmn, opp, env):
    if env.weather == 'hail':
        pkmn.EVA *= 1.2

def a_snow_warning  (pkmn, opp, env):
    env.weather = 'hail'

def a_solar_power   (pkmn, opp, env):
    if env.weather == 'sun':
        pkmn.SPA.stageAdd(1)

def a_solid_rock    (pkmn, opp, env):
    opp.effs.superEff *= 0.75

def a_soundproof    (pkmn, opp, env):
    if not opp.breaksMold():
        for move in opp.moves:
            if move.isSoundMove():
                move.disable()

def a_stall         (pkmn, opp, env):
    pkmn.SPE *= 0
    # not correctly implemented
    # speed would not be actually changed, but this works for gen IV

def a_storm_drain   (pkmn, opp, env):
    for move in opp.moves:
        if move.type == 'water':
            move.accuracy = None

def a_sturdy        (pkmn, opp, env):
    if not opp.breaksMold():
        for move in opp.moves:
            if move.isOHKOMove():
                move.disable()

def a_suction_cups  (pkmn, opp, env):
    for move in opp.moves:
        if move.isSwitchMove():
            move.disable()

def a_swift_swim    (pkmn, opp, env):
    if env.weather == 'rain':
        pkmn.SPE *= 2

def a_synchronize   (pkmn, opp, env):
    if pkmn.status == 'brn' and opp.ability != 'Water Veil':
        opp.status = 'brn'
    elif pkmn.status == 'psn' and opp.ability != 'Immunity':
        opp.status = 'psn'
    elif pkmn.status == 'par' and opp.ability != 'Limber':
        opp.status = 'par'

def a_tangled_feet  (pkmn, opp, env):
    if pkmn.statusVolatile == 'confusion':
        pkmn.EVA *= 1.2

def a_technician    (pkmn, opp, env):
    for move in pkmn.moves:
        if move.power <= 60:
            move.power *= 1.5

def a_thick_fat     (pkmn, opp, env):
    opp.typeMults.ice *= 0.5
    opp.typeMults.fire *= 0.5

def a_tinted_lens   (pkmn, opp, env):
    pkmn.effs.weak *= 2

def a_trace         (pkmn, opp, env): 
    if not opp.isUntraceable():
        pkmn.ability = opp.ability

def a_unaware       (pkmn, opp, env):
    opp.ATK.stage = 0
    opp.ATK.increment = 0
    opp.DEF.stage = 0
    opp.DEF.increment = 0
    opp.SPA.stage = 0
    opp.SPA.increment = 0
    opp.SPD.stage = 0
    opp.SPD.increment = 0
    opp.SPE.stage = 0
    opp.SPE.increment = 0
    opp.ACC.stage = 0
    opp.ACC.increment = 0
    opp.EVA.stage = 0
    opp.EVA.increment = 0
    # wrong implementation, but works for gen IV. (gen V needs 'Stored Power' clause)
    # the stat changes actually do not get revoked, but just ignored in calculations

def a_vital_spirit  (pkmn, opp, env):
    if not opp.breaksMold():
        for move in pkmn.moves:
            if move.name == 'Rest':
                move.disable()
        for move in opp.moves:
            if move.isSleepMove():
                move.disable()

def a_volt_absorb   (pkmn, opp, env):
    if not opp.breaksMold():
        opp.typeMults.electric = 0

def a_water_absorb  (pkmn, opp, env):
    if not opp.breaksMold():
        opp.typeMults.water = 0

def a_water_veil    (pkmn, opp, env):
    if not opp.breaksMold() and pkmn.status == 'brn':
        pkmn.status = ''
    # propably not correctly implemented

def a_wonder_guard  (pkmn, opp, env):
    if not opp.breaksMold():
        opp.effs.weak = 0
        opp.effs.normal = 0

def a_mold_breaker  (pkmn, opp, env):
    pass  # consider taken into account

