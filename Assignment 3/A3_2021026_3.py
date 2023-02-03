class BankAccount:
    
    def __init__(self,username,password,current_bal):
        self.username=username
        self.pw=password
        self.cbal=current_bal
        self.f=open('Assignment 3\Q3_txtFiles\{}.txt'.format(self.username),'x')


    def authenticate(self):
        secret_pw=input('Provide your secret password:')
        Attempts=1
        try:
            while not secret_pw==self.pw:
                print ('Wrong password!! Try again! Is there an imposter among us?')
                Attempts+=1
                secret_pw=input('Provide your secret password:')
                if Attempts==3:
                    break
            assert Attempts<=3
            assert secret_pw==self.pw
            return True
        except AssertionError:
            print ('Too many Wrong attempts!! FBI OPEN UP!')
            
               

    def deposit(self,amt):
        if self.authenticate():
            self.cbal+=amt
            self.f=open('Assignment 3\Q3_txtFiles\{}.txt'.format(self.username),'a')
            from datetime import datetime
            self.f.write(str(datetime.now()))
            self.f.write(' The amount of Rupees {} has been added'.format(amt))
            self.f.write(' Current balance --> {}'.format(self.cbal) + '\n')
            self.f.close()


    def withdraw(self,amt):
        if self.authenticate():
            if amt>self.cbal:
                print ('Low balance!! Cannot be debited at this time!')
                return
            else:
                self.cbal-=amt
                self.f=open('Assignment 3\Q3_txtFiles\{}.txt'.format(self.username),'a')
                from datetime import datetime
                self.f.write(str(datetime.now()))
                self.f.write(' The amount of Rupees {} has been debited'.format(amt))
                self.f.write(' Current balance --> {}'.format(self.cbal) + '\n')
                self.f.close()


    def bankStatement(self):
        if self.authenticate():
            self.f=open('Assignment 3\Q3_txtFiles\{}.txt'.format(self.username),'r')
            print ('Hey {}! Your transactions history:'.format(self.username), end='\n\n')
            print (self.f.read())


menu=(''' Select Your option:
1. Deposit
2. Withdraw
3. Bank Statement ''')

print ('WELCOME TO THE BANK OF IIIT-DELHI \n \n')
a=input('Enter your Username:')
b=input('Enter your password:')
c=eval(input('Initial balance for your account:'))
obj=BankAccount(a,b,c)

while True:
    print (menu)
    x=int(input('Enter your choice(1/2/3):'))
    if x==1:
        p=eval(input('Provide the amount to be deposited:'))
        obj.deposit(p)
    elif x==2:
        q=eval(input('Provide the amount to be withdrawn:'))
        obj.withdraw(q)
    elif x==3:
        obj.bankStatement()
    cont=input('Do you wish to Continue?(Y/N):')
    if not(cont=='Y'):
        break


                

        

