Hello! As an attempt to make a prime number sieve using Python, I have started a new repository here... 
At this moment of development, I am only uploading a module for calculating gcd and lcm.
Please do tell me if you find any bug here... :)
---------------------
My gratitude goes to:
(1)Wikipedia - for getting me an article on prime number sieves
(2)The inventors of the Sieve of Atkin
(3)Well, you all who download this or at least star this... :)

---------------------
How to do:
---------------------
Check the 'SieveExample.py' file for how I did it.
Steps:
1) Filter out all numbers till the limit which satisfy the condtion:
n!/n^2  != 0 (n = the number we take)
2) Remove all numbers which, when factorised, gives more than two integer factors.
