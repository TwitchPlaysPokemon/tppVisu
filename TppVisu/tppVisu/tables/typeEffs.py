'''
Created on 28.04.2015

@author: Felk
'''
from __future__ import division

Types = {"normal"   :  0,
         "fire"     :  1,
         "water"    :  2,
         "electric" :  3,
         "grass"    :  4,
         "ice"      :  5,
         "fighting" :  6,
         "poison"   :  7,
         "ground"   :  8,
         "flying"   :  9,
         "psychic"  : 10,
         "bug"      : 11,
         "rock"     : 12,
         "ghost"    : 13,
         "dragon"   : 14,
         "dark"     : 15,
         "steel"    : 16}
#class Type(IntEnum):
#    normal   =  0
#    fire     =  1
#    water    =  2
#    electric =  3
#    grass    =  4
#    ice      =  5
#    fighting =  6
#    poison   =  7
#    ground   =  8
#    flying   =  9
#    psychic  = 10
#    bug      = 11
#    rock     = 12
#    ghost    = 13
#    dragon   = 14
#    dark     = 15
#    steel    = 16

tableTypeEffs = [
    #                                     Defenders
    #NOR  FIR  WAT  ELE  GRA  ICE  FIG  POI  GRO  FLY  PSY  BUG  ROC  GHO  DRA  DAR  STE
    [  1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 0.5,   0,   1,   1, 0.5], # NOR
    [  1, 0.5, 0.5,   1,   2,   2,   1,   1,   1,   1,   1,   2, 0.5,   1, 0.5,   1,   2], # FIR
    [  1,   2, 0.5,   1, 0.5,   1,   1,   1,   2,   1,   1,   1,   2,   1, 0.5,   1,   1], # WAT
    [  1,   1,   2, 0.5, 0.5,   1,   1,   1,   0,   2,   1,   1,   1,   1, 0.5,   1,   1], # ELE
    [  1, 0.5,   2,   1, 0.5,   1,   1, 0.5,   2, 0.5,   1, 0.5,   2,   1, 0.5,   1, 0.5], # GRA
    [  1, 0.5, 0.5,   1,   2, 0.5,   1,   1,   2,   2,   1,   1,   1,   1,   2,   1, 0.5], # ICE
    [  2,   1,   1,   1,   1,   2,   1, 0.5,   1, 0.5, 0.5, 0.5,   2,   0,   1,   2,   2], # FIG
    [  1,   1,   1,   1,   2,   1,   1, 0.5, 0.5,   1,   1,   1, 0.5, 0.5,   1,   1,   0], # POI
    [  1,   2,   1,   2, 0.5,   1,   1,   2,   1,   0,   1, 0.5,   2,   1,   1,   1,   2], # GRO   Attackers
    [  1,   1,   1, 0.5,   2,   1,   2,   1,   1,   1,   1,   2, 0.5,   1,   1,   1, 0.5], # FLY
    [  1,   1,   1,   1,   1,   1,   2,   2,   1,   1, 0.5,   1,   1,   1,   1,   0, 0.5], # PSY
    [  1, 0.5,   1,   1,   2,   1, 0.5, 0.5,   1, 0.5,   2,   1,   1, 0.5,   1,   2, 0.5], # BUG
    [  1,   2,   1,   1,   1,   2, 0.5,   1, 0.5,   2,   1,   2,   1,   1,   1,   1, 0.5], # ROC
    [  0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   1,   1,   2,   1, 0.5, 0.5], # GHO
    [  1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   1, 0.5], # DRA
    [  1,   1,   1,   1,   1,   1, 0.5,   1,   1,   1,   2,   1,   1,   2,   1, 0.5, 0.5], # DAR
    [  1, 0.5, 0.5, 0.5,   1,   2,   1,   1,   1,   1,   1,   1,   2,   1,   1,   1, 0.5], # STE
]

def getEff(type1name, type2name):
    type1 = Types[type1name]
    type2 = Types[type2name]
    return tableTypeEffs[type1][type2]