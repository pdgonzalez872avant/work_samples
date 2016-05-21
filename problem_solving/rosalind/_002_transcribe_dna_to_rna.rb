# This is an attempt to be as functional as I possibly can with Ruby.
# It has been a good exercise, different way of thinking.
module Rosalind
  class DnaToRna
    def self.transcribe(dna_string: )
      dna_string.gsub('T', 'U')
    end
  end
end
