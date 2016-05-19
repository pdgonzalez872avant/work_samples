require 'rspec'

module DailyProgrammer
  class Easy267

    SINGLE_DIGITS = { '1'  => 'st',
                      '2'  => 'nd',
                      '3'  => 'rd',
                    }

    SPECIAL = {
                '11' => 'th',
                '12' => 'th',
                '13' => 'th',
               }

    def self.ordinal(el)
      el = el.to_s # handle integers as well as strings

      length = el.split('').length

      if length == 1
        handle_sigle_digit(el)
      elsif length > 1
        handle_multiple_digits(el)
      else
        "not implemented yet"
      end
    end

    def self.element_is_special?(el)
      SPECIAL.include?(el)
    end

    def self.handle_special_digits(el)
      "#{el}#{SPECIAL[el]}"
    end

    def self.handle_sigle_digit(el)
      SINGLE_DIGITS.include?(el) ? "#{el}#{SINGLE_DIGITS[el]}" : "#{el}th"
    end

    def self.handle_multiple_digits(el)
      last_two = parse_last_two_digits(el)

      return handle_special_digits(last_two) if element_is_special?(last_two)
      return "#{el}" if first_digit_is_zero?(last_two)   # handle zero

    end

    def self.parse_last_two_digits(el)
      split_el = el.split('')
      "#{split_el[-2]}#{split_el[-1]}"
    end

    def self.first_digit_is_zero?(el)
      return true if el[0] == '0'
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

    it 'handles zero'


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

  context '.first_digit_is_zero?' do
    it 'parses zero correctly' do

    end
  end

end
