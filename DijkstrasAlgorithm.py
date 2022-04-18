# Chapter 2
class Node:
    def __init__(self, name, distance, path, neighbors) -> None:
        self.name = name
        self.distance = distance
        self.path = path
        self.neighbors = neighbors

class Edge:
    def __init__(self, node1, node2, weight) -> None:
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def __repr__(self) -> str:
        return str(self.weight)


# Initializing Nodes
nodeA = Node("A", 0, Node("A", 0, 0, []), [])
nodeB = Node("B", 10000, None, [])
nodeC = Node("C", 10000, None, [])
nodeD = Node("D", 10000, None, [])
nodeE = Node("E", 10000, None, [])
nodeF = Node("F", 10000, None, [])
allNodes = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF]

# Initializing edges
edgeAB = Edge(nodeA, nodeB, 3)
edgeAC = Edge(nodeA, nodeC, 1)

edgeBD = Edge(nodeB, nodeD, 3)
edgeBF = Edge(nodeB, nodeF, 6)

edgeCD = Edge(nodeC, nodeD, 4)
edgeCE = Edge(nodeC, nodeE, 2)

edgeDF = Edge(nodeD, nodeF, 1)

edgeEF = Edge(nodeE, nodeF, 5)

nodeA.neighbors = [edgeAB, edgeAC]
nodeB.neighbors = [edgeBD, edgeBF]
nodeC.neighbors = [edgeCD, edgeCE]
nodeD.neighbors = [edgeDF]
nodeE.neighbors = [edgeEF]

class DijkstrasAlgorithm:
    """Dijkstra's Algorithm. Used to show the shortest distance between to nodes on a linked graph"""
    def findPaths(start: Node):
        start.distance = 0
        
        for node in allNodes: # Go through each node in the list
            minDis = sorted(node.neighbors, key=lambda x: x.weight, reverse=False) # sort its neighbors by weights of edges

            for neighbors in minDis: # go through each node in neighbors
                # Check each neighbor and if it's distance is greater than what we would get through the current node then update the distance and path
                if neighbors.node2.distance > (node.distance + neighbors.weight):
                    neighbors.node2.distance = node.distance + neighbors.weight
                    neighbors.node2.path = neighbors.node1

    def shortestPath(start: Node, end: Node):
        currentNode = end
       
        returnVal = ["", 0]

        # construct path
        while currentNode != start:
            returnVal[0] += (currentNode.name)
            currentNode = currentNode.path 
       
        returnVal[0] += start.name
        returnVal[1] = end.distance # add distance
        returnVal[0] = returnVal[0][::-1] # reverse string order
        print(returnVal)

DijkstrasAlgorithm.findPaths(nodeA)
DijkstrasAlgorithm.shortestPath(nodeA, nodeF)