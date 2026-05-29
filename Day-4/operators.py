Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
b=10
a+b
20
a-b
0
a*b
100
a/b
1.0
9/2
4.5
a//b
1
9//2
4
a**2
100
6**3
216
a%b
0
17%2
1
17
17



























17%4
1
a
10
b
10
a<b
False
a>b
False
10<=b
True
a==b
True
a!=b
False
10>=b
True
y=5
y
5
y=y+5
y
10
y=y+10
y
20
y+=10
y
30
y-=10
y
20
y*=20
y
400
y/=2
y
200.0
y//3
66.0
y
200.0
y%-10
-0.0
y**-2
2.5e-05
2.5e-05
2.5e-05
y//=3
y
66.0
y%=6
y
0.0
y%-+4
-0.0
y**-=13
SyntaxError: invalid syntax
a
10
b
10
a%10==0
True
a%20==0 and b%20==0 and a>b
False
a%20==0 or b%20==0 or a>b
False
a%20==0 0r b%20==0 0r a<b
SyntaxError: invalid decimal literal
a%20==0 or b520==0 or a<b
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a%20==0 or b520==0 or a<b
NameError: name 'b520' is not defined
a%20==0 or b%20 or a<b
10
a%22==0 or b%20==0 or a<b
False
not a>b
True
a%20==0 or b%20==0 or a<b
False
False
False
#str,list,tuple,set,dict
a='python programming'
a
'python programming'
'python programming'
'python programming'
'y' in a
True
'g' in a
True
'z' not in a
True
'r' not in a
False
l=['java','python','mysql', 'c++','c','html']
'mysql' in 1
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    'mysql' in 1
TypeError: argument of type 'int' is not a container or iterable
'mysql' in
SyntaxError: invalid syntax
'java' in l
True
'mysql in l
SyntaxError: unterminated string literal (detected at line 1)
SyntaxError: unterminated string literal (detected at line 1)
SyntaxError: invalid syntax
'mysql' in l
True
'python' in 1
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    'python' in 1
TypeError: argument of type 'int' is not a container or iterable
 'c++' in l
 
SyntaxError: unexpected indent
'c' not in l
False
t=['laptop', 'moblie','mouse','keyword')
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
t=['laptop', 'moblie', 'mouse', 'keyword']
t
['laptop', 'moblie', 'mouse', 'keyword']
'laptop' in t
True
'charger' in t
False
d=[ 'oil':150,'water' :120, 'suger':90]
SyntaxError: invalid syntax
'oil' in d
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    'oil' in d
NameError: name 'd' is not defined. Did you mean: 'id'?
d=['water':80,'rice':89]
SyntaxError: invalid syntax

n=[1,2,3,4,5]
n
[1, 2, 3, 4, 5]
n==m
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    n==m
NameError: name 'm' is not defined
l is m
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    l is m
NameError: name 'm' is not defined
l=[1,2,3,4,5]
m=[1,2,3,4,6,7]
l==m
False
n=m
n
[1, 2, 3, 4, 6, 7]
n==m
True
l is m
False
n is m
True
id(l)
2468125478784
id9m)
SyntaxError: unmatched ')'
id(m)
2468125479552
id(n)
2468125479552
l is not m
True
>>> n is not 1
True
>>> 1-0001
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> 8&14
8
>>> 8&7
0
>>> 8/7
1.1428571428571428
>>> 10^11
1
>>> ~14
-15
>>> 8..2
SyntaxError: invalid syntax
>>> 8>>2
2
>>> 15>>2
3
>>> 16<<1
32
>>> a=12
>>> b=12.34
>>> c='python'
>>> print(a,b,c)
12 12.34 python
>>> print("a=",a,'b=',b,'c=',c,sep='')
a=12b=12.34c=python
>>> a=12b=12.34c=python
SyntaxError: invalid decimal literal
>>> print("a=",a,'b=',b,'c=',c,sep=,end='@@@@')
SyntaxError: expected argument value expression
>>> print("a=",a,'b,'c=',c,sep='',end='@@@@')
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> a=12b=12.34c=python@@@
...       
SyntaxError: invalid decimal literal
>>> print(f'a= {a} b={b} c={c}')
...       
a= 12 b=12.34 c=python
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
...       
a=12 b=12.34 c=python
