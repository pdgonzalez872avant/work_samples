# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

require 'prime'

def index_prime(input_index)

  index = 0
  prime_number = 0

  # Iterates through 0 to the input_index, increments the index and also the prime number variable.
  while index < input_index do

    if Prime.prime?(prime_number)
      index += 1
    end

    prime_number += 1
  end

  return prime_number - 1

end

puts index_prime(10001)