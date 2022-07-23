# Graph Algorithms


## Glossary and Syntax

**Graph**: Abstractly, a graph is a set of objects and the relationship between those objects.

In the context of graph algorithms, a graph is defined as a collection of **vertices** and **edges**, and is written as $G = (V, E)$.

**Vertex**: A point/object in a graph, the set of which is usually written as $V$.

**Edge**: A pairwise relationship between two vertices, the set of which is usually written as $E$.

For an undirected graph a specific edge in $E$
is usually written as $\\{v, w\\} \in E$  where $v$ and $w$ are vertices in $E$. Sometimes this is written as $v \leftrightarrow w$.

For a directed graph a specific edge in $E$
is usually written as $(v,w)$ where $v$ and $w$ are vertices in $E$, and the direction of the edge is from $v$ to $w$. Sometimes this is written as $v \rightarrow w$.

**Undirected Graph**: A graph in which the relationship between vertices is bidirectional, written as $G = (V, E)$.

**Directed Graph**: A graph in which the relationship between vertices is unidirectional, written as $\overrightarrow{G} = (V, E)$

**Fully Connected Graph**: Every vertex is connected to every other vertex.

**Walk**: Traversing a graph, visiting vertices any number of times.

**Path**: A path from from $v$ to $w$ without visiting a vertex multiple times.

**Cycle**: A path through a graph that begins and ends at the same vertex.

**Degree Of A Vertex**: The number of edges a vertex has.

$n$: In the context of graph algorithms, $n$ usually refers to the number of vertices of a graph. Example: $n = |V|$

$m$: In the context of graph algorithms, $m$ usually refers to the number of edges of a graph. Example: $m = |E|$


## Some Common Graphs We See Everyday

**The World Wide Web**: Each page (or site, depending on your analysis) is a vertex, and each link is a directed edge.

**Social Networks**: Each user is a vertex, each “follow” is a directed edge, and each friendship is an undirected edge.

**Road Networks**: Each address is a vertex, each road is an undirected edge, and each one-way street is a directed edge.

**Computer Networks**: Each network attached device is a vertex, and each connection between devices is (usually) a bidirectional edge.

**Work Planning/Orchestration**: The precedence/dependency order of work in a project forms a graph.


## Continued Reading and References

[Algorithms Illuminated (Part 2): Graph Algorithms and Data Structures](https://www.amazon.com/Algorithms-Illuminated-Part-Graph-Structures/dp/0999282921)

[Graduate Algorithms Notes](https://teapowered.dev/assets/ga-notes.pdf)
