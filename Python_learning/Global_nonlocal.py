#____________global______________
x = ""

def myfunc():
  global x
  x = 300
  def myinnerfunc():
    global x
    print(x, 'line 7')
    x = 100
  myinnerfunc()

myfunc()
print(x, 'line 9')

#____________nonlocal_____________

def fonc():
    y = 100
    print(y)
    def fonc2():
        nonlocal y
        y = 200
        print(y)
    fonc2()
fonc()
