
=begin

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

=end


# this has to do with prime numbers and the fact that you don't need to test for every number up to
# it, you just need to test up to its square root



def is_this_prime(input_number)

  # Initiates variables
  square_root = input_number ** 0.5
  ceiling = square_root + 1

  # tries to divide by 2. Optimizes loops
  return false if input_number % 2 == 0

  # A prime number doesn't have to be divided by all numbers before it. It can be divided up to the square
  # root of said number. In this case, I add 1 to account for negative.
  (3..ceiling).step(2).each { |i|

    # returns as soon as the number is divisible.
    return false if input_number % i == 0
  }
    # If it hasn't returned false, it will return true since the number is indeed prime.
    return true
end

# # Sanity check
# p is_this_prime(9)
# p is_this_prime(23)

def add_to_prime_array(input_number)

  # Initiates variables
  start = Time.now

  # Since I start checking the primes at 3, I add 2 to the cumulative prime number.
  prime_sum = 2

  # Iterates through range, tests if the number is a prime, if so, increments a variable with said number.
  (2..input_number).each { |i|

  # Conditional
  if is_this_prime(i) == true

    # Increments variable
    prime_sum += i

    # Sanity check, can be commented out.
    p "#{i} -> #{prime_sum}"
  end
  }

  # Calculates the time it took to solve the problem
  finish = Time.now
  elapsed_time = finish - start

  return prime_sum, elapsed_time
end

# Uses function.
p add_to_prime_array(2000000)