"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

"""
Thinking:

- The range has duplicate values, yielding unnecessary calcs. For example, if divisible by 20, it is divisible by 10

- Should have something to do with prime numbers, maybe can multiply only them and brute force backwards. 
"""

primes = [1,2,3,4,7,11,13,17,19]

mult = 1

primes.each {|i| mult *= i}

puts mult

puts mult % 20