from math import sin,cos


def matmul(A,B):
    #function giving the product of matrices A and B(A*B). matrix=list of lists
    row_A=len(A)
    col_A=len(A[1])
    row_B=len(B)
    col_B=len(B[1])
    
    if col_A != row_B:
        raise ValueError('Product not defined for such matrices')
    prod_matrix=[]
    
    for i in range(row_A):
        l=[]
        for j in range(col_B):
            p=A[i] #ith row
            q=[]    #jth column
            for k in range(row_B):
                q.append(B[k][j])
            s=0
            for x in range(len(p)):
                    s+=p[x]*q[x]
            l.append(s)
        
        prod_matrix.append(l)

    return prod_matrix


def scale(x,y,z,sx,sy,sz):
    a = matmul([[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]], [[x],[y],[z],[1]])
    output=[]
    for i in range(3):
        output.append(a[i][0])
    return output


def translate(x,y,z,tx,ty,tz):
    a = matmul([[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]],[[x],[y],[z],[1]])
    output=[]
    for i in range(3):
        output.append(a[i][0])
    return output


def rotate(x,y,z,axis,phi):
    
    if axis=='z':
        a=matmul([[cos(phi),-sin(phi),0,0],[sin(phi),cos(phi),0,0],[0,0,1,0],[0,0,0,1]],[[x],[y],[z],[1]] )
    elif axis=='y':
        a=matmul([[cos(phi),0,sin(phi),0],[0,1,0,0],[-sin(phi),0,cos(phi),0],[0,0,0,1]],[[x],[y],[z],[1]])
    elif axis=='x': 
        a=matmul([[1,0,0,0],[0,cos(phi),-sin(phi),0],[0,sin(phi),cos(phi),0],[0,0,0,1]],[[x],[y],[z],[1]])       
    
    output=[]
    for i in range(3):
        output.append(a[i][0])
    return output









        



            


    
