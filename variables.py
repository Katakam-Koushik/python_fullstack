Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=9
print(a)
9
x=90
print(X)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
9a=10
SyntaxError: invalid decimal literal
a=20
a,b,c=10,200,3000
print(a,b,c)
10 200 3000
a=b=c=100
print(a,b,c)
100 100 100
name="koushik"
print("name")
name
print(name)
koushik
fname=koushik
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    fname=koushik
NameError: name 'koushik' is not defined
fname="koushik"
print(name" "fm=name
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(name" "fname)
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
@=0
      
SyntaxError: invalid syntax
_40=28
      
print(_40)
      
28
print(name," ",fname)
      
koushik   koushik
if = 50
      
SyntaxError: invalid syntax
else = 20
SyntaxError: invalid syntax
a =10 ; b= 19
print(a+b)
29
del a
print(a)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
a=10,10,20,300,50000
print(a)
(10, 10, 20, 300, 50000)
a=10
type(a)
<class 'int'>
a=9.5
type(a)
<class 'float'>
a="codegnan"
type(a)
<class 'str'>
a='''codegnan'''
type(a)
<class 'str'>
a=4 + 5j
type(a)
<class 'complex'>
a=9j
type(a)
<class 'complex'>
a=8j+1
type(a)
<class 'complex'>
a=true
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
a=True
type(a)
<class 'bool'>
int(a)
1
int(7.8)
7
int(8j+1)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    int(8j+1)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int("hi")
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
float(1)
1.0
float(2.3)
2.3
float("hi")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    float("hi")
ValueError: could not convert string to float: 'hi'
float(5j+1)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    float(5j+1)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
str("hi")
'hi'
str(1)
'1'
str(2.4)
'2.4'
str(True)
'True'
str(hi)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    str(hi)
NameError: name 'hi' is not defined
>>> bool(2)
True
>>> bool(0)
False
>>> bool(3j+1)
True
>>> bool(2j)
True
>>> bool(0)
False
>>> complex(2j)
2j
>>> complex(1)
(1+0j)
>>> complex("str")
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    complex("str")
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(False)
0j
