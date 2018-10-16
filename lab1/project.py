data=[['A','B','C',0]]
path=['the steps:']
Monkey='A'
Banana='B'
Box='C'
On=0
i=1
def move(n):
    global Monkey,i
    path.append('step %d:from %s move to %s'%(i,Monkey,n))
    Monkey=n
    data.append([Monkey,Banana,Box,On])
    i=i+1
def up():
    global On,i
    path.append('step %d:Climb the box at point %s'%(i,Box))
    On=1
    data.append([Monkey,Banana,Box,On])
    i = i + 1
def push(n):
    global Monkey,Box,i
    path.append('step %d:push the box from %s to %s'%(i,Box,n))
    Monkey=n
    Box=n
    data.append([Monkey,Banana,Box,On])
    i = i + 1
def get():
    path.append('step %d:get this banana'%(i))
def step():
    if Monkey==Banana:
        if Box==Banana:
            up()
            get()
        else:
            move(Box)
            step()
    else:
        if Box==Monkey:
            push(Banana)
            step()
        else:
            move(Box)
            step()
step()
for S in path:
    print S
print 'the status:'
print '[Monkey,Banana,Box,On the box]'
for X in data:
    print X





