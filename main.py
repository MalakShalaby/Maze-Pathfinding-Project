
from pymaze import maze, agent, COLOR, textLabel

def BFS(m):
    start = (m.rows, m.cols)
    possible_cells = [start]
    visited_cells = [start]

    bfsPath = {}
    bSearch = []

    while len(possible_cells) > 0:
        current_Cell = possible_cells.pop(0)
        if current_Cell == (1, 1):
            break
        for d in 'ESNW':
            if m.maze_map[current_Cell][d]:
                if d == 'E':
                    NEXT_Cell = (current_Cell[0], current_Cell[1] + 1)
                elif d == 'W':
                    NEXT_Cell = (current_Cell[0], current_Cell[1] - 1)
                elif d == 'N':
                    NEXT_Cell = (current_Cell[0] - 1, current_Cell[1])
                elif d == 'S':
                    childCell = (current_Cell[0] + 1, current_Cell[1])

                if NEXT_Cell in visited_cells:
                    continue
                possible_cells.append(NEXT_Cell)
                visited_cells.append(NEXT_Cell)
                bfsPath[NEXT_Cell] = current_Cell
                bSearch.append(NEXT_Cell)
    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]
    return bSearch, bfsPath, fwdPath


if _name_ == '_main_':
    m = maze(7, 5)
    m.CreateMaze(loopPercent=50, theme='light')

    bSearch, bfsPath, fwdPath = BFS(m)

    # agent class in pymaze that start from the last cell by default and try to reach goal
    # footprints is to keep tracking the path
    a = agent(m, footprints=True, color=COLOR.pink, shape='square', filled=True)
    b = agent(m, footprints=True, color=COLOR.purple, shape='arrow', filled=False)
    c = agent(m, 1, 1, footprints=True, color=COLOR.turquois, shape='square', filled=True, goal=(m.rows, m.cols))

    l = textLabel(m, 'Length of Shortest Path', len(fwdPath) + 1)

    # first path trace how agent search in all directions "ESNW" until reach the goal or the possible cells is null
    m.tracePath({a: bSearch}, delay=100)

    # second path trace from the goal till reach the start cell to get the bfs bath
    m.tracePath({c: bfsPath}, delay=100)

    # third path reverse bfspath just to get back to goal with shortest length
    m.tracePath({b: fwdPath}, delay=100)

    m.run()