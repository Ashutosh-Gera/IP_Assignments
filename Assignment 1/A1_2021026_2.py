'''Values printed will be only till 2 decimal places''' 
def Square():
        s=float(input('Enter length of side'))
        print('Perimeter :',round(4*s,2))
        print('Area :',round(s*s,2))
def Rectangle():
        l=float(input('Enter length'))
        b=float(input('Enter breadth'))
        print('Perimeter :',round(l+l+b+b,2))
        print('Area :',round(l*b,2))
def Rhombus():
        s=float(input('Enter side length'))
        d1=float(input('Enter diagnol 1 length'))
        d2=float(input('Enter diagnol 2 length'))
        print('Perimeter :',round(4*s,2))
        print('Area :',round(d1*d2/2,2))
def Parallelogram():
        l=float(input('Enter length'))
        b=float(input('Enter breadth'))
        h=float(input('Enter height'))
        print('Perimeter :',round(l+l+b+b,2))
        print('Area :',round(b*h,2))
def Circle():
        r=float(input('Enter radius'))
        print('Perimeter :',round(2*3.14*r,2))
        print('Area :',round(3.14*r*r,2))
def Cube():
        l=float(input('Enter side length'))
        print('CSA :',round(4*l*l,2))
        print('TSA :',round(6*l*l,2))
        print('Volume :',round(l*l*l,2))
def Cuboid():
        l=float(input('Enter length'))
        b=float(input('Enter breadth'))
        h=float(input('Enter height'))
        print('CSA :',round(2*(b+l)*h,2))
        print('TSA :',round(2*(l*b+b*h+l*h),2))
        print('Volume :',round(l*b*h,2))
def Right_Circular_Cone():
        l=float(input('Enter slant height'))
        r=float(input('Enter radius'))
        h=float(input('Enter height'))
        print('CSA :',round(3.14*r*l,2))
        print('TSA :',round(3.14*r*(l+r),2))
        print('Volume :',round(3.14*r*r*h/3,2))
def Hemisphere():
        r=float(input('Enter radius'))
        print('CSA :',round(2*3.14*r*r,2))
        print('TSA :',round(3*4.14*r*r,2))
        print('Volume :',round(2*3.14*r*r*r/3,2))
def Sphere():
        r=float(input('Enter radius'))
        print('CSA :',round(4*3.14*r*r,2))
        print('TSA :',round(4*3.14*r*r,2))
        print('Volume :',round(4*3.14*r*r*r/3,2))
def Solid_Cylinder():
        r=float(input('Enter radius'))
        h=float(input('Enter height'))
        print('CSA :',round(2*3.14*r*h,2))
        print('TSA :',round(2*3.14*r*h+2*3.14*r*r,2))
        print('Volume :',round(3.14*r*r*h,2))
def Hollow_Cylinder():
        r1=float(input('Enter inner radius'))
        r2=float(input('Enter outer radius'))
        h=float(input('Enter height'))
        print('CSA :',round(2*3.14*h*(r1+r2),2))
        print('TSA :',round(2*3.14*h*(r1+r2)+2*3.14*(r2*r2-r1*r1),2))
        print('Volume :',round(3.14*h*(r2*r2-r1*r1),2))
d={1:'Square',2:'Rectangle',3:'Rhombus',4:'Parallelogram',5:'Circle',6:'Cube',7:'Cuboid',8:'Right_Circular_Cone',9:'Hemisphere',10:'Sphere',11:'Solid_Cylinder',12:'Hollow_Cylinder',13:'Exit'}
n=int(input('Enter number of students:'))
twod=['Square','Rectangle','Rhombus','Parallelogram','Circle']
threed=['Cube','Cuboid','Right Circular Cone','Hemisphere','Sphere','Solid Cylinder','Hollow Cylinder']
for i in range(n):
     print('-'*13+'MENU'+'-'*13)
     choose=input('2D or 3D:')
     if choose=='2D':
        for i in range(1,6):
                print(i,'.',twod[i-1])
     elif choose=='3D':
        for i in range(6,13):
                print(i,'.',threed[i-6])
     print('-'*30)
     opt=int(input('Choose option:'))
     eval(d[opt])()
