--------------------
Hello! As an attempt to make a prime number sieve using Python, I have started a new repository here... 
Please do tell me if you find any bugs... :)
---------------------
My gratitude goes to:

(1)Wikipedia - for getting me an article on prime number sieves (really interesting articles, indeed !)

(2)The inventors of the Sieve of Atkin (for inspiring me)

(3)Well, you all who download this or at least star this... :) (for supporting me)

---------------------
How to do:
---------------------
Check the 'SieveExample.py' file for how I did it.
Steps:
1) Filter out all numbers till the limit which satisfy the condtion:
n!/n^2  != 0 (n = the number we take)
2) Remove all numbers which, when factorised, gives more than two integer factors.
---------------------
Current Updates (since the last one):
---------------------
1 - Made a simpler sieve

2 - Created a wiki

3 - Uploaded example

4 - Updated MathTools.py with factorial function

________________________
The New Update: Intro for All
________________________
I have newly added a module (Sieve.py) to get an object - oriented kind of feel when creating prime sieves.

------------
How To
------------

1) Import Sieve.py to your code:

  ` import Sieve ` or `from Sieve import *` or `import Sieve as sieve` - the last one may make things easy to use.

2) Set up a sieve using the following command:

  ` sieve = PrimeNumSieve(100) # sieve -> an instance of 'PrimeNumSieve' object, 100 is an arbitary limit (for demo only) `

3) Call the instance as a function:

` sieve()`
