import networkx as nx
import doctest as doctest
import math


def vcg_cheapest_path(graph, source, target):
    """
   calculate the price for each edge in the graph for the chips path from  source to target
   according to vcg algorithm
    :param graph: a networkx graph object(weighted).
    :param source -the start node
    :param target - the start target

   >>> G = nx.Graph()
   >>> G.add_edge('a', 'b', weight=3)
   >>> G.add_edge('b', 'd', weight=4)
   >>> G.add_edge('c', 'd', weight=1)
   >>> G.add_edge('d', 'a', weight=10)
   >>> G.add_edge('a', 'c', weight=5)
   >>> G.add_edge('b', 'c', weight=1)
   >>> vcg_cheapest_path(G,'a','d')
   [('a', 'b', {'weight': 3}), ('a', 'd', {'weight': 10}), ('a', 'c', {'weight': 5}), ('b', 'd', {'weight': 4}), ('b', 'c', {'weight': 1}), ('d', 'c', {'weight': 1})]
   [4, 0, 0, 0, 2, 3]



   # the original path and length
   length , path = nx.single_source_dijkstra(graph, source, target)
   eg = graph.edges()
   ans=[0]*len(eg)
   i = 0
   for (u, v, d) in graph.edges(data=True):
      print(d.get('weight'))
      print((u, v, d))
      graph.remove_edge(u,v)
      temp_length, temp_path = nx.single_source_dijkstra(graph, source, target)
      # if the original path goes through this edge
      if not(temp_path == path):
      # calculate his price
         pass
         #ans [i] = d.get('weight') + temp_length - length
      graph.add_edge(u, v, weight = d.get('weight'))
      print("the i: {}".format(i))
      i+= 1
   #print(eg)
   #print(ans)



   # the original path and length
   length , path = nx.single_source_dijkstra(graph, source, target)
   eg = graph.edges()
   ans=[0]*len(eg)
   i = 0
   for (u, v, d) in graph.edges(data=True):
      g = nx.Graph()
      # build the same graph without the edge (x, y, z)
      for (x, y, z) in graph.edges(data=True):
         if((x, y, z) == (u, v, d)):
            g.add_edge(u, v, weight = math.inf)
         else:
            g.add_edge(x, y, weight = z.get('weight'))
      # find the new path without (x, y, z)
      temp_length, temp_path = nx.single_source_dijkstra(g, source, target)
      # if the original path goes through this edge
      if not(temp_path == path):
      # calculate his price
         ans [i] = d.get('weight') + temp_length - length
      i+= 1
   print(eg)
   print(ans)
   """
    # the original path and length
    length, path = nx.single_source_dijkstra(graph, source, target)
    eg = graph.edges(data=True)
    ans = [0] * len(eg)
    i = 0
    for (u, v, d) in eg:
        graph.remove_edge(u, v)
        temp_length, temp_path = nx.single_source_dijkstra(graph, source, target)
        graph.add_edge(u, v, weight=d.get('weight'))
        # if the original path goes through this edge
        if not (temp_path == path):
        # calculate his price
            ans [i] = d.get('weight') + temp_length - length
        i += 1
        if(i >= len(eg)):
           break
    print(eg)
    print(ans)


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
