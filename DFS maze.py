from pyamaze import maze,agent,COLOR
def DFS(m):
    #set the start to last node in maze
    start=(10,10)

    #push the start in the two stacks
    explored=[start]
    frontlist=[start]
    dfsPath={}

     #while front list have elements
    while len(frontlist)>0:
        #pop it in current
        current=frontlist.pop()

        #break if current equals to goal
        if current==(1,1):
            break

            #search in all directions of map
        for d in 'ESNW':
           if m.maze_map[current][d]==True:
                if d=='E':
                    childCell=(current[0],current[1]+1)
                elif d=='S':
                    childCell=(current[0]+1,current[1])
                elif d=='N':
                    childCell=(current[0]-1,current[1])
                elif d=='W':
                    childCell=(current[0],current[1]-1)

#if there is a path continue
                if childCell in explored:
                    continue
                    #append this path to both stacks
                explored.append(childCell)
                frontlist.append(childCell)

                #dfs dics has the child as key and current as value
                #this will return all tried paths
                dfsPath[childCell]=current

         #fwdpath dics will store the path right ahead from start to end
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return fwdPath


if __name__=='__main__':
    m=maze(10,10)
    m.CreateMaze(loopPercent=50,theme="light")
    path=DFS(m)
    a=agent(m,10,10,footprints=True,color=COLOR.pink)
    m.tracePath({a:path})


    m.run()
