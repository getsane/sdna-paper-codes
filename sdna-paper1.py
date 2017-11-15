
# coding: utf-8

# ## SDNA PAPER EVALUATION - 11/13/2017

# In[2]:

import numpy as np
import pandas as pd
import networkx as nx
import random
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib notebook')


# ### Generating a random network with communities [Liu & Hu, 2005]

# In[ ]:

def graph_gen_random(n_nodes =30, n_groups =3, prob_in = 0.10, prob_ac = 0.03):
    
    '''
    Parameters:
    ----------
    n_nodes: Number of nodes
    n_groups: Number of communities
    prob_in: Probability of connections within communities
    prob_out: Probability of connections across communities.
    
    Note: prob_out << prob_in
        
    Output: 
    -------
    Networkx Graph Object
    
    Notes:
    ------
    The approach is as follows: 
    - Generate nodes and assign them to groups
    - Within group connect the nodes with a high probability
    - Put them into a graph (leverage Networkx graph)
    - Iterate over all the nodes of the graph to assign connections to nodes
       across the groups at a lower selected probability.
    
    '''

    lt = [(i,random.randint(1,n_groups)) for i in range(1, n_nodes+1) ] 

    groups = set([gr for nr,gr in lt])

    # Create a list of list of tuples of nodes (nodes within a group) This now gives me
    # the distribution of nodes in the various groups for future use.

    newlist = []

    for gr in groups:
        newlist.append([node for node,group in lt if group == gr])

 
    # Create data structure (of nodes) that can be consumed by the NetworkX
    # graph class 

    #take each list within a list and create a tuple among them

    list_nodes = []
    for items in newlist:
        for nodes in items:
            for nodes1 in items:
                if nodes1 > nodes and random.uniform(0,1)<prob_in:
                    list_nodes.append((nodes, nodes1))

    # Add the nodes to a graph
    G = nx.Graph()
    G.add_edges_from(list_nodes)

    # Take all the nodes and connect them across groups
    for nodes in G.nodes():
        for nodes1 in G.nodes():
            if nodes1 > nodes and (random.uniform(0,1)<prob_ac) :
                G.add_edge(nodes,nodes1)

    return G

#testing = graph_gen_random() 
#print(testing.nodes(data=True))


# ### Generating a scale free network with communities [Huang & Li, 2007]

# #### Step 1 Initialization of communities 

# In[3]:

n_groups = 5
n_nodes = 100
lt = [(i,random.randint(1,n_groups)) for i in range(1, n_nodes+1)] # no zero as node


# In[148]:

# take each list within a list and create a tuple among them


# In[4]:

groups = set([gr for nr,gr in lt])

newlist = []
for gr in groups:
    newlist.append([(node,gr) for node,group in lt if group == gr])


# In[40]:

list_nodes = []
for items in newlist:
    for nodes,gr2 in items:
        for nodes1,gr3 in items:
            if nodes1 > nodes:
                list_nodes.append((nodes, nodes1,gr2, gr3))


# In[41]:

# Adding inter-community links (M(M-1)/2)


# In[42]:

for index1, items1 in enumerate(newlist):
    node1,group1 = random.choice(items1) 
    for index2, items2 in enumerate(newlist):
        if index2 > index1:
            node2,group2 = random.choice(items2) 
            list_nodes.append((node1,node2,group1,group2))    


# In[43]:

# Converting into Panda data frame (easier to view the structure)


# In[44]:

lt1 = pd.DataFrame(list_nodes, columns = ['node_start','node_end', 'groupofstartnode','groupofendnode'])
#lt1['st-end-nodes'] = list(zip(lt1.node_start, lt1.node_end))


# In[45]:

# Calculate within-community degree for each node - This will be required for the PA growth


# In[46]:

# Degree within community
lt1['degreestart'] = lt1.groupby(by=['groupofstartnode','node_start'])['node_start'].transform(len)


# In[47]:

# Degree outside community (inter-community degree)
lt1['degree_out']= lt1[lt1['groupofstartnode'] != lt1['groupofendnode']].groupby('node_start')['node_start'].transform(len)
#lt1[lt1['groupofstartnode'] != lt1['groupofendnode']]

# Taking care of NANs
lt1['degree_out'].fillna(0, inplace = True)


# In[72]:

# within group fitness of each node in a community
lt1['fitness_in'] = lt1['degreestart']/(lt1.groupby(by=['groupofstartnode'])['groupofstartnode'].transform(len))


# In[109]:

#lt1['fitness_out'] = lt1['degree_out']/(lt1[lt1['groupofstartnode'] != lt1['groupofendnode']].groupby('node_start')['node_start'].transform(len))

#lt1['fitness_out'] = lt1['degree_out']/(lt1[lt1['groupofstartnode'] != lt1['groupofendnode'],'node_start'].transform(len))


# In[106]:

# Putting in a graph

#G = nx.from_pandas_dataframe(lt1, source='node_start',target = 'node_end',edge_attr=['groupofstartnode','groupofendnode','degreestart'])


# #### Step 2: grow the network & step  3: (PA -- inner community, -- intra community)

# The purpose is to grow the graph by adding new nodes. Each new node is first assigned to a random community. Then it creates `m` links
# to `m` other nodes in the same community. This happens based on the number of degrees of the nodes.
# This node also connects to `n` other nodes in other communities based on their inter-community degrees. That is, the new nodes are 
# attracted to nodes in other communities who connected to other communities.
# 
# Step 3 - Preferential Attachments:
# a) Inner-community preferential attachment: When choosing nodes in the same community (we denote it as the
# jth community) to which the new node connects through inner-community links, we assume that the probability Π
# that a new node will be connected to node i in community j depends on the inner-degree sij (defined as the number
# of inner-links connected to node i) of that node, such that $\Pi(s_{ij})=\frac{s_{ij}}{\sum_{k} S_{kj}}$
# 
# b) Inter-community preferential attachment: When choosing the nodes in other communities to which the new node
# connects through inter-community links, we assume that the probability Π that a new node will be connected to node
# i in community k(k 6= j) depends on the inter-degree lik (defined as the number of inter-links connected to the node),
# such that 
# $\Pi(l_{ik})=\frac{l_{ik}}{\sum_{m,n, n \neq j} l_{kj}}$

# In[ ]:

# generate random number of link (FIXED)
n_edges_in = min([len(items) for items in newlist]) # from the same community, # number of edges  within community (FIXED)

# one link across each community - Fix the # of 
n_edges_out = random.choice(list(groups)) 


# In[ ]:

newnodes = []
for i in range(101,501):
    # choose random community to add new node
    rn = random.randint(1,3)
    random.sample(newlist[rn],n_edges_in
    #newlist[rn].append((i,rn))  #updates the newlist
    lt1.loc['groupofstartnode'== rn].
    while n_edges_in > 0:
        for j in newlist[rn]:
            if i != j:
                if random.uniform()
        newnodes.append((i,j, rn) 
    


# In[166]:

#sorted(lt1.loc[lt1.groupofstartnode == 1,["node_start", "fitness_in"]].drop_duplicates().set_index("node_start").to_dict().get('fitness_in').values(), reverse =True)


# In[171]:

random.sample([1,2,3,4,5],4)


# In[ ]:



