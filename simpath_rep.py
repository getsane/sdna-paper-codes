# !usr/env/python
# -*-coding: utf-8 -*-

# Simpath by Goyal et al 

__author__ = ['Sandeep @ 11/27/2017']

__all__ = ['Simpath Replication']




import os, sys
import logging
import networkx as nx

# Function simpath-spread

def simpath_spread():
    ''' Algorithm 1 in paper '''
    path_calc = S

    for u in S:
        path_calc = path_calc + backtrack(
    pass

# Function Backtrack

def backtrack(u, tol=0.1, W, U):
    ''' Algorithm 2 in paper '''
    Q = Q + {u}
    spd = 1
    pp = 1
    D = None
    
    while Q is not None:
        Q,D,spd,pp = forward(Q,D,spd,pp,tol,W,U)
        u = Q[-1]
        Q = Q - u
        del D[u]
        v = Q.last()
        pp = pp/(b_vu)

    return spd

# Function Forward

def forward(Q,D,spd,pp,tol=0.1,W,U):
    ''' Algorithm 3 in paper '''
    x = Q.last()

    

# SIMPATH

def simpath():
    ''' Algorithm 4 in paper '''
    pass
