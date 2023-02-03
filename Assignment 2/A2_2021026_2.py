from math import cos, sin

n=int(input('Enter the number of vertices the 3D shape has:'))
lx=[eval(i) for i in input('Enter the x-axis vertice coordinates:').split()]
ly=[eval(i) for i in input('Enter the y-axis vertice coordinates:').split()]
lz=[eval(i) for i in input('Enter the z-axis vertice coordinates:').split()]

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


q=int(input('Number of queries:'))
queries=[]
for i in range(q):
    q1=input('Enter queries:').split()
    queries.append(q1)
#so now queries is a matrix consisting of all the queries
# to be performed
f=open('Assignment 2\ques2.txt','w')
f.write('Input vertices:' + '\n')
s1=''
for i in lx:
    s1= s1 + str(i) +' '
s2=''
for i in ly:
    s2= s2 + str(i) +' '
s3=''
for i in lz:
    s3= s3 + str(i) +' '
f.write('x:' + s1 + '\n' + 'y:' + s2 + '\n' + 'z:' + s3 + '\n')            
for i in queries:
    #i=[S SX SY SZ] OR [T TX TY TZ] OR [R X PHI]
    if i[0]=='S':
        sx,sy,sz=eval(i[1]),eval(i[2]),eval(i[3])
        for j in range(len(lx)):
            lx[j] *= sx
        for j in range(len(ly)):
            ly[j] *= sy
        for j in range(len(lz)):
            lz[j] *= sz         
    
    
    elif i[0]=='T':
        tx,ty,tz=eval(i[1]),eval(i[2]),eval(i[3])
        for j in range(len(lx)):
            lx[j] += tx
        for j in range(len(ly)):
            ly[j] += ty
        for j in range(len(lz)):
            lz[j] += tz  
    
    
    elif i[0]=='R':
        axis,phi=i[1],float(i[2])
        if axis=='x':
            for k in range(len(ly)):
                j=int(ly[k])
                b=lz[k]
                ly[k]=(a*float(cos(phi))) - (b*float(sin(phi)))
                lz[k]=(a*float(sin(phi))) + (b*float(cos(phi)))
        if axis=='y':
            for k in range(len(lz)):
                j=int(lz[k])
                a=int(j)
                b=lx[k]
                lz[k]=(a*float(cos(phi))) - (b*float(sin(phi)))
                lx[k]=(a*float(sin(phi))) + (b*float(cos(phi)))        
        if axis=='z':
            for k in range(len(lx)):
                j=int(lx[k])
                a=int(j)
                b=ly[k]
                lx[k]=(a*float(cos(phi))) - (b*float(sin(phi)))
                ly[k]=(a*float(sin(phi))) + (b*float(cos(phi)))          
print (lx)
print (ly)
print (lz)
f.write('Output:' + '\n')
s4=''
for i in lx:
    s4= s4 + str(i) +' '
s5=''
for i in ly:
    s5= s5 + str(i) +' '
s6=''
for i in lz:
    s6= s6 + str(i) +' '
f.write('x:' + s4 + '\n' + 'y:' + s5 + '\n' + 'z:' + s6 + '\n')
f.close() 