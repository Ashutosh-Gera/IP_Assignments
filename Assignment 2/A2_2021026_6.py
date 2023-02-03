N=int(input('Enter size of the 2d square matrix:'))
matrix=[]
for i in range(N):
    l=[int(i) for i in input(('Enter the elements of row {} of matrix:').format(i+1)).split()]
    if len(l)==N:
        matrix.append(l)
    else:
        print ('Enter correct amount of elements based on N') 
        break   
#print (matrix)

def nt(matrix):#nt=normal traversal
    for i in matrix:
        for j in i:
            print (j, end=' ')
#nt(matrix)            

def at(matrix):#at=alternate traversal
    for i in matrix:
        k=matrix.index(i)
        if k%2==0:
            pass
        else:
            i1=i[::-1]
            matrix[k]=i1
    nt(matrix)
#at(matrix)


def bt(matrix):#bt=boundary traversal
    l=[]
    for i in matrix[0]:
        l.append(i)   
    for i in matrix[1:N-1]:
        l.append(i[-1])
    for i in matrix[-1][::-1]:
        l.append(i)
    for i in matrix[N-2:0:-1]:
        l.append(i[0])        
    print (*l)


def st(matrix):#spiraltraversal
    while len(matrix) != 0:
        for j in range(len(matrix[0])):
            print(matrix[0][j], end=" ")
        del matrix[0]
        if len(matrix) == 0:
            return

        
        for i in range(len(matrix)):
            print(matrix[i][-1], end=" ")
            del matrix[i][-1]
        if len(matrix) == 0:
            return


        for j in range(len(matrix[0])-1, -1, -1):
            print(matrix[-1][j], end=" ")
        del matrix[-1]
        if len(matrix) == 0:
            return


        for i in range(len(matrix)-1, -1, -1):
            print(matrix[i][0], end=" ")
            del matrix[i][0]


def dt1(matrix):
    #diagonal traversal from right to left
    n=len(matrix)
    l=[]
    for i in range(n):
        for j in range(i+1):
            l.append(matrix[j][i])
            i-=1
    
    #for i in range(1,n):
        #for j in range(i,0,-1):
            #l.append(matrix[i][-j])
            #i+=1

    for i in range(n-1,0,-1):
        for j in range(1,i+1):
            l.append(matrix[-i][-j])
            i-=1             
    print (*l)        


def dt2(matrix):
    #diagonal traversal from left to right
    l=matrix.copy()
    for j in range(len(l)):
        a=l[j]
        l[j]=a[::-1]
    dt1(l)    

                        
while True:
   print ("""
1) Normal traversal (from left to right for each row)
2) Alternating traversal ( first left to right for the first row, then right to left for the second row,
then left to right for the third row, and so on.)
3) Spiral traversal from outer to inwards
4) Boundary traversal.(First, traverse the upper boundary from left to right, then right
boundary from up to down, then bottom boundary from right to left and at last from left
boundary from down to up)
5) Diagonal traversal from right to left
6) Diagonal traversal from left to right.
7) Quit
""")
   a=int(input('select option:'))
   if a==1:
       nt(matrix)
   elif a==2:
       at(matrix)
   elif a==3:
       st(matrix)       
   elif a==4:
       bt(matrix)  
   elif a==5:
       dt1(matrix)
   elif a==6:
       dt2(matrix)
   elif a==7:
       break       