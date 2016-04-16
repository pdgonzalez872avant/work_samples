def rot13(input_string)
  rules = hash_table

  split_string = input_string.split('')

  translated_string = translate_string(split_string: split_string,
                                       rules: rules)
  return translated_string
end

def hash_table
  {
    'A' => 'N',
    'B' => 'O',
    'C' => 'P',
    'D' => 'Q',
    'E' => 'R',
    'F' => 'S',
    'G' => 'T',
    'H' => 'U',
    'I' => 'V',
    'J' => 'W',
    'K' => 'X',
    'L' => 'Y',
    'M' => 'Z',

    'N' => 'A',
    'O' => 'B',
    'P' => 'C',
    'Q' => 'D',
    'R' => 'E',
    'S' => 'F',
    'T' => 'G',
    'U' => 'H',
    'V' => 'I',
    'W' => 'J',
    'X' => 'K',
    'Y' => 'L',
    'Z' => 'M',

    ' ' => ' ',
    '!' => '!',
    '?' => '?',
    '.' => '.',
  }
end

def translate_string(split_string:, rules:)
  translated_string = ''

  split_string.each do |letter|
    translated_string += rules[letter]
  end
  translated_string
end

raise "Bigfoot" unless rot13("HELLO") == "URYYB"
raise "Not Working Yet" unless rot13("FREE CODE CAMP") == "SERR PBQR PNZC"
raise "Not Working Yet" unless rot13("SERR CVMMN!") == "FREE PIZZA!"
raise "Not Working Yet" unless rot13("SERR YBIR?") == "FREE LOVE?"
raise "Not Working Yet" unless rot13("GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.") == "THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX."

p "All passed"
