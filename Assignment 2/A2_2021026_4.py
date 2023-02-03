akey=open('Assignment 2\AnswerKey.txt')
a=open('Assignment 2\Ash_12.txt')#a=ash
b=open('Assignment 2\Brock_1000.txt')#b=brock
j=open('Assignment 2\John_1357.txt')#j=john
m=open('Assignment 2\Misty_372.txt')#m=misty
r=open('Assignment 2\Ram_1211.txt')#r=ram
def options(l):
    l1=[]
    for i in range(len(l)):
        if i%2==0:
            pass
        else:
            l1.append(l[i])
    return l1
ans=options(akey.read().strip().split())
ash=options(a.read().strip().split())
brock=options(b.read().strip().split())
john=options(j.read().strip().split())
misty=options(m.read().strip().split())
ram=options(r.read().strip().split())
def evaluate(l1,l2):
    #l1=list of student marked options
    #l2=list of answer key's options
    marks=0
    for i in range(len(l1)):
        if l1[i]==l2[i]:
            marks+=4
        else:
            if l1[i]=='-':
                pass
            else:
                marks-=1    
    return marks
ashmarks=evaluate(ash,ans)
brockmarks=evaluate(brock,ans)
johnmarks=evaluate(john,ans)
mistymarks=evaluate(misty,ans)
rammarks=evaluate(ram,ans)
l=[johnmarks, rammarks,brockmarks,mistymarks, ashmarks]
f=open('Assignment 2\RegisteredStudents.txt')
s=f.read().splitlines()
for i in range(len(s)):
    s[i] = s[i]+" "+str(l[i])
final=open('Assignment 2\FinalReport.txt', 'w')
for i in s:
    final.write(i + "\n")