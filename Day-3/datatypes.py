Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
t=69.39
type(t)
<class 'float'>
c=12+5j
type(c)
<class 'complex'>
s="mahalakshmi"
type(s)
<class 'str'>
s='maha'
type(s)
<class 'str'>
s='''maha'''
type(s)
<class 'str'>
l=[1,2,3]
id(l)
2198757914048
l=['post1.png','reel1.mp4']
id(l)
2198756899328
l=['post1.png','reel1.mp4']
l
['post1.png', 'reel1.mp4']
1=[]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l=[]
l=list()
type(t)
<class 'float'>
s={1,2,3,4,6}
type(s)
<class 'set'>
s=set()
s={45678,678,56789,897}
a
10
s
{897, 678, 56789, 45678}
>>> d={'name:'abc','age':100,'course':'PSF'}
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> d={'name':'abc','age':100,'course':'PSF}
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> d
...    
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> d={'name':'abc','age':100,'course':'PSF'}
...    
>>> D
...    
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    D
NameError: name 'D' is not defined. Did you mean: 'd'?
>>> d
...    
{'name': 'abc', 'age': 100, 'course': 'PSF'}
>>> type(d)
...    
<class 'dict'>
>>> status=True
...    
>>> status=Flase
...    
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    status=Flase
NameError: name 'Flase' is not defined. Did you mean: 'False'?
>>> status=True
...    
>>> status=False
...    
>>> type(status)
...    
<class 'bool'>
>>> a=None
...    
>>> type(a)
...    
<class 'NoneType'>
