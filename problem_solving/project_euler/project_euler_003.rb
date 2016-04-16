"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

require 'prime'

factors = []

number = 600851475143

results =  number.prime_division

results.each {|i| factors.push(i[0])}

puts factors

# puts results