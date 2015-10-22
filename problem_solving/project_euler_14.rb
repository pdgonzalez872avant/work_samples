
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

def collatz
  highest_count = {number: 2, running_count: 1}
  (3..1_000_000).each do |number|
    starting_number = number
    temp_array = []
    get_length(number, temp_array)

    if temp_array.length > highest_count[:running_count]
      highest_count[:number] = starting_number
      highest_count[:running_count] = temp_array.length
    end

    p highest_count
  end
  
  return highest_count
end

def get_length(number, temp_array)
  while number > 1
    if number.even?
      number = number/2
      temp_array << number
    else
      number = 3 * number + 1
      temp_array << number
    end
  end
  return temp_array
end

p collatz
