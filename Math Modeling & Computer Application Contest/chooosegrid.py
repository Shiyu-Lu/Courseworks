import math



def choosegrid_stationary(er,Lastsize_ii):
    grid = []
    if abs(er/Lastsize_ii)==0:
        return [0]
    elif 0<abs(er/Lastsize_ii) <=10:
        grid = [-10,0,10]
    elif 10< abs(er/Lastsize_ii) <=20:
        grid = [-20,-10,0,10,20]
    elif 20< abs(er/Lastsize_ii) <=30:
        grid = [-30,-20,-10,0,10,20,30]
    elif 40< abs(er/Lastsize_ii) <=30:
        grid = [-40,-20,-10,0,10,20,40]
    else:
        grid = []
    return grid

def choosegrid_increasing(tovprice_ii,Lastprice_ii):
    gridnum = int(abs(tovprice_ii/10))
    if gridnum==0:
        gridnum=1
    #flag2 = abs(tovprice_ii+1)/(tovprice_ii+1) #防止除以0
    grid,grid2 = [],[]
    prim = 1

    if gridnum<10:
        pass
    elif 20>abs(gridnum)>=10:
        gridnum = int(math.floor(gridnum/2))
        prim = 2
    elif 40>abs(gridnum)>=20:
        gridnum = int(math.floor(gridnum/4))
        prim = 4
    elif 80>abs(gridnum)>=40:
        gridnum = int(math.floor(gridnum/8))
        prim = 8
    else:
        #print ("too much change")
        return [[],[]]
    grid.append(0)
    grid2.append(Lastprice_ii)
    
    for n in range(1,gridnum+1):
        grid.append(grid[n-1]-10*prim)
        grid2.append(grid[n-1]-10*prim)
    if len(grid)>2:
        if grid[gridnum] != tovprice_ii:
            grid[gridnum] = -tovprice_ii
            grid2[gridnum] = Lastprice_ii-tovprice_ii

    return [grid,grid2]


def choosegrid_decreasing(tovprice_ii,Lastprice_ii):
    gridnum = int(abs(tovprice_ii/10))
    if gridnum==0:
        gridnum=1
    #flag2 = abs(tovprice_ii+1)/(tovprice_ii+1) #防止除以0
    grid,grid2 = [],[]
    prim = 1

    if gridnum<10:
        pass
    elif 20>abs(gridnum)>=10:
        gridnum = int(math.floor(gridnum/2))
        prim = 2
    elif 40>abs(gridnum)>=20:
        gridnum = int(math.floor(gridnum/4))
        prim = 4
    elif 80>abs(gridnum)>=40:
        gridnum = int(math.floor(gridnum/8))
        prim = 8
    else:
        print ("too much change")
        return [[],[]]
    grid.append(0)
    grid2.append(Lastprice_ii)
    
    for n in range(1,gridnum+1):
        grid.append(grid[n-1]+10*prim)
        grid2.append(grid[n-1]+10*prim)
    if len(grid)>2:
        if grid[gridnum] != tovprice_ii:
            grid[gridnum] = -tovprice_ii
            grid2[gridnum] = Lastprice_ii-tovprice_ii

    return [grid,grid2]