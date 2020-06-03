# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:02:07 2020

@author: Ashish
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import bipartite

dataset = pd.read_excel("MedicalExperta(1).xlsx")
dataset = dataset.iloc[:,3:]
dataset = dataset.iloc[6:,:]

columns = dataset['Unnamed: 3'].to_list()
rows = dataset.iloc[0,:].to_list()
disease = rows[1:]
symptoms=columns[1:]

    
dataset1 = dataset.iloc[1:,1:]
dataset2=dataset1.values

final_dict={}
temp=0
for i in range(dataset2.shape[0]):
    temp1=0
    for j in range(dataset2.shape[1]):
        if(dataset2[i,j]=='yes'):
            if disease[temp1] in final_dict:
                final_dict[disease[temp1]].append(symptoms[temp])
            else:
                final_dict[disease[temp1]]=[symptoms[temp]]
                
        temp1+=1
    temp+=1
        
G=nx.Graph()
G.add_nodes_from(final_dict.keys(), bipartite=1)
G.add_nodes_from(symptoms, bipartite=0)

for i in final_dict.keys():
    for j in final_dict[i]:
        G.add_edge(i,j)

X, Y = bipartite.sets(G)
pos = dict()
pos.update( (n, (1, i)) for i, n in enumerate(X) ) 
pos.update( (n, (2, i)) for i, n in enumerate(Y) ) 
nx.draw(G, pos=pos,with_labels=True)
plt.savefig(f'./Knowledge_Graph.png')
plt.show()


