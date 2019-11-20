from extractors import extract_city, extract_neighbors

graph = {}
with open('./cities.txt','r') as file:
    for line in file:
        node1 = extract_city(line)
        node2 = extract_neighbors(line)
        graph.setdefault(node1, node2)

print(graph)        


    
