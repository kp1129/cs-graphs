"""how to solve any graph problem:

1. translate the problem into graph terms (vertices, edges, weights?)
2. build the graph
3. traverse

___________________________________________
terminology

-a TRIVIAL graph is a graph with only one vertex
-a NULL graph is a graph with no edges. it may have one or more vertices.

-nodes/vertices/vertexes = the data components of the graph
-edges = the connections between nodes

-directed graphs have one-way edges
-undirected graphs have all the edges point both ways.
(if two nodes are connected by a straight line, with no arrows,
you may assume it's an undirected graph and the edges point both ways.)

-cyclic = there is at least one "loop", or at least one way to get back
to the same node from which you started. doesn't have to look 
like a circle. undirected graph that has edges that point both ways 
is also cyclic. a single node that has an edge that points to itself is also cyclic.

-acyclic = there are no "loops" at all, you can never get back to the same node 
from which you started. all directed graphs are acyclic. 
even if they form a circular shape on a graph (like, a points to b and c, 
b points to c, and c doesn't point anywhere but u can get there by 2 different edges.)

-dense graphs = high ratio of edges to nodes, nodes are connected to many other nodes
-sparse graphs = nodes are connected to few other nodes

-weighted graphs = graphs where the edges have associated weights
(think of weights as a cost of travel between two nodes). 
if the edges don't have weights written out, assume they're all 
weighted equally (i.e., they're unweighted). 
weights can represent time, fuel, distance, cost, road conditions, traffic volume, 
terrain difficulty, bandit risk, etc
-unweighted graphs = graphs where edges do not have weights/ are all the same weight.

graph representations

-adjacency matrix = a matrix of nodes (2d array, or list of lists) 
that has 0/1 or true/false inside the square if the nodes connect. 
can also use the squares to specify edge weights (0 = no edge, 
4 = weight of 4, 10 = weight of 10, etc)

example:

    a   b
a   0   1

b   1   0

-adjacency list = instead of keeping track of every possible 
connection like in the adjacency matrix, 
we only keep track of the ones that exist.

example:
{
    a: [b],
    b: [a]
}

*multiple nodes can have the same value. they're still different nodes.
*you don't always have to store the neighbors. if there's a way to calculate a node's neighbors
on the fly, then do that on the fly while implementing the traversing algorithms

*how to avoid getting stuck in cycles in a cyclical graph: use a visited set.
check to see if the vertex where you've arrived is already in visited set, and if it is, ignore it.

___________________________________________________________________________
breadth-first traversal:
-traverse the graph from the given starting node
-not just iterate, but traverse in a specific order: the starting node first, then the nodes that
the starting node is connected to (its neighbors), then each of the neighbors' neighbors, etc. this looks
side-to-side in a binary tree, but in a graph it can look radial or diagonal, 
because the starting node will not always be the first one on top. the order of the neighbors doesn't
matter, as long as they're all in the same 'level' (i.e., first all the neighbors of the starting node, 
then all the neighbors of each of the neighbors of the starting node, etc). 
-IT TURNS OUT that this is the BEST WAY to find the shortest path between two nodes!
REMEMBER THIS.

init: add starting node to the queue (for breadth-first, use queue always, 
because it's a first in - first out structure).

while queue is not empty:
    dequeue a node
    if visited, ignore it
    else: (or literally: if node not in visited)
        add all of node's neighbors to the queue
        mark node as visited

^ this is a simple algorithm that does a really complicated thing! <3     
________________________________________________________________________________
depth-first traversal:
-traverse the graph from the given starting node
-again, not just iterate but traverse in a specific order: starting node, then its neighbors but
for each neighbor explore its neighbors (and each of those neighbors' neighbors, until a dead-end node)
before moving on to the next neighbor. Basically like with binary search trees, once you start
heading out in a direction in depth-first traversal, you don't come back until you explore the entire subset
of that tree/graph.
-for depth-first traversal, use a stack (in the same way we used a queue for breadth-first). stack is
first in - last out structure. so if you start with A and add B and C to the stack, then pop off B, explore it,
and add it's children D and E not to the end (like in a queue) but to the top of the stack, so that you
end up with a stack of D, E, C. then pop off D, explore it, add it's children/neighbors to the top of the stack...etc
This is what ensures that you explore the subset of the graph all the way before you move on to the next neighbor.
stack is keyyyy

init: add starting node to the stack (for depth-first, use stack always, 
because it's a first in - last out structure).

while stack is not empty:
    pop off a node
    if visited, ignore it
    else: (or literally: if node not in visited)
        add all of node's neighbors to the top of the stack
        mark node as visited
___________________________________________________________________________________________________
breadth-first search:
-works like a breadth-first traversal, but it gives us a PATH from one node to another.
-for breadth first search, you want to store not only the nodes 
you visited but the exact path you took to get there.
-because it's breadth first, the result of the search is the shortest path.
-note, this search is for graphs with unweighted edges.
-to find the shortest path in a graph THAT HAS WEIGHTED EDGES, use Dijkstra's algorithm!!
we don't go over it in class but look it up. 

init: instantiate a queue, enqueue a list that contains starting node (this is a path list)
create a visited set

while queue is not empty:
    dequeue first path from the front of the queue
    grab the last vertex from the path (the most recent neighbor added)
    if that vertex has not been visited:
        IS IT THE TARGET? IS THIS WHAT WE ARE LOOKING FOR? if yes:
            return the path we just dequeued
        else:
            visit it/add it to visited
            get all of its neighbors and for each:
                copy the path it took to get here
                append the neighbor to the path
                enqueue the copy of the path with the neighbor added

_____________________________________________________________________________________
*interesting application of a depth first traversal/search: drawing a maze, where it's not 
practical to draw everything close to the starting point and then radiate out, but you want to 
draw the entire path to the end first before coming back and picking up another path 


more on graphs: (specifically the terminology)
https://www.statisticshowto.com/graph-theory/

__________________________________________________________
connected components
-a set of nodes that is connected to one another in some way

-graphs can have multiple sets of connected nodes that are disjoint

-a set of connected nodes is called a connected component

counting connected components:
while there are unvisited nodes:
        choose an unvisited node
        traverse from that node, marking each as visited
        increment connected component counter
or

for each node in the graph:
        if it's unvisited:
            traverse from that node, marking each as visited
            increment connected component counter










"""