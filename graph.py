# Create the dictionary with graph elements

graph = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
print(graph)
print("---------------------------")

# Display graph vertices

class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict=[]
        self.gdict=gdict

# Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())
    
graph_elements = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g=graph(graph_elements)
print(g.getVertices())