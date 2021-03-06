require 'rspec'

# This was finished on May/18/2016
# This is my attempt of solving this problem in a functional way.
# I do like how I don't deal with the state of the object, but passing around
# arguments seems a little too much. Interesting problem, learned a lot.

module DailyProgrammer
  # Source:
  # https://www.reddit.com/r/dailyprogrammer/comments/4jom3a/20160516_challenge_267_easy_all_the_places_your/

  # Notes: I modified the challenge to solve the crux only: to return the ordinal version of any
  # integer or string that is passed to the method.
  class Easy267
    SINGLE_DIGITS = { '1'  => 'st',
                      '2'  => 'nd',
                      '3'  => 'rd' }.freeze

    SPECIAL       = { '11' => 'th',
                      '12' => 'th',
                      '13' => 'th' }.freeze

    def self.ordinal(el)
      return '0' if element_is_zero?(el)

      el = el.to_s # handle integers as well as strings

      length = el.split('').length

      if length == 1
        print_digits(el: el, handler: handle_sigle_digit(el))
      elsif length > 1
        handle_multiple_digits(el)
      else
        'not implemented'
      end
    end

    def self.handle_multiple_digits(el)
      last_two_digits = parse_last_two_digits(el)
      last_digit = last_two_digits[-1]


      if element_is_special?(last_two_digits)
        print_digits(el: el, handler: handle_special_digits(last_two_digits))
      elsif second_digit_is_zero?(last_two_digits)
        print_digits(el: el, handler: handle_sigle_digit(last_digit))
      else
        simple_ordinal(el)
      end
    end

    def self.element_is_special?(el)
      SPECIAL.include?(el)
    end

    def self.handle_special_digits(el)
      (SPECIAL[el]).to_s
    end

    def self.handle_sigle_digit(el)
      SINGLE_DIGITS.include?(el) ? (SINGLE_DIGITS[el]).to_s : 'th'
    end


    def self.parse_last_two_digits(el)
      split_el = el.split('')
      "#{split_el[-2]}#{split_el[-1]}"
    end

    def self.second_digit_is_zero?(el)
      el[0] == '0'
    end

    def self.element_is_zero?(el)
      el.to_s == '0'
    end

    def self.simple_ordinal(el)
      "#{el}th"
    end

    def self.print_digits(el:, handler:)
      "#{el}#{handler}"
    end
  end
end

describe DailyProgrammer::Easy267 do
  context '.ordinal' do
    it 'handles 1 correctly' do
      result = described_class.ordinal('1')

      expect(result).to eq '1st'
    end

    it 'handles 2 correctly' do
      result = described_class.ordinal('2')

      expect(result).to eq '2nd'
    end

    it 'handles 3 correctly' do
      result = described_class.ordinal('3')

      expect(result).to eq '3rd'
    end

    it 'handles 4 correctly' do
      result = described_class.ordinal('4')

      expect(result).to eq '4th'
    end

    it 'handles 11 correctly' do
      result = described_class.ordinal('11')

      expect(result).to eq '11th'
    end

    it 'handles 13 correctly' do
      result = described_class.ordinal('13')

      expect(result).to eq '13th'
    end

    it 'handles 14 correctly' do
      result = described_class.ordinal('14')

      expect(result).to eq '14th'
    end

    it 'handles integers correctly' do
      result = described_class.ordinal(13)

      expect(result).to eq '13th'
    end

    it 'handles edge case -> 111' do
      result = described_class.ordinal(111)

      expect(result).to eq '111th'
    end

    it 'handles edge case -> 104' do
      result = described_class.ordinal(104)

      expect(result).to eq '104th'
    end

    it 'handles edge case -> 101' do
      result = described_class.ordinal(101)

      expect(result).to eq '101st'
    end

    it 'handles zero' do
      result = described_class.ordinal(0)

      expect(result).to eq '0'
    end

    it 'handles big numbers' do
      result = described_class.ordinal(10_100_014)

      expect(result).to eq '10100014th'
    end
  end

  context '.parse_last_two_digits' do
    it 'parses last two digits correctly' do
      result = described_class.parse_last_two_digits('114')

      expect(result).to eq '14'
    end

    it 'parses last two digits correctly' do
      result = described_class.parse_last_two_digits('10')

      expect(result).to eq '10'
    end
  end

  context '.second_digit_is_zero?' do
    it 'returns true when there is a zero' do
      result = described_class.second_digit_is_zero?('04')

      expect(result).to eq true
    end

    it 'returns false when there is not' do
      result = described_class.second_digit_is_zero?('14')

      expect(result).to eq false
    end
  end

  context '.print_digits' do
    it 'returns a string with the element and the handler we want' do
      result = described_class.print_digits(el: '12', handler: 'th')

      expect(result).to eq '12th'
    end
  end
end
