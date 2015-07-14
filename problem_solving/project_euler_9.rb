

def p9(input_value)

  # Found a list of triplets up to 2,000. Will test some to see the if sum is 1000
  # http://www.tsm-resources.com/alists/trip.html

  # Here is the winner for the sum == 1000, a [8 - 15 - 17] triplet
  # 200 + 375 + 425

  # I'll come back to this problem once I understand algorithms better

  # Initiate variables
  a, b, c = 200, 375, 425

  # Condition hash
  condition_hash = {A: a + b + c == input_value,
                    B: a*a + b*b == c*c,
                    C: c == (a**2 + b**2)**0.5}

  # Would like to have stored a D: key with a value that
  # checked :A, :B, :C as true. Could not get it to work
  # all conditions combined. Must be better way...


  should_be_true = condition_hash[:A] == true &&
                   condition_hash[:B] == true &&
                   condition_hash[:C] == true

  return a * b * c if should_be_true == true

end

puts p9(1000)






















