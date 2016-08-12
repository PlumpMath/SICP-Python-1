def product(n,terms):
    return terms(n) 

def terms(n):
	if n==0:
		return 1
	else:
		return n*terms(n-1)
# print product(3,terms)

	
def double(f):
	def b(x):
		return 2*f(x)
	return b

def f(x):
	return x	

###

from operator import mul, pow
def square(x):
	return mul(x,x)

def repeated(f,n):
	def h(x):
		if n == 1:
			return f(x)
		else:
			return f(repeated(f,n-1)(x))
	return h

       


###

def zero(f):
	return lambda x: x

def successor(n):
	return lambda f: lambda x: f(n(f)(x))


def one(f):
	return lambda x: f(x)

def two(f):
	return lambda x : f(f(x))

def add_church(m, n):
    return lambda f: lambda x: m(f)(n(f)(x))
def church_init(n):
	return n(lambda x : x)(0)


    