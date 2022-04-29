from collections import defaultdict
from collections import deque

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    front = deque([start_node])

  
    while len(front) != 0:
      intersection = front.popleft()
      ##pops left as the intersection
      for neighbor in graph[intersection]:
        if neighbor not in result:
          ##if it is a result then add it and then append it from neighbor
          result.add(neighbor)
          front.append(neighbor)
    return result

def test_reachable():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']
    assert sorted(reachable(graph, 'E')) == ['E', 'F', 'G']




def connected(graph):
  points = len(graph)
  ## first count the number of points by taking the length of the graph
  firstPoint = next(iter(graph))
  ## then using the iter function you can make it so you can interate through the set one at a time
  inRangeFirst = reachable(graph, firstPoint)
  ## then check if this point is able to reach the first point
  
  if(points == len(inRangeFirst)):
    return True
  return False

def test_connected():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert connected(graph) == True
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert connected(graph) == False



def n_components(graph):
  workingParts = set()
  ##work through the list of items in graph
  for i, j in graph.items():
    ##checking the parts to see if it fits all criteria
    part = reachable(graph, i)
    part = tuple(sorted(part))

    ##if it passed then add it to the list of working parts
    workingParts.add(part)
  return len(workingParts)
  
def test_n_components():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert n_components(graph) == 1

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert n_components(graph) == 2

if __name__ == "__main__":
  test_reachable()
  test_connected()
  test_n_components()