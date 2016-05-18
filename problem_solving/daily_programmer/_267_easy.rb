require 'rspec'

module DailyProgrammer
  class Placement

    SINGLE_DIGITS = { '1'  => 'st',
                      '2'  => 'nd',
                      '3'  => 'rd',
                    }

    SPECIAL = {
                '11' => 'th',
                '12' => 'th',
                '13' => 'th',
               }

    def self.print(el)
      parse(el)
    end

    def self.parse(el)

      splitted = el.split('')

      first_digit = splitted[-1]

      if special?(el)
        return "#{el}#{SPECIAL[el]}"
      end

      if splitted.length > 1
        "#{el}#{SINGLE_DIGITS[el]}"
      end

      # p splitted.length

      # if special?(el)
      #   "#{el}#{HASH_LOOKUP[el]}"
      # else
      #   "#{el}th"
      # end
    end

    def self.special?(el)
      SPECIAL.include?(el)
    end
  end
end



describe DailyProgrammer::Placement do
  context '#parse' do
    it 'handles 1 correctly' do
      result = described_class.print('1')

      expect(result).to eq '1st'
    end

    it 'handles 2 correctly' do
      result = described_class.print('2')

      expect(result).to eq '2nd'
    end

    it 'handles 3 correctly' do
      result = described_class.print('3')

      expect(result).to eq '3rd'
    end

    it 'handles 11 correctly' do
      result = described_class.print('11')

      expect(result).to eq '11th'
    end

  end
end
