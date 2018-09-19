Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> __builtins__.doc__

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    __builtins__.doc__
AttributeError: 'module' object has no attribute 'doc__'
>>> __builtincs__.__doc__

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    __builtincs__.__doc__
NameError: name '__builtincs__' is not defined
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> print(__builtins__.__doc__)
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
>>> abs(10)
10
>>> abs(-10)
10
>>> a = abs(-10)
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 10, '__package__': None}
>>> a
10
>>> a
10
>>> a = 20
>>> a
20
>>> a * b

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a * b
NameError: name 'b' is not defined
>>> a =10
>>> a = 10
>>> a.__doc__
"int(x=0) -> int or long\nint(x, base=10) -> int or long\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is floating point, the conversion truncates towards zero.\nIf x is outside the integer range, the function returns a long instead.\n\nIf x is not a number or if base is given, then x must be a string or\nUnicode object representing an integer literal in the given base.  The\nliteral can be preceded by '+' or '-' and be surrounded by whitespace.\nThe base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to\ninterpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 10, '__package__': None}
>>> type(a)
<type 'int'>
>>> b = 1.5
>>> print b.__doc__
float(x) -> floating point number

Convert a string or number to a floating point number, if possible.
>>> vars()
{'a': 10, 'b': 1.5, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type (b)
<type 'float'>
>>> c = D

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    c = D
NameError: name 'D' is not defined
>>> C = "D"
>>> vars()
{'a': 10, 'C': 'D', 'b': 1.5, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> print c.__doc__

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print c.__doc__
NameError: name 'c' is not defined
>>> print C.__doc__
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
>>> type(C)
<type 'str'>
>>> 
