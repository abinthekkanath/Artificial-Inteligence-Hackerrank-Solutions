def indexof(e,arr):
    for i in range(len(arr)):
        if e in arr[i]:
            return [i,arr[i].index(e)]
def position(x,y):
    

    if x<0:
        xvalue='UP\n'
    elif x>0:
        xvalue='DOWN\n'
    elif x==0:
        xvalue=''

    if y<0:
        yvalue='LEFT\n'
    elif y>0:
        yvalue='RIGHT\n'
    elif y==0:
        yvalue=''    


    return ''+abs(x)*xvalue+abs(y)*yvalue

        
def displayPathtoPrincess(n,grid):
#print all the moves here

    x=indexof("p",grid)[0]-indexof("m",grid)[0]
    y=indexof("p",grid)[1]-indexof("m",grid)[1]
    print(position(x,y))

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)