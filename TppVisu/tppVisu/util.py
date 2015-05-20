'''
Created on 29.04.2015

@author: Felk

(non-categorized) utilities and utility-objects used for the visualizer.
'''
from __future__ import division, print_function

from collections import namedtuple


def enum(**enums):
    return type('Enum', (), enums)

Eff = enum(NOT='not', WEAK='weak', NORMAL='normal', SUPER='super')

class Effs(object):
    def __init__(self, SUPER, NORMAL, WEAK, NOT):
        self.SUPER = SUPER
        self.NORMAL = NORMAL
        self.WEAK = WEAK
        self.NOT = NOT

class Environment(object):
    def __init__(self, weather='none'):
        self.weather = weather
        # TODO maybe add terrain for move 'Secret Power'

class TypeSet(object):
    def __init__(self, normal=1, fire=1, water=1, electric=1, grass=1, ice=1, fighting=1, poison=1, ground=1, flying=1, psychic=1, bug=1, rock=1, ghost=1, dragon=1, dark=1, steel=1):
        self.normal = normal   ;   self.fire = fire     ;   self.water = water
        self.grass = grass     ;   self.ice = ice       ;   self.fighting = fighting
        self.poison = poison   ;   self.ground = ground ;   self.flying = flying
        self.psychic = psychic ;   self.bug = bug       ;   self.rock = rock
        self.ghost = ghost     ;   self.dragon = dragon ;   self.dark = dark
        self.steel = steel     ;   self.electric = electric

# namedtuples as convenient 'data bags'. They are like immutable structs.
# stats uppercase, because 'def' is a keyword
Stats = namedtuple('Stats', 'HP ATK DEF SPA SPD SPE')
Stages = namedtuple('Stages', 'ATK DEF SPA SPD SPE ACC EVA')
