# This is an attempt to be as functional as I possibly can with Ruby.
# It has been a good exercise, different way of thinking.
module Rosalind
  class DnaNucleotides

    def self.parse_dna_string(dna_string: )

      prepared_string = prepare_dna_string(dna_string)

      compiled_data = compile_data(prepared_string: prepared_string,
                                   hash:            Hash.new(0))
      display_data(compiled_data)
    end

    def self.prepare_dna_string(dna_string)
      dna_string.split('')
    end

    def self.compile_data(prepared_string:, hash:)
      result = prepared_string.each do |e|
        hash[e] += 1
      end
      hash
    end

    def self.display_data(compiled_data)
      "#{compiled_data['A']} #{compiled_data['C']} #{compiled_data['G']} #{compiled_data['T']}"
    end
  end
end
