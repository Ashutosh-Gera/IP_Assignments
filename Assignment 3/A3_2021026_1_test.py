from A3_2021026_1 import matmul,scale
from A3_2021026_1 import translate,rotate

def test_matmul(A,B,true_C):
    C=matmul(A,B)
    try:
        assert len(C)==len(true_C)
    except AssertionError:
        return False

    for i in range(len(true_C)):
        try:
            assert true_C[i]==C[i]
        except AssertionError:
            return False
    return True

def test_scale(x,y,z,sx,sy,sz,true_x,true_y,true_z):
    x_bar,y_bar,z_bar=scale(x,y,z,sx,sy,sz)
    try:
        assert x_bar==true_x
        assert y_bar==true_y
        assert z_bar==true_z
        return True
    except AssertionError:
        return False

def test_translate(x,y,z,tx,ty,tz,true_x,true_y,true_z):
    x_bar,y_bar,z_bar=translate(x,y,z,tx,ty,tz)
    try:
        assert x_bar==true_x
        assert y_bar==true_y
        assert z_bar==true_z
        return True
    except AssertionError:
        return False

def test_rotate(x,y,z,axis,phi,true_x,true_y,true_z):
    x_bar,y_bar,z_bar=rotate(x,y,z,axis,phi)
    try:
        assert x_bar==true_x
        assert y_bar==true_y
        assert z_bar==true_z
        return True
    except AssertionError:
        return False

#testcase for function matmul
#print (test_matmul([[1,2],[3,4]],[[1,2],[3,4]],[[7,10],[15,22]]))
#print (test_matmul([[1,2,3],[8,9,10]],[[1,2],[3,4],[5,6]],[[22,28],[85,112]]))










a=input('Enter the function you would like to test(matmul/scale/translate/rotate):')
if a=='matmul':
    A=eval(input('Enter matrix A:'))
    B=eval(input('Enter matrix B:'))
    true_C=eval(input('Enter their product:'))
    print (test_matmul(A,B,true_C))

elif a=='scale':
    x,y,z=[eval(i) for i in input('Enter the coordinates to be scaled as space separated values:').split()]
    sx,sy,sz=[eval(i) for i in input('Enter the scaling parameters(sx,sy,sz) as space separated values:').split()]
    true_x,true_y,true_z=[eval(i) for i in input('Enter the coordinates after scaling as space separated values:').split()]
    print (test_scale(x,y,z,sx,sy,sz,true_x,true_y,true_z))

elif a=='translate':
    x,y,z=[eval(i) for i in input('Enter the coordinates to be translated as space separated values:').split()]
    tx,ty,tz=[eval(i) for i in input('Enter the translating parameters(tx,ty,tz) as space separated values:').split()]
    true_x,true_y,true_z=[eval(i) for i in input('Enter the coordinates after translating as space separated values:').split()]
    print (test_translate(x,y,z,tx,ty,tz,true_x,true_y,true_z))

elif a=='rotate':
    x,y,z=[eval(i) for i in input('Enter the coordinates to be rotated as space separated values:').split()]
    axis,phi=[eval(i) for i in input('Enter the axis and value of phi:').split()]
    true_x,true_y,true_z=[eval(i) for i in input('Enter the coordinates after rotating as space separated values:').split()]
    print (test_rotate(x,y,z,axis,phi,true_x,true_y,true_z))
else:
    raise ValueError('Enter valid input')        


    

    


