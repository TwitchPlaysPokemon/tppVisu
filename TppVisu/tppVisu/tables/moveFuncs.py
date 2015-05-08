'''
Created on 29.04.2015

@author: Felk
'''
from tppVisu.pokemon import Gender

class MoveOverwrites(object):
    def __init__(self):
        self.damage = None
        self.power = None
        self.notice = None

def call(move, pkmn, opp, env):
    funcname = 'm_' + move.name.lower().replace(' ', '_').replace('-', '_')
    ovwr = MoveOverwrites()
    try:
        ovwr.notice = globals()[funcname](move, pkmn, opp, env, ovwr)
        return ovwr
    except KeyError:
        # no notice by default. Assume unhandled moves are regular attacks
        return ovwr

#####################################################
#          MOVE   IMPLEMENTATIONS   BELOW           #
#####################################################

# sample method declaration. lowercase, prefixed with m_ and spaces/- written as _
# takes the move, user's and opponent's pokemon plus an environment (see util) as params.
# Also takes a overwrite variable, containing variables that can be overwritten for calculation 
# Can return a string with a notice message for extra information
def m_sample_move   (move, pkmn, opp, env, ovwr):
    pass

def m_attract       (move, pkmn, opp, env, ovwr):
    if pkmn.gender == Gender.none or opp.gender == Gender.none or pkmn.gender == opp.gender:
        move.disable()
    
def m_blizzard      (move, pkmn, opp, env, ovwr):
    if env.weather == 'hail':
        move.accuracy = 100
        
def m_crush_grip    (move, pkmn, opp, env, ovwr):
    ovwr.power = (1, 121)
    return 'the more HP the opponent has, the more damage does this move'
    
def m_dragon_rage   (move, pkmn, opp, env, ovwr):
    ovwr.damage = (40, 40)
    
def m_explosion     (move, pkmn, opp, env, ovwr):
    move.power *= 2
    
def m_facade        (move, pkmn, opp, env, ovwr):
    if pkmn.hasStatusCondition():
        move.power *= 2
    
def m_frustration   (move, pkmn, opp, env, ovwr):
    move.power = (255 - pkmn.happiness) / 2.5
    if move.power == 0:
        move.power = 1
        
def m_grass_knot    (move, pkmn, opp, env, ovwr):
    if opp.weight < 0.1:
        move.disable()
    elif opp.weight < 10:
        move.power = 20
    elif opp.weight < 25:
        move.power = 40
    elif opp.weight < 50:
        move.power = 60
    elif opp.weight < 100:
        move.power = 80
    elif opp.weight < 200:
        move.power = 100
    else:
        move.power = 120
        
def m_gyro_ball     (move, pkmn, opp, env, ovwr):
    move.power = 25 * (opp.SPE.get() / pkmn.SPE.get())
    
def m_low_kick      (move, pkmn, opp, env, ovwr):
    if opp.weight < 0.1:
        move.disable()
    elif opp.weight < 10:
        move.power = 20
    elif opp.weight < 25:
        move.power = 40
    elif opp.weight < 50:
        move.power = 60
    elif opp.weight < 100:
        move.power = 80
    elif opp.weight < 200:
        move.power = 100
    else:
        move.power = 120
    
def m_magnitude     (move, pkmn, opp, env, ovwr):
    ovwr.power = (10, 150)
    
def m_night_shade   (move, pkmn, opp, env, ovwr):
    ovwr.damage = (pkmn.level, pkmn.level)
    
def m_psywave       (move, pkmn, opp, env, ovwr):
    ovwr.damage = (0.5 * pkmn.level, 1.5 * pkmn.level)
    # TODO typeless move
    
def m_punishment    (move, pkmn, opp, env, ovwr):
    stagenum = 0
    stagenum += max(0, opp.ATK.stage)
    stagenum += max(0, opp.DEF.stage)
    stagenum += max(0, opp.SPA.stage)
    stagenum += max(0, opp.SPD.stage)
    stagenum += max(0, opp.SPE.stage)
    move.power = min(200, 60 + 20 * stagenum)
    
def m_return        (move, pkmn, opp, env, ovwr):
    move.power = pkmn.happiness / 2.5
    if move.power == 0:
        move.power = 1
        
def m_reversal      (move, pkmn, opp, env, ovwr):
    # TODO Does more damage as the user's HP decreases
    ovwr.power = (20, 200)
    
def m_secret_power  (move, pkmn, opp, env, ovwr):
    return 'can cause secondary effect'
    
def m_seismic_toss  (move, pkmn, opp, env, ovwr):
    ovwr.damage = (opp.level, opp.level)
    
def m_self_destruct (move, pkmn, opp, env, ovwr):
    move.power *= 2
    
def m_smelling_salts(move, pkmn, opp, env, ovwr):
    if opp.status == 'par':
        move.power *= 2
        
def m_sonic_boom    (move, pkmn, opp, env, ovwr):
    ovwr.damage = (20, 20)
    
def m_spit_up       (move, pkmn, opp, env, ovwr):
    # TODO varies in power depending on the number of uses of stockpile
    ovwr.power = (100, 300)
    return '1,2 or 3 stockpiles = 100, 200 or 300 base power'
    
def m_thunder       (move, pkmn, opp, env, ovwr):
    if env.weather == 'rain':
        move.accuracy = 100
        
def m_triple_kick   (move, pkmn, opp, env, ovwr):
    # hack for: 3 hits with 10, 20, 30 base power.
    # 10 minimum, or avg. 20 for maximum
    ovwr.power = (10, 20)
        
def m_trump_card    (move, pkmn, opp, env, ovwr):
    # TODO power increases as PP decreases
    ovwr.power = (40, 200)
    return '4+, 3, 2, 1, 0 PP after use = 40, 50, 60, 80, 200 base power'
    
def m_wake_up_slap  (move, pkmn, opp, env, ovwr):
    # TODO base power doubles if used on a sleeping target. Wakes up
    return ''
    
def m_weather_ball  (move, pkmn, opp, env, ovwr):
    if env.weather != 'none':
        move.power *= 2
        if env.weather == 'sun':
            move.type = 'fire'
        elif env.weather == 'rain':
            move.type = 'water'
        elif env.weather == 'hail':
            move.type = 'ice'
        elif env.weather == 'sandstorm':
            move.type = 'rock'
            
def m_wring_out     (move, pkmn, opp, env, ovwr):
    # TODO base power depends on the target's remaining HP
    ovwr.power = (1, 121)
    return 'the more HP the opponent has, the more damage does this move'