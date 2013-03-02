# Exercises for chapter 3: Problems 3.1, 3.2, 3.3, and 3.4 in Think Python

Mark Levi

ex3.1
NameError: name 'repeat_lyrics' is not defined

ex3.2
Because you do not call the function repeat_lyrics() until after you define it, it does not cause any errors. The program runs smoothly. 

ex3.3
def right_justify(x):
    rj = 70 - len(x)
    print ' ' * rj + x

right_justify('allen')

ex3.4
1) 

def do_twice(f):
	(f)
	(f)

def print_spam():
	print 'spam'

do_twice(print_spam)
spam
spam

2) 

def do_twice(f, x):
    f(x)
    f(x)

3) 

def print_twice(x):
    print x
    print x

4) 

do_twice(print_twice, 'spam')

spam
spam
spam
spam


5) 

def do_four(f, x):
    do_twice(f, x)
    do_twice(f, x)

do_four(print_twice, 'spam')

spam
spam
spam
spam
spam
spam
spam
spam
