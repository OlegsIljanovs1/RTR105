>>> import sys
>>> sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
>>> from numpy import *
>>> x = linspace ( 0, 4, 70)
>>> y = cos(x)
>>> from matplotlib import pyplot as plt
>>> plt.grid(0)
>>> plt.grid()
>>> plt.xlabel('x'°
  File "<stdin>", line 1
    plt.xlabel('x'°
                  ^
SyntaxError: invalid character in identifier
>>> plt.xlabel('x')
Text(0.5,0,'x')
>>> plt.ylabel('f(x)')
Text(0,0.5,'f(x)')
>>> plt.title('Funkcija$cos(x)$'°
  File "<stdin>", line 1
    plt.title('Funkcija$cos(x)$'°
                                ^
SyntaxError: invalid character in identifier
>>> plt.title('Funkcija$cos(x)$')
Text(0.5,1,'Funkcija$cos(x)$')
>>> plt.plot(x, y)
[<matplotlib.lines.Line2D object at 0x7f906bf88e48>]
>>> plt.show()
>>> 
>>> import sys
>>> sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
>>> 
>>> from numpy import *
>>> x = linspace( 0, 4, 11)
>>> y = sin(x)
>>> y1 = x
>>> #y2 = x - x*x*x/(2*3*4)
... y2 = y1 - x**4/(2*3*4)
>>> #y3 = x - x*x*x/(2*3*4) + x*x*x*x*x(2*3*4*5*6)
... 
>>> y2 = y1 - x**4/(2*3*4)
>>> y4 = y3 - x**7/(1*2*3*4*5*6*7)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y3' is not defined
>>> y3 = y2 + x**6(2*3*4*5*6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
>>> 



>>> import sys
>>> sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages'°
  File "<stdin>", line 1
    sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages'°
                                                                      ^
SyntaxError: invalid character in identifier
>>> sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
>>> from numpy import *
>>> x = linspace ( 0, 4 , 11)
>>> y = sin(x)
>>> y1 = x
>>> y2 = x - x*x*x/(1*2*3)
  File "<stdin>", line 1
    y2 = x - x*x*x/(1*2*3)
      ^
SyntaxError: invalid syntax
>>> #y2 = x - x*x*x/(1*2*3)
... 
>>> y2 = y1 - x**3/(1*2*3)
>>> #y3 = x - x*x*x/(1*2*3) + x*x*x*x*x/(1*2*3*4*5)
... 
>>> y3 = y2 + x**5/(1*2*3*4*5)
>>> #y4 = x - x*x*x/(1*2*3) + x*x*x*x*x/(1*2*3*4*5) - x*x*x*x*x*x*x/(1*2*3*4*5*6*7)
... 
>>> y4 = y3 - x**7/(1*2*3*4*5*6*7)
>>> 
>>> from matplotlib import pyplot as plt
>>> plt.grid()
>>> plt.xlabel('x')
Text(0.5,0,'x')
>>> plt.ylabel('f(x)')
Text(0,0.5,'f(x)')
>>> plt.title('Funkcija $sin(x)$')
Text(0.5,1,'Funkcija $sin(x)$')
>>> plt.plot(x, y color = "#FFFF00")
  File "<stdin>", line 1
    plt.plot(x, y color = "#FFFF00")
                      ^
SyntaxError: invalid syntax
>>> plt.plot(x, y, color = "#FFFF00")
[<matplotlib.lines.Line2D object at 0x7f906a900470>]
>>> plt.plot( x, y1, color = "#0000FF")
[<matplotlib.lines.Line2D object at 0x7f906a900668>]
>>> plt.plot(x , y2, color = "#FF00FF")
[<matplotlib.lines.Line2D object at 0x7f906a900be0>]
>>> plt.plot (x, y3, color = "#00FF00")
[<matplotlib.lines.Line2D object at 0x7f906a9080b8>]
>>> plt.plot( x, y4, color = "#FF0000")
[<matplotlib.lines.Line2D object at 0x7f906a908550>]
