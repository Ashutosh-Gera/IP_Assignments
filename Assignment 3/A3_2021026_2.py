class LaundryService:
    def __init__(self,name,contact,email,Clothtype,branded,season):
        self.name=name    #a string 
        self.contact=contact   #a numeric
        self.email=email       #alphanumeric string
        self.Clothtype=Clothtype #string
        self.branded=branded     #boolean
        self.season=season       #string
        self.id=Customer_id


    def customerDetails(self):
        print ('Customer Id:',self.id,'Customer Name:',self.name, 'Customer contact:',self.contact,'Customer email:',self.email,'Type of cloth:',self.Clothtype, 'Is the Cloth Branded?:',self.branded, sep='\n', end='\n')


    def calculateCharge(self):
        Charge=0
        if self.Clothtype=='Cotton':
            Charge+=50
        elif self.Clothtype=='Silk':
            Charge+=30
        elif self.Clothtype=='Woolen':
            Charge+=90
        elif self.Clothtype=='Polyester':
            Charge+=20
        if self.branded==True:
            Charge*=1.5
        if self.season=='Winter':
            Charge*=0.5
        elif self.season=='Summer':
            Charge*=2
        return Charge


    def finalDetails(self):
        self.customerDetails()
        Charge=self.calculateCharge()
        print ('Total Charge(in INR):',Charge)
        if Charge>200:
            print ('To be returned in 4 days!')
        else:
            print ('To be returned in 7 days!')                                    



n=int(input('Enter the number of customers you want to define:'))
Customer_id=1


for i in range(n):
    a=input('Name of Customer:')
    b=int(input('Contact No.:'))
    c=input('Email:')
    d=input('Type of Cloth(Cotton/Silk/Woolen/Polyester):')
    e=bool(int(input('Branded?(0/1):')))
    f=input('Season(Summer/Winter):')
    cust=LaundryService(a,b,c,d,e,f)
    Customer_id+=1
    print ('\n')
    print ('The customer Specific details are:',end='\n\n')
    cust.finalDetails()





        