from turtle import color
from arcade import Color
from pyamaze import maze,agent,COLOR,textLabel

def dijkstra(m,*h,start=None): #*h means that we can have more than one h
    if start is None:
        start=(m.rows,m.cols) #if there is no start point given then it will start at (6,6)

    hurdles=[(i.position,i.cost) for i in h]

    unvisited={n:float('inf') for n in m.grid} #it loops in each point in the maze and gives it coast of infinity
    unvisited[start]=0 #it gives the starting point coast of zero
    visited={}
    revPath={}
    while unvisited: #while the maze is not finished
        currCell=min(unvisited,key=unvisited.get) #it searches for the minimum value of a point (this is responsible for taking the path with lower coast)
        visited[currCell]=unvisited[currCell] #it markes this point as visited
        if currCell==m._goal:
            break #it breaks out of the loop when the currCell reaches the goal point
        for d in 'EWNS': 
            if m.maze_map[currCell][d]==True: #if the wall is open in any direction
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in visited:
                    continue
                tempDist= unvisited[currCell]+1
                for hurdle in hurdles:
                    if hurdle[0]==currCell: #if the current cell have hurdle
                        tempDist+=hurdle[1] #add the cost of the hurdle to the cost of the cell 

                if tempDist < unvisited[childCell]:#if the caculated cost is better than the previous cost
                    unvisited[childCell]=tempDist #update the cost to the better one
                    revPath[childCell]=currCell
        unvisited.pop(currCell) #remove the current cell from the unvisited

    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[revPath[cell]]=cell
        cell=revPath[cell]

    return fwdPath,visited[m._goal]




if __name__=='__main__':
    myMaze=maze(6,6)
    myMaze.CreateMaze(1,4,loopPercent=100)
   


    h1=agent(myMaze,4,4,'square',color=COLOR.pink)
    h2=agent(myMaze,4,6,'square',color=COLOR.pink)
    h3=agent(myMaze,4,2,'square',color=COLOR.pink)
    # h4=agent(myMaze,4,1,'square',color=COLOR.pink)
    # h5=agent(myMaze,4,3,'square',color=COLOR.pink)
    # h6=agent(myMaze,4,6,'square',color=COLOR.pink)

    h1.cost=50
    h2.cost=50
    h3.cost=50
    # h4.cost=50
    # h5.cost=50
    # h6.cost=50

    path,c=dijkstra(myMaze,h1,h2,h3,start=(6,1))
    textLabel(myMaze,'Total Cost',c)


    a=agent(myMaze,6,1,color=COLOR.purple,filled=True,footprints=True) #before running the code please make sure to add these lines 'pink=("mediumvioletred","mediumvioletred"), purple=("mediumorchid3","mediumorchid3"), turquois=("mediumturquoise","mediumturquoise")' in the pymaze library colors class
    myMaze.tracePath({a:path})


    myMaze.run()
