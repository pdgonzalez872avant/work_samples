
def p9(input_value)

  # Initiate variables
  a, b, c = 0, 1, 2

  # Condition hash
  condition_hash = {"A": a + b + c == input_value,
                    "B": a**2 + b**2 == c**2
  }


  # puts condition_hash[:A]

  # until condition_hash[:A] == true do
  # # while condition_hash[:A] && condition_hash[:B] == true do
  #   a += 1
  #   b += 1
  #   c += 1
  #   puts a, b, c
  # end

  puts a, b, c
  # if a + b + c == input_value
  #   puts "yes"
  # else
  #   puts "no"
  #   # puts condition_hash[:A]
  # end



end

# puts p9(1000)
p9(1000)

puts

