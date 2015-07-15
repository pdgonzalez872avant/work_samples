
=begin

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

=end


# this has to do with prime numbers and the fact that you don't need to test for every number up to
# it, you just need to test up to its square root


def is_this_prime(input_number)

  sum_of_primes = []
  square_root = input_number ** 0.5

  (2..square_root).each { |i|
    if input_number % i == 0
      puts "Not Prime!  #{i}"

    else
      sum_of_primes << input_number
    end
    # puts "Yeah! #{num} , #{i}"
  }

  puts sum_of_primes

end

is_this_prime(25)