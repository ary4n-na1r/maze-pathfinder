The maze is defined with the following:
- 0: Empty (can be moved through)
- 1: Wall (cannot be moved through)
- S: Start (An empty square where the maze begins)
- E: End (an empty square where the maze ends)
  - Both S and E are along the outer edges of the maze
- Movement is up, down, left and right
- Size of the maze defined by the user (5 to 10)
- An optimal path is a path that uses the least amount of moves.

An example of a 5x5 maze (with optimal path marked by O):
  1SOO0
  111O1
  100OO
  1011E
  10000

Each cell is represented by its coordinates, and it is stored as a 2D list.

Breadth First Search (BFS) Plan: (February)
1. Add start node to queue
2. Mark start as visited
3. While queue is not empty:
   - Remove front node
   - If node is end, stop
   - Otherwise add all valid unvisited neighbours
4. Use parent dictionary to reconstruct path
