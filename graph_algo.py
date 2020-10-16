import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import math

# all_data[x][y] -> zero'd out np array, x goes from 0-99, y goes from 0-999999
# x_axis and y_axis hold the required values for plotting 
all_data = np.zeros((100,1000000))
y_axis = np.zeros(1000000)
x_axis = np.zeros(1000000)

# Generating a valid graph
G = nx.Graph()

# Generating the randomized graph
for graph_iterator in range(100):
   
    # Edge assignments    
    for x in range(1, 11):
        for y in range(x+1, 11):
            G.add_edges_from([(x,y)], relationship=random.choice([-1, 1]))   

    # Running dynamic algorithm 1000000 times
    for triad_iterator in range(1000000):
        
        # Picking a random triad
        l = random.sample(range(1, 11), 3)
        edge_1 = G[l[0]][l[1]]["relationship"]
        edge_2 = G[l[0]][l[2]]["relationship"]
        edge_3 = G[l[1]][l[2]]["relationship"]
        
        # Triad balanced 
        if ((edge_1 * edge_2 * edge_3) == 1):
            all_data[graph_iterator][triad_iterator] = all_data[graph_iterator][triad_iterator - 1]
            continue
        
        # Triad unbalanced
        else:
            chosen_edge = random.sample(l , 2)
            chosen_edge_weight = -(G[chosen_edge[0]][chosen_edge[1]]["relationship"])
            G.add_edges_from([(chosen_edge[0],chosen_edge[1])], relationship=chosen_edge_weight)
        
        # Storing number of balanced triads/total number of triads
        balanced_triad_counter = 0    
        for x in range(1, 11):
            for y in range(x+1, 11):
                for z in range(y+1, 11):    
                    edge_1 = G[x][y]["relationship"]
                    edge_2 = G[y][z]["relationship"]
                    edge_3 = G[x][z]["relationship"]
                    
                    if ((edge_1 * edge_2 * edge_3) == 1):
                        balanced_triad_counter += 1

        all_data[graph_iterator][triad_iterator] = (balanced_triad_counter/120)
    
    # Clearing up the graph
    G.clear()
    
# Setting up the y axis
for i in range(1000000):
    for y in range(100):
        y_axis[i] += all_data[y][i] 
y_axis = y_axis/100

# Setting up the x axis
for i in range(1000000):
    x_axis[i] = math.log(i+1)

# Plotting 
plt.plot(x_axis, y_axis)
plt.xlabel('log(i)')
plt.ylabel('# of balanced triad/total number of triads')
plt.title('Proportion of balanced triads over 1000000 iterations')
plt.show()