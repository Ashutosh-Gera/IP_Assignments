class Student:
    
    def __init__(self,name,cgpa,branch):
        self.name=name #string
        self.cgpa=cgpa #float
        self.branch=branch #string(CSE,CSAM,ECE)
        self.isPlaced=False


    def isEligible(self,Company_obj):
        if (self.cgpa>=Company_obj.reqd_cgpa) and (self.branch in Company_obj.branches) and not(self.isPlaced):
            print ('Student {} is eligible for Company {}'.format(self.name, Company_obj.name))
            self.apply(Company_obj)
        else:
            print ('Student {} is not eligible for Company {}'.format(self.name, Company_obj.name))


    def apply(self,Company_obj):
        Company_obj.appliedStudents.append(self)
    

    def getsPlaced(self):
        self.isPlaced=True
    
    def getcgpa(self):
        return self.cgpa

class Company:
    
    
    def __init__(self,name,reqd_cgpa,branches,positionOpen):
        self.name=name #string
        self.reqd_cgpa=reqd_cgpa #float
        self.branches=branches #list of branches from which company would hire
        self.positionOpen=positionOpen #Maxm number of students company will hire
        self.appliedStudents=[]
        self.applicationOpen=True

    def closeApplication(self):
        self.applicationOpen=False
        def sort_students(elem):
            #l=list of objects of class Student
            return elem.getcgpa()
        
        self.appliedStudents.sort(key=sort_students, reverse=True)
        k=len(self.appliedStudents[:self.positionOpen])

        print ('The company has hired {} students'.format(k))
    
    def hireStudents(self):
        
        def sort_students(elem):
            #l=list of objects of class Student
            return elem.getcgpa()
        
        self.appliedStudents.sort(key=sort_students, reverse=True)
        print ('\nThe Company {} has hired the following students : '.format(self.name))
        k=len(self.appliedStudents[:self.positionOpen])
        for i in self.appliedStudents[:self.positionOpen]:
            i.isPlaced=True
            print (i.name)
        self.closeApplication()


n=int(input('Enter the number of students:'))
students=[]
for i in range(n):
    a=input('Enter the name of the student {} :'.format(i+1))
    try:
        b=float(input('Enter the cgpa of student {} : '.format(i+1)))
        assert 0<=b<=10
    except AssertionError:
        print ('The cgpa is invalid!!')
        exit()
    c=input('Enter the branch of student {} : '.format(i+1))
    students.append(Student(a,b,c))
#students = list of object(s) Student

x=int(input('Enter the number of companies:'))
for i in range(x):
    p=input('Enter the name of Company {}:'.format(i+1))
    q=float(input('Enter the reqd cgpa of Company {}:'.format(i+1)))
    r=[i for i in input('Enter space separated branches of Company {} :'.format(i+1)).split()]
    s=int(input('Enter the number of positions open of Company {}:'.format(i+1)))
    obj=Company(p,q,r,s)
    for j in students:
        j.isEligible(obj)
    obj.hireStudents()

            






