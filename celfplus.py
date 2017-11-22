#! python3.6


def clef_pl2():
    
    ''' clef_pl2 is a function to implement the CLEF++ algorithm by Goyal
    et al
    #-----------------------------
    Defined:
    S: seed set (objective)
    Q: List of tuples. Collecting information.
    last_seed:
    cur_best: The best node in the current iteration
    u_mg1: Marginal gain in spread(S+{v})
    u_mg2: Marginal gain in spread(S + {prev_best})

    #-----------------------------
    Output:
    S: seed set
    
    #-----------------------------
    Recording: 
    
    #-----------------------------
    '''
    
    S = [] # Seed set
    q = [] # Intermediate list of tuples --> Q
    Q = [] # list of tuples
    
    # Simple case iterating once through each node

    for index, v in V:
        s_v = (spread(v)
        s_Sv = spread(S.append(v))
        vmg = s_Sv - s_v
        q.append((v,s_v,s_Sv,vmg,1*q[]vmg))
        if q[index-1][4] == ():
            if q[index-1][4]> q[index][4]:
                q[index
        sorted(q, ke_index=[3])
        



