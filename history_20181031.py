Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> fhand = open("teksts.txt", "r")

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    fhand = open("teksts.txt", "r")
IOError: [Errno 21] Is a directory: 'teksts.txt'
>>> handle = open("tekst.txt")

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    handle = open("tekst.txt")
IOError: [Errno 2] No such file or directory: 'tekst.txt'
>>> fhand = open("teksts.txt")

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    fhand = open("teksts.txt")
IOError: [Errno 21] Is a directory: 'teksts.txt'
>>> fhand = open(teksts)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    fhand = open(teksts)
NameError: name 'teksts' is not defined
>>> print(fhand)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(fhand)
NameError: name 'fhand' is not defined
>>> open(teksts.txt)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    open(teksts.txt)
NameError: name 'teksts' is not defined
>>> open(Music)

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    open(Music)
NameError: name 'Music' is not defined
>>> handle = open("teksts.txt")

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    handle = open("teksts.txt")
IOError: [Errno 21] Is a directory: 'teksts.txt'
>>>  >
