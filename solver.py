user_maze = [
  ["S","0","0","0","1"],
  ["1","1","0","0","1"],
  ["0","0","0","0","1"],
  ["1","0","1","0","E"],
  ["1","1","1","0","E"]
]

def find_start_end(maze):
  for row in range(len(maze)):
    for col in range(len(maze[0])):
      if maze[row][col] == "S":
        start = (row, col)
      if maze[row][col] == "E":
        end = (row, col)
  print("Start: ",start)
  print("End: ",end)

find_start_end(user_maze)
