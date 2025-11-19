while True:
  edges = list(map(int, input().split(' ')));
  max_edge = max(edges);
  remain_edges = edges.copy();
  remain_edges.remove(max_edge);

  if (edges[0] == 0):
    break;

  if (max_edge < sum(remain_edges)):
    if (len(set(edges)) == 1):
      print('Equilateral');
    elif (len(set(edges)) == 2):
      print('Isosceles ');
    else:
      print('Scalene');
  else:
    print('Invalid');

