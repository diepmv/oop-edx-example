#Any procedure or method with yield statement called a GENERATOR

def genTest():
  yield 1
  yield 2

"""
Generators have a next() method (__next__ in python3) which 
starts/resumes execution of the procedure. Inside of generator:
+ yield suspends execution and returns a value
+returning from a generator raises a StopIteration
"""
foo = genTest()
foo.__next__()
#Execution will proceed in body of foo, until reaches first yield 
# statement; then returns value associated with tha statement
#Execution will resume in body of foo at point where stopped, until 
#reaches next yield statement ; then returns value associated with that 
#statement



for n in genTest():
  print(n)
"""
Using generator:
can use generator inside a looping structure as it will continue until 
it gets a StopIteration exception:

"""


def genFib():
  fibn_1 = 1
  fibn_2 = 0
  while True:
    next = fibn_1 + fibn_2
    yield next
    fibn_2 = fibn_1
    fibn_1 = next




def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
