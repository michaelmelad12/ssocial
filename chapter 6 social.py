#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx


# In[6]:


G = nx.Graph()
nx.add_cycle(G,[0, 1, 2, 3])
nx.add_cycle(G,[4, 5, 6, 7])
G.add_edge(0, 7)
nx.draw(G, with_labels=True)


# In[7]:


partition = [
    {1, 2, 3},
    {4, 5, 6},
    {0, 7},
]


# In[8]:


nx.community.is_partition(G, partition)


# In[9]:


partition_map = {}
for idx, cluster_nodes in enumerate(partition):
    for node in cluster_nodes:
        partition_map[node] = idx

partition_map


# In[10]:


partition_map[0] == partition_map[7]


# In[11]:


node_colors = [partition_map[n] for n in G.nodes]
        
nx.draw(G, node_color=node_colors, with_labels=True)


# In[13]:


def modularity(G, partition):
    W = sum(G.edges[v, w].get('weight', 1) for v, w in G.edges)
    summation = 0
    for cluster_nodes in partition:
        s_c = sum(G.degree(n, weight='weight') for n in cluster_nodes)
        # Use subgraph to count only internal links
        C = G.subgraph(cluster_nodes)
        W_c = sum(C.edges[v, w].get('weight', 1) for v, w in C.edges)
        summation += W_c - s_c ** 2 / (4 * W)
    
    return summation / W


# In[14]:


modularity(G, partition)


# In[15]:


partition_2 = [
    {0, 1, 2, 3},
    {4, 5, 6, 7},
]
modularity(G, partition_2)


# In[16]:


nx.community.quality.modularity(G, partition_2)


# In[25]:


K = nx.karate_club_graph()
nx.draw(K, with_labels=True)


# In[26]:


K.nodes[0]


# In[28]:


K.nodes[9]


# In[29]:


K = nx.karate_club_graph()
club_color = {
    'Mr. Hi': 'orange',
    'Officer': 'lightblue',
}
node_colors = [club_color[K.nodes[n]['club']] for n in K.nodes]
nx.draw(K, node_color=node_colors, with_labels=True)


# In[31]:


groups = {
    'Mr. Hi': set(),
    'Officer': set(),
}

for n in K.nodes:
    club = K.nodes[n]['club']
    groups[club].add(n)
    
groups


# In[32]:


empirical_partition = list(groups.values())
empirical_partition


# In[33]:


nx.community.is_partition(K, empirical_partition)


# In[34]:


nx.community.quality.modularity(K, empirical_partition)


# In[35]:


random_nodes = random.sample(K.nodes, 17)
random_partition = [set(random_nodes),
                    set(K.nodes) - set(random_nodes)]
random_partition


# In[36]:


random_node_colors = ['orange' if n in random_nodes else 'lightblue' for n in K.nodes]
nx.draw(K, node_color=random_node_colors)


# In[ ]:




