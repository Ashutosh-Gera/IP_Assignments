class Person:


    def __init__(self,firstname,lastname,age):
        self.firstname=firstname #string
        self.lastname=lastname #string
        self.age=age #int


    def object_info(self):
        print (self.firstname,self.lastname,self.age, sep = ' ')    


def sort_attribute(l,st):
    
    def attribute(elem):
        
        if st=='firstname':
            return elem.firstname
        elif st=='lastname':
            return elem.lastname
        elif st=='age':
            return elem.age

    l.sort(key=attribute)
    return 
    
    

menu='''Welcome to the Application! \n\n'''
while True:
    print (menu)
    n=int(input('Specify the number of people to be enrolled:'))
    print ('\n\n')
    persons=[]

    for i in range(n):
        a=input('Enter the firstname for person {} :'.format(i+1))
        b=input('Enter the lastname for person {} :'.format(i+1))
        c=int(input('Enter Age for Person {} :'.format(i+1)))
        obj=Person(a,b,c)
        print ('\n\n')
        persons.append(obj)

    #persons=list of objects of class Person
    k=int(input('Specify the number of Queries:'))
    for i in range(k):
        output=[]
        query=input('Enter Query {} (firstname/lastname/age):'.format(i+1))
        sort_attribute(persons,query)
        print ('Required Order:',end='\n')
        for j in persons:
            output.append(j.object_info())
        filtered_output=list(filter(None,output))
        print (*filtered_output, sep='\n')    

    x=input('Thanks for using the application UwU, if you wish to restart, press "Y" else press "N" to exit:') 
    if x=='Y':
        pass
    elif x=='N':
        break
    else:
        raise ValueError('Enter either "Y" or "N". Dumbass!!')

    







