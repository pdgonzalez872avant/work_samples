def rot13(input_string)
  rules = hash_table

  split_string = input_string.split('')

  translated_string = translate_string(split_string: split_string,
                                       rules: rules)
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
  split_string.inject('') do |translated_string, letter|
    translated_string += rules[letter]
  end
end

p 'Starting tests'

raise "Not working Yet" unless rot13("HELLO") == "URYYB"
p 'passed'
raise "Not Working Yet" unless rot13("FREE CODE CAMP") == "SERR PBQR PNZC"
p 'passed'
raise "Not Working Yet" unless rot13("SERR CVMMN!") == "FREE PIZZA!"
p 'passed'
raise "Not Working Yet" unless rot13("SERR YBIR?") == "FREE LOVE?"
p 'passed'
raise "Not Working Yet" unless rot13("GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.") == "THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX."

p "All passed"
