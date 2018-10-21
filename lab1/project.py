data=[['A','B','C',0]]
path=['the steps:']
Monkey,Banana,Box,On=data[0]
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
def down():
    global i,On
    path.append('step %d:jump off this box at %s'%(i,Box))
    On=0
    data.append([Monkey, Banana, Box, On])
    i=i+1
def step():
    if Monkey==Banana:
        if Box==Banana:
            up()
            get()
        else:
            move(Box)
            step()
    else:
        if On==1:
            down()
            step()
        elif Box==Monkey:
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





