class grafo(object):
    #didn't make any check, so if u don t use properly 100% broke
    def __init__(self, name):
        self._name = name
        self._nodes = []

    def get_node(self, u):
        for i in self._nodes:
            if i.getName == u.getName:
                return i
    def add_node(self, node):
        self._nodes.append(node)
    
    #lack check and factoring
    def add_edge(self, node1, node2, relation):
        nodecheck1 = self.get_node(node1)
        nodecheck2 = self.get_node(node2)
        nodecheck1.addNodes(nodecheck2, relation)
        nodecheck2.addNodes(nodecheck1, relation)
    def nodes(self):
        return self._nodes[:]
    #lack check
    def getRelation(self, node1, node2):
        relationNode1 = node1.getRelation(node2)
        relationNode2 = node2.getRelation(node2)
        if not relationNode1 is None and not relationNode2 is None:
            return [relationNode1, relationNode2]

    def __str__(self) -> str:
        return ("This is social Network {0} and this is my users \
            \n {1}".format(self._name, [x.name for x in self._nodes]))
        

class Node:
    def __init__(self, name):   
        self.name = name
        self.__otherNodes = []
    def addNodes(self, node, relation):
        if not node in self.__otherNodes:
            self.__otherNodes.append((node, relation))
    def getName(self):
        return self.name
    def __eq__(self, node) -> bool:
        return self.name == node.name
    def __ne__(self, node):
        return not (node == self)
    def __hash__(self):
        return self.name.__hash__()
    def __str__(self) -> str:
        return "I m {0}".format(self._name)
    def getRelation(self, node):
        for i in self.__otherNodes:
            return i

if __name__ == "__main__":
    socialNetwork = grafo("LinWorks")
    Franci = Node("Francesco LoPresti")
    McAyrthonAragon = Node("McAyrthonAragon")
    Lin = Node("BossWorks")
    DavideIelmini = Node("E' già andato")
    Oscar = Node("Forever yaoi")
    Fabio = Node("Fabiuccio")
    socialNetwork.add_node(Franci)
    socialNetwork.add_node(McAyrthonAragon)
    print(socialNetwork)
    print("Now with my social network we connect them")
    socialNetwork.add_edge(Franci, McAyrthonAragon, "Amicizia")
    result = socialNetwork.getRelation(Franci,McAyrthonAragon)
    
    if result != None :
        print("{0} ha un rapporto di {1} con {2}".format(result[0][0].name, result[0][1], result[1][0].name))
        print("{0} ha un rapporto di {1} con {2}".format(result[1][0].name, result[1][1], result[0][0].name))