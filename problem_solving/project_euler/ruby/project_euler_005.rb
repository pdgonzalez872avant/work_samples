"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

"""
Thinking:

- The range has duplicate values, yielding unnecessary calcs. For example, if divisible by 20, it is divisible by 10

<<<<<<< HEAD
- Should have something to do with prime numbers, maybe can multiply only them and brute force backwards. 
"""

primes = [1,2,3,4,7,11,13,17,19]

mult = 1

primes.each {|i| mult *= i}

puts mult

puts mult % 20
=======
- Should have something to do with prime numbers, maybe can multiply only them and brute force backwards.
"""


# Brute Force!
(1..1000000000).each {|i|
  if i % 1 == 0 &&
     i % 2 == 0 &&
     i % 3 == 0 &&
     i % 4 == 0 &&
     i % 5 == 0 &&
     i % 6 == 0 &&
     i % 7 == 0 &&
     i % 8 == 0 &&
     i % 9 == 0 &&
     i % 10 == 0 &&
     i % 11 == 0 &&
     i % 12 == 0 &&
     i % 13 == 0 &&
     i % 14 == 0 &&
     i % 15 == 0 &&
     i % 16 == 0 &&
     i % 17 == 0 &&
     i % 18 == 0 &&
     i % 19 == 0 &&
     i % 20 == 0
     puts i
     break
  end
}
>>>>>>> f7d267a578544b81084e47a6db472a30090f50d5
