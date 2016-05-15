require 'rspec'

describe Enumerable do
  context 'all?' do

    let(:strings) { ['longerstring', 'short', 'no', 'yeeeeah'] }

    context 'takes a collection and passes each element of the collection to a block' do
      context 'numbers' do
        it 'returns true if all elements are integers and greater than 0' do

          integers = [1, 2, 3, 4]

          result = integers.all? do |e|
            e.is_a?(Integer) && e > 0
          end
          expect(result).to be true
        end

        it 'returns false if any elements are floats' do
          not_all_floats = [1.2, 2.3, 3, 4.0]

          result = not_all_floats.all? { |e| e.is_a?(Float) }
          expect(result).to be false
        end

      end

      context 'strings'

      context 'edge case -> nils'
    end
  end
end

all_enumerables = [ 'all?',
                    'any?',
                    'chunk',
                    'chunk_while',
                    'collect',
                    'collect_concat',
                    'count',
                    'cycle',
                    'detect',
                    'drop',
                    'drop_while',
                    'each_cons',
                    'each_entry',
                    'each_slice',
                    'each_with_index',
                    'each_with_object',
                    'entries',
                    'find',
                    'find_all',
                    'find_index',
                    'first',
                    'flat_map',
                    'grep',
                    'grep_v',
                    'group_by',
                    'include?',
                    'inject',
                    'lazy',
                    'map',
                    'max',
                    'max_by',
                    'member?',
                    'min',
                    'min_by',
                    'minmax',
                    'minmax_by',
                    'none?',
                    'one?',
                    'partition',
                    'reduce',
                    'reject',
                    'reverse_each',
                    'select',
                    'slice_after',
                    'slice_before',
                    'slice_when',
                    'sort',
                    'sort_by',
                    'take',
                    'take_while',
                    'to_a',
                    'to_h',
                    'zip'
                  ]
