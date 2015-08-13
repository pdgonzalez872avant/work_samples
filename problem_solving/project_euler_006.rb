# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def some_math(input_array)

  # Starts variables
  sum_squares = 0
  sum = 0

  # Loops over array and increments variables accordingly
  input_array.each { |itm|
    sum_squares += itm**2
    sum += itm
  }

  # Does the necessary math
  result = sum**2 - sum_squares
end

p some_math((1..100))

# # Works, refactored above
# input_array = (1..10)

# sum_squares = 0
# sum = 0

# input_array.each {|i|
#   sum_squares += i**2
#   sum += i
#   # puts i
# }

# p result = sum**2 - sum_squares

