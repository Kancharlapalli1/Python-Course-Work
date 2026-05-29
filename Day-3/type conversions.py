Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
a
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set)(a)
SyntaxError: unmatched ')'
set(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
b=75.2
int(b)
75
75
75
complex(b)
(75.2+0j)
(75.2+0j)
(75.2+0j)
str(b)
'75.2'
complex(b)
(75.2+0j)
str(b)
'75.2'
list(b)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
bool(b)
True
c=75+2j
int(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(75+2j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
list(c)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
b00l(c)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    b00l(c)
NameError: name 'b00l' is not defined
bool(c)
True
s="maha"
s='1234'
s='13.45'
int9a)
SyntaxError: unmatched ')'
int(s)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: '13.45'
s="maha"
a='1234'
b='13.45'int(a)
SyntaxError: invalid syntax
s="maha"
a='1234'
b='13.45'
int(a)
1234
float(b)
13.45
list(s)
['m', 'a', 'h', 'a']
list(a)
['1', '2', '3', '4']
list(b)
['1', '3', '.', '4', '5']
tuple(s)
('m', 'a', 'h', 'a')
tuple(a)
('1', '2', '3', '4')
tuple(b)
('1', '3', '.', '4', '5')
set(s)
{'a', 'h', 'm'}
set(b)
{'3', '4', '1', '5', '.'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
bool(a)
True
bool(b)
True
l=[1,2,3,4]
l
[1, 2, 3, 4]
int(l)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
tuple(l)
(1, 2, 3, 4)
set(l)
{1, 2, 3, 4}
bool(l)
True
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
str(t)
'(1, 2, 3, 4, 5)'
list(t)
[1, 2, 3, 4, 5]
tuple(t)
(1, 2, 3, 4, 5)
bool(t)
True
s={1,2,3}
str
<class 'str'>
str(s)
'{1, 2, 3}'
list(s)
[1, 2, 3]
tuple(s)
(1, 2, 3)
bool(s)
True
b=
SyntaxError: invalid syntax
b=true
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    b=true
NameError: name 'true' is not defined. Did you mean: 'True'?
bool9s)
SyntaxError: unmatched ')'
bool(s)
True
b=true
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    b=true
NameError: name 'true' is not defined. Did you mean: 'True'?
int(b)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: '13.45'
float(b)
13.45
complex(b)
(13.45+0j)
str(b)
'13.45'
d={'name':'maha','age':'21'}
d
{'name': 'maha', 'age': '21'}
>>> str(d)
"{'name': 'maha', 'age': '21'}"
>>> list(d)
['name', 'age']
>>> tuple(d)
('name', 'age')
>>> set(d)
{'age', 'name'}
>>> bool(d)
True
>>> int(l)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> complex(l)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
>>> tuple(l)
(1, 2, 3, 4)
>>> set(l)
{1, 2, 3, 4}
>>> bool(l)
True
>>> t=(1,2,3,4,5)
>>> t
(1, 2, 3, 4, 5)
>>> str(t)
'(1, 2, 3, 4, 5)'
>>> list(t)
[1, 2, 3, 4, 5]
>>> tuple(t)
(1, 2, 3, 4, 5)
>>> bool(t)
True
>>> s
{1, 2, 3}
>>> ={1,2,3}
SyntaxError: invalid syntax
>>> str(s)
'{1, 2, 3}'
>>> list(s)
[1, 2, 3]
