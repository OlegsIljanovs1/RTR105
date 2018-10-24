user@epk428-11:~$ ~/RTR105
bash: /home/user/RTR105: Is a directory
user@epk428-11:~$ dgr_20181024.py
dgr_20181024.py: command not found
user@epk428-11:~$ cd ~/RTR105
user@epk428-11:~/RTR105$ dgr_20181024.py
dgr_20181024.py: command not found
user@epk428-11:~/RTR105$ nano dgr_20181024.txt
user@epk428-11:~/RTR105$ ls -lt
total 32
-rw-rw-r-- 1 user user 3115 Oct 24 09:14 dgr_20181024.py
-rw-rw-r-- 1 user user  179 Oct 24 08:51 history_20181024
-rw-rw-r-- 1 user user 3100 Oct 24 08:30 dgr_20180919.py
-rwxrwxr-x 1 user user  173 Oct 24 08:30 git-upload
-rw-rw-r-- 1 user user  678 Oct 24 08:30 history_20180905.txt
-rw-rw-r-- 1 user user 1800 Oct 24 08:30 history_20180912
-rw-rw-r-- 1 user user  741 Oct 24 08:30 history_20180919.txt
-rw-rw-r-- 1 user user  977 Oct 24 08:30 README.md
user@epk428-11:~/RTR105$ ./git-upload 20181024
[master b2cd4d7] 20181024
 1 file changed, 159 insertions(+)
 create mode 100644 dgr_20181024.py
Username for 'https://github.com': cd dgr_20181024.py
Password for 'https://cd dgr_20181024.py@github.com': 
]remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/OlegsIljanovs1/RTR105/'
user@epk428-11:~/RTR105$ git  clone https://github.com/OlegsIljanovs1/RTR105
Cloning into 'RTR105'...
remote: Enumerating objects: 87, done.
remote: Counting objects: 100% (87/87), done.
remote: Compressing objects: 100% (84/84), done.
remote: Total 87 (delta 28), reused 9 (delta 2), pack-reused 0
Unpacking objects: 100% (87/87), done.
Checking connectivity... done.
user@epk428-11:~/RTR105$ ./git-upload dgr_20181024.py
[master e8ff6fb] dgr_20181024.py
 1 file changed, 1 insertion(+)
 create mode 160000 RTR105
Username for 'https://github.com': exit()
Password for 'https://exit()@github.com': 
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/OlegsIljanovs1/RTR105/'
user@epk428-11:~/RTR105$ 
user@epk428-11:~/RTR105$ nano dgr_20181024.txt
user@epk428-11:~/RTR105$ python
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> fruit = 'banana'
>>> "n" in fruit
True
>>> "m" in fruit
False
>>> "nan" in fruit
True
>>> if "a" in fruit: print("Found it!")
... "a" in fruit
  File "<stdin>", line 2
    "a" in fruit
      ^
SyntaxError: invalid syntax
>>> if word == 'banana': print('All right,bananas.')
... if word < 'banana': print( Your word,'+word+' comes before banana.)
  File "<stdin>", line 2
    if word < 'banana': print( Your word,'+word+' comes before banana.)
     ^
SyntaxError: invalid syntax
>>> elif word >'banana':
  File "<stdin>", line 1
    elif word >'banana':
       ^
SyntaxError: invalid syntax
>>> greet = 'Hello Bob'
>>> zap = greet.lower()
>>> print (zap)
hello bob
>>> print(greet)
Hello Bob
>>> print ('Hi There.lower())
  File "<stdin>", line 1
    print ('Hi There.lower())
                            ^
SyntaxError: EOL while scanning string literal
>>> print ('Hi There'·lower())
  File "<stdin>", line 1
    print ('Hi There'·lower())
                          ^
SyntaxError: invalid character in identifier
>>> print('Hi There'·lower())
  File "<stdin>", line 1
    print('Hi There'·lower())
                         ^
SyntaxError: invalid character in identifier
>>> stuff ='Hello world'
>>> type(stuff)
<class 'str'>
>>> dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 

