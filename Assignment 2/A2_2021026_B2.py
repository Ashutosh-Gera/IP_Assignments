#both win a grammy every year
# for scyscraper of height h, fan reputation 
# earned = h*(no. of grammy's holding at that time)
#can buy 1 skyscraper per year
#both decide to buy skyscrapers in alternate years
#doja dog going first
#P= initial grammys of dog
#Q=initial grammys of snack
#M=height of city
#N=number of skyscrapers
#column of 1s=skyscraper
P,Q=[int(i) for i in input().split()]
M,N=[int(i) for i in input().split()]
s=''
l=[]
for i in range(M):
    st=input()
    l.append(st)
    s=s+st+'\n'
#print (s)
#print (l)
h1=[] #vertical list
for j in range(N):
    s0=''
    for i in l:
        s0+=i[j]
    h1.append(s0)
#print (h1)
#each string in h1 represents a skyscraper
def skyscraperheight(s):
    count=0
    s[::-1]
    for i in s:
        if i=='1':
            count+=1
    return count  
h2=h1.copy() #copy of h1 , will represent height of skyscrapers          
for i in range(len(h2)):
    a=h2[i]
    b=skyscraperheight(a)
    h2[i]=b
#print (h2)
h3=h2.copy()    
h2.sort(reverse=True)
#calculating total reputation of dog
Dog=0
for i in range(0,len(h2),2):
    Dog+=P*h2[i]
    P+=2
print (Dog,end=' ') 
#calculating total reputation of snack
Snack=0
Q+=1
for i in range(1,len(h2),2):
    Snack+=Q*h2[i]
    Q+=2   
print (Snack,end='\n')

for i in h2:
    for j in h1:
        if h2.index(i)%2==0:
            if j.count('1')==i:
                k=h1.index(j)
                j1=j.replace('1','D')
                h1[k]=j1
            else:
                pass
        else:
            if j.count('1')==i:
                k=h1.index(j)
                j1=j.replace('1','S')
                h1[k]=j1
            else:
                pass
#print (h1)
final=[]
for j in range(M):
    horizontal=''
    for i in h1:
        horizontal+=i[j]
    final.append(horizontal)
#print (final)    
for i in final:
    print (i, end='\n')
    






      
