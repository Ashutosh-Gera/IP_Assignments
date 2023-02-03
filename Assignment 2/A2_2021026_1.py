while True:
    print (''' Enter your choice:
    1. Display specific Word Count
    2. Display all Unique Words
    3. Display all Word Counts
    4. Replace word
    5. quit ''')
    a=int(input())
    f= open('Assignment 2\question1_input.txt', 'r')
    l=f.read().split()
    if a==1:
        s=input('Enter the word:')
        count=0
        for i in l:
            if i==s:
                count+=1
        if count>=1:
            print ('The count of the given word is:',count)
        else:
            print ('Word does not exist')            
    elif a==2:
        s=set(l)
        print ('Unique words:')
        for i in s:
            print (i, end='  ;  ')
        print ( 'Number of unique words is:',len(s))
    elif a==3:
        dict={}
        s=set(l)
        for i in s:
            dict[i]=l.count(i)
        print ('Word counts:')    
        for i in dict.keys():
            print (i, end=' : ')
            print (dict[i])
    elif a==4:
        w1=input('Enter the word to be replaced:')
        if w1 not in l:
            print ('The word is not in the file')
            pass
        else:
            w2=input('Enter word that will replace:')
            while w1 in l:
                k=l.index(w1)
                l[k]=w2
            new=' '.join(l)
            f=open('Assignment 2\question1_input.txt','w') 
            f.write(new)
            f.close()
            print ('program replaced successfully!')
    elif a==5:
        f.close()
        break        
    
        


        
