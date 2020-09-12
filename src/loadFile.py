import xml.etree.ElementTree as ET


def loadFile():
    tree = ET.parse('brazil58.xml')
    return tree


root = loadFile().getroot()

graph = []
i = 1


for vertex in root:
    city = "city: "+str(i)
    costs = []
    for edge in vertex:
        costs.append(float(edge.attrib["cost"]))
    graph.append({"city": city, "costs": costs})
    i += 1

# print(graph)

for vertex in graph:
    print(vertex['city'])
