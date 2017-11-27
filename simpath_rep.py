# !usr/env/python
# -*-coding: utf-8 -*-

# Simpath by Goyal et al 
# Sandeep @ 11/27/17


import os, sys
import logging
import networkx as nx

# 1) Get a directed graph for play
DG = nx.DiGraph(50)

DG.add_weighted_edges_from([(1,2,0.5), (3,1,0.75),(6,1,0.25),
    (7,1,0.75),(2,3,0.25),(5,2,0.15)])


#2) Function simpath-spread

def simpath_spread():
    ''' Algorithm 1 in paper '''
    path_calc = S

    for u in S:
        path_calc = path_calc + backtrack(
    pass

#3) Function Backtrack

def backtrack(u, tol=0.1, W, U):
    ''' Algorithm 2 in paper '''
    Q = Q + [u]  # adding to u to Q (list)
    spd = 1      # initial value of spread
    pp = 1       # intial pp simple path weight
    D = {}       # Dictionary: {node: {visited neighbors}}
    
    while Q is not None:
        Q,D,spd,pp = forward(Q,D,spd,pp,tol,W,U)
        Q.remove(u) # remove the old u 
        del D[u]
        u = Q[-1]   # make us as the last node from forward so that it can be forwarded
        v = Q[-1]
        pp = pp/()

    return spd

#4) Function Forward

def forward(Q,D,spd,pp,tol=0.1,W,U=None):
    ''' Algorithm 3 in paper 
    This function operates on each node?
    
    '''

    x = Q[-1]                # keeping this as a list; extract last element
    nout_x = W.successors(x) # list of immediate successor of x in graph W
    Dx = []                  # this needs to be initialized earlier as
                             # Dictionary or something  

    for succ in nout_x:
        wght = W.edge[x][succ]['weight'] # assuming in data 'weight'

        if succ not in Q: 
            if succ not in Dx: 
                if succ in W:
                    if pp*wght < tol:
                        Dx = D[x] + [succ] # keeping track of outneighbors
                    else:
                        Q = Q + [succ]
                        pp = pp*wght 
                        spd = spd + pp
                        Dx = Dx + [succ]
                        x = Q[-1]  # what is happening here?
    return (Q,D,spd,pp)
            
            
        
#5) Assembly of SIMPATH with CELF

def simpath():
    ''' Algorithm 4 in paper '''
    pass
