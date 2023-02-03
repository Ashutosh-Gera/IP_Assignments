def noteCreate():
    notes=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C`','C#`','D`','D#`','E`','F`','F#`','G`','G#`','A`','A#`','B`','C']
    
    def majorscale(rootnote):
        k=notes.index(rootnote)
        l=[notes[k],notes[k+2],notes[k+4],notes[k+5],notes[k+7],notes[k+9],notes[k+11],notes[k+12]]
        return ' '.join(l)
    
    def minorscale(rootnote):
        k=notes.index(rootnote)
        l=[notes[k],notes[k+2],notes[k+3],notes[k+5],notes[k+7],notes[k+8],notes[k+10],notes[k+12]]
        return ' '.join(l)       
    f1=open('Assignment 2\scaleMajor.txt','w')
    s1=''
    for i in notes[0:13]:
        s1=s1 + i + ' ' + majorscale(i) + '\n'
    f1.write(s1)
    f1.close()
    f2=open('Assignment 2\scaleMinor.txt','w')
    s2=''
    for i in notes[0:13]:
        s2=s2 + i + ' ' + minorscale(i) + '\n'
    f2.write(s2)
    f2.close()

def majorNotes(root):
    f=open('Assignment 2\scaleMajor.txt')
    a=f.readlines()
    for i in a:
        i.strip()
    for i in a:
        if i[0]==root:
            return i[2:]    

def minorNotes(root):
    f=open('Assignment 2\scaleMinor.txt')
    a=f.readlines()
    for i in a:
        i.strip()
    for i in a:
        if i[0]==root:
            return i[2:]
x=input('Enter the root note:')
y=input('Enter the type of scale(Major/Minor):')
noteCreate()
if y=='Major':
    print ('The major scale in the key of {} is:'.format(x),majorNotes(x))
elif y=='Minor':
    print ('The minor scale in the key of {} is:'.format(x),minorNotes(x))                             