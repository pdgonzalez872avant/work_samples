require 'rspec'

describe Enumerable do
  context 'all?' do
    context 'takes a collection and passes each element of the collection to a block. Halts whenever condition is not met' do
      context 'numbers' do
        it 'returns true if all elements are integers and greater than 0' do
          all_integers = [1, 2, 3, 4]

          result = all_integers.all? do |e|
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

      context 'strings' do
        it 'can evaluate strings based on length' do
          strings = ['longerstring', 'short', 'no', 'yeeeeah']

          result = strings.all? { |e| e.length >= 2 }
          expect(result).to be true
        end

        it 'can evaluate strings based on content' do
          all_have_a = ['langarstrang', 'shart', 'na', 'yaaaaah']

          result = all_have_a.all? { |e| e.include?('a') }
          expect(result).to be true
        end
      end

      context 'truthy assumptions' do
        it 'defaults to truthy values if block is not passed' do
          truthy_values = [1, 2, 'yes', true]

          result = truthy_values.all?
          expect(result).to be true
        end

        it 'defaults to truthy values if block is not passed and returns false if there is a falsy value' do
          falsy_spy_among_truthy_values = [1, 2, 'yes', nil]

          result = falsy_spy_among_truthy_values.all?
          expect(result).to be false
        end
      end
    end
  end # all?

  context 'any?' do
  end

  context 'all?' do
  end

  context 'any?' do
  end

  context 'chunk' do
  end

  context 'chunk_while' do
  end

  context 'collect' do
  end

  context 'collect_concat' do
  end

  context 'count' do
  end

  context 'cycle' do
  end

  context 'detect' do
  end

  context 'drop' do
  end

  context 'drop_while' do
  end

  context 'each_cons' do
  end

  context 'each_entry' do
  end

  context 'each_slice' do
  end

  context 'each_with_index' do
  end

  context 'each_with_object' do
  end

  context 'entries' do
  end

  context 'find' do
  end

  context 'find_all' do
  end

  context 'find_index' do
  end

  context 'first' do
  end

  context 'flat_map' do
  end

  context 'grep' do
  end

  context 'grep_v' do
  end

  context 'group_by' do
  end

  context 'include?' do
  end

  context 'inject' do
  end

  context 'lazy' do
  end

  context 'map' do
  end

  context 'max' do
  end

  context 'max_by' do
  end

  context 'member?' do
  end

  context 'min' do
  end

  context 'min_by' do
  end

  context 'minmax' do
  end

  context 'minmax_by' do
  end

  context 'none?' do
  end

  context 'one?' do
  end

  context 'partition' do
  end

  context 'reduce' do
  end

  context 'reject' do
  end

  context 'reverse_each' do
  end

  context 'select' do
  end

  context 'slice_after' do
  end

  context 'slice_before' do
  end

  context 'slice_when' do
  end

  context 'sort' do
  end

  context 'sort_by' do
  end

  context 'take' do
  end

  context 'take_while' do
  end

  context 'to_a' do
  end

  context 'to_h' do
  end

  context 'zip' do
  end



end # Enumerable

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
