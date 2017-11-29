# !usr/env/python
# -*-encoding: utf-8 -*-

# Simpath by Goyal et al 
# Sandeep @ 11/27/17


import os, sys
import logging
import networkx as nx

# 1) Get a directed graph for play
DG = nx.DiGraph()

DG.add_weighted_edges_from([(1,2,0.5),
    (1,3,0.75),(6,1,0.25),(1,9,0.2),(7,1,0.75),(2,3,0.25),(5,2,0.15),(2,8,0.15)])



#2) Function simpath-spread

def simpath_spread(S, tol, U):
    ''' Algorithm 1 in paper
    
    '''
    
    spread_S = 0      # Marginal benefit of mb(S)
    
    W1 = [v for v in DG.nodes() if v not in S]  # V - S

    for s in S:
        W1.append(s)                            # V - S + s
        W = DG.subgraph(W1)  # creating a subgraph
        spread_S = spread_S + backtrack(s, tol, W, U=None)
    
    return spread_S

    
#3) Function Backtrack

def backtrack(u, tol, W, U=None):

    ''' Algorithm 2 in paper - called backtrack
    This function like a shift operator. By switching the focus on the next
    node to be operated by the forward algorithm shown below. 
    
    '''
    D = {}
    Q = [u]      # adding to u to Q (list)
    D[u] = []    # Dictionary: {node: {visited neighbors}}
    spd = 1      # initial value of spread
    pp = 1       # intial pp simple path weight
    

    while Q:     # is not None:

        Q,D,spd,pp = forward(Q,D,spd,pp,tol,W,U)
        print(Q)
        print(D)
        print('we are here')
        
        if Q :
            print('ahoy!', Q)
            u = Q[-1]        # make this as the last node from forward so that it can be forwarded
        
            Q.remove(u)      # remove the old u; this can make Q empty
        
            print('length', len(Q)) 
            if len(Q) >= 2:
                v = Q[-1]        # second last from Q 
        
                try: 
        
                    w1= W.edge[u][v]['weight']
                    pp = pp+ (pp/(w1))  # (u, v): 
                except: 
                    pass


        if u in D:
            del D[u]
                
                    
        # problem with the last element being the last node on a path so there
        # is no weight need to use try-error

            
    return spd

#4) Function Forward

def forward(Q,D,spd,pp,tol,W,U=None):

    ''' Algorithm 3 in paper - Forward Algorithm enumerates all (active) nodes
    on a given path starting from a given node.
    
    '''

    x = Q.pop() #Q[-1] #                    # keeping this as a list; extract last element
    D[x] = [] 
    nout_x = W.successors(x)    # list of immediate successor of x in graph W
    
    while nout_x: # is not None:
        
        for succ in nout_x:
            print(succ)
            print(D)
            print(Q)
            print(W.nodes())
            print(x)
            if (succ not in Q) and (succ not in D[x]) and (succ in W.nodes()):

                wght = W.edge[x][succ]['weight'] # assuming in data 'weight'
                print(wght) 
                if pp*wght < tol:
                
                    D[x] = D[x] + [succ] # keeping track of outneighbors
        
                else:
                    Q = Q + [succ]
                    pp = pp*wght 
                    spd = spd + pp
                    D[x] = D[x] + [succ]
            else:
                continue
        
        
                    
        print('MyQ', Q)
        x = Q[-1]       # Take the last element look for its successors 
        print('Dx', D)
        #D[x] = []
        nout_x = W.successors(x)

    return (Q,D,spd,pp)


def main():
     
    print(simpath_spread(S=[1,2,3,9],tol=0.05,U=None))          


if __name__ == "__main__" :
    main()

#5) Assembly of SIMPATH with CELF

#def simpath():
#    ''' Algorithm 4 in paper '''
#    pass
