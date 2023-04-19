from sys import stdin

def spiralPrint(mat, nRows, mCols):
    #Your code goes here
    if len(mat)==0: #Empty Matrix
        return

    top=0
    bottom=len(mat)
    left=0
    right=len(mat[0])

    while left<right and top<bottom:
        #Top
        for i in range(left,right):
            print(mat[top][i], end=' ')
        top += 1

        #right

        for i in range(top,bottom):
            print(mat[i][right-1],end=' ')
        right -=1

        if not(left<right and top<bottom):
            break

        #bottom

        for i in range(right-1,left-1,-1):
            print(mat[bottom-1][i],end=' ')
        bottom -=1

        #left

        for i in range(bottom-1,top-1,-1):
            print(mat[i][left],end=' ')
        left +=1





























#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1