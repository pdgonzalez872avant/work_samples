# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def p9(input_value)

  # Initiate variables
  a, b, c = 0, 0, 0

  range = (1..input_value)

  # # Condition hash
  # condition_hash = {A: a + b + c == input_value,
  #                   B: a*a + b*b == c*c,
  #                   C: c == (a**2 + b**2)**0.5,
  #                   D: a == 10}

  # # Would like to have stored a D: key with a value that
  # # checked :A, :B, :C as true. Could not get it to work
  # # all conditions combined. Must be better way...

  # should_be_true = condition_hash[:A] == true &&
  #                    condition_hash[:B] == true &&
  #                    condition_hash[:C] == true

  range.each { |first_loop|
    range.each { |second_loop|
      a, b, c_squared = first_loop, second_loop, (a*a + b*b)
      # c = (c_squared ** 0.5).to_i # This failed... bad rounding.

      c = 1000 - a - b
      product = a * b * c

      # Wanted to use a conditional hash here, but was not able to.
      condition_hash = {A: a + b + c == input_value,
                        B: a*a + b*b == c*c,
                        C: c == (a**2 + b**2)**0.5,
                        D: a == 10}

      return "#{a}, #{b}, #{c} -> #{product}" if a + b + c == input_value && a*a + b*b == c*c
    }
  }

end

p p9(1000) # 31875000






















