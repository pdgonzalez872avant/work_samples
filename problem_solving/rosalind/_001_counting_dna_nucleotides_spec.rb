require 'rspec'
require_relative 'counting_dna_nucleotides_001'

describe Rosalind::DnaNucleotides do

  let(:sample_string) {'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'}

  let(:challenge_string) do
    "TAGTCGCTGTTGCAGTGGCAAAAGTCCTAGAGTGCACAAGCCTATCTCAGAACCCAACACCTGTGGGGGGATATTGTCGTTTGAATACAGCAGAGTTTGAACGCGGGCGATCTTCACGCAAGTCGGGGATGTACAGCGCTCACAAGGACTGGGGGTCAAATGTGGGTGTCACCGTCCGCACAACTCGCCACTCGCGTTAGCGGCTAAGACTCTCACTCCATTTAGCATGCCTAATACCACCTAGAACACACCTGTTTCTGCCTGTAGTGGACTCTTTGCGCCGTTTCTACTGCCGAACTAGAGGGAGGGATACACTACAAATTCGGACCCTGAGCCAGCCCCTACGGCTTCGTGATACCTGTCCCTTACGCCAGGAAATCTTGGTTCACAGGAAACCCTTCTAACGTGGAAGCGGCCTAAGGGGCAGAGTTCATCCATACTCCAATCTGTTCATGGCTCCGCTACAGGTCTCTCATTGTCAAATCGAGTGTTCTGATATTCTCACTGGTGTTGGCTAATCGGGACAGCTTAAGTTATGTGAGTTCGTCCCGACACGAAGTTCCGGTTAGGAGCATTCACGACTTCTGCATTCGACACAGTACCCTTCCCTAGGCCTAATGAGCGTGGATTTTCACTGACTTCAGGAGCATGTTGGAACGTATTCAGGTAATGCTCGCACGTAATACCCATCTGCCCCATCTTTGCGCAGCCCCAACCCAGACTCATCTGTCAGAGTGGGCAACCTTAATATCCAGCGTTGATCTATACACGTAAAGACCGCACTGGCCGGTGTCATCGAACTTGCGATG"
  end

  it 'returns the expected output' do
    result = described_class.parse_dna_string(dna_string: sample_string)

    expect(result).to eq('20 12 17 21')
  end

  it 'solves the challenge' do
    result = described_class.parse_dna_string(dna_string: challenge_string)

    expect(result).to eq('190 222 195 202')
  end
end