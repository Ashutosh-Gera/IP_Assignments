#d=decimal
#b=binary
#h=hexadecimal
#o=octal
#We will be defining to general functions r2d(radix to decimal)
# & d2r ( decimal to radix) & then implementing them according to requirements.
def r2d(number,radix):
    p=list(number)[::-1]
    dict={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35}
    for j in p:
        if j in dict.keys() and dict[j]<radix:
            k=p.index(j)
            p[k]=dict[j]     
        else:
            print("")
            return
    l=[]
    for i in p:
        k=p.index(i)
        a=(i*(radix**k))
        l.append(a)    
    d=sum(l)
    return d

def d2r(number,radix):
    st=''
    dict={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J',20:'K',21:'L',22:'M',23:'N',24:'O',25:'P',26:'Q',27:'R',28:'S',29:'T',30:'U',31:'V',32:'W',33:'X',34:'Y',35:'Z'}
    while int(number)>0:
        remainder=int(number)%radix
        if remainder>=10:
            a=dict[remainder]
        else:
            a=str(remainder)    
        st+=(a)
        number=int(number)//radix
    final=st[::-1]
    return final

 
while True:
    print ('''Choose a function among the following:
    1. Convert decimal to binary
    2. Convert binary to decimal
    3. Convert decimal to hexadecimal
    4. Convert hexadecimal to decimal
    5. Convert decimal to octal
    6. Convert octal to decimal
    7. Convert binary to hexadecimal
    8. Convert hexadecimal to binary
    9. Convert binary to octal
    10. Convert octal to binary
    11. Convert hexadecimal to octal
    12. Convert octal to hexadecimal
    13. Convert  radix A to radix B
    14. exit ''')
    a=int(input())
    b=str(input('Enter the number to be converted:'))
    if a==1:
        print (d2r(b,2))
    elif a==2:
        print (r2d(b,2))
    elif a==3:
        print (d2r(b,16))
    elif a==4:
        print (r2d(b,16))
    elif a==5:
        print (d2r(b,8))
    elif a==6:
        print (r2d(b,8))
    elif a==7:
        m=r2d(b,2)
        n=d2r(m,16)
        print (n)                
    elif a==8:
        m=r2d(b,16)
        n=d2r(m,2)
        print (n)
    elif a==9:
        m=r2d(b,2)
        n=d2r(m,8)
        print (n)
    elif a==10:
        m=r2d(b,8)
        n=d2r(m,2)
        print (n)
    elif a==11:
        m=r2d(b,16)
        n=d2r(m,8)
        print (n)
    elif a==12:
        m=r2d(b,8)
        n=d2r(m,16)
    elif a==13:
        x=int(input('Enter radix A:'))
        m=r2d(b,x)
        y=int(input('Enter radix B:'))
        n=d2r(m,y)
        print (n)
    elif a==14:
        break                        

