require 'rspec'

describe Enumerable do

  let(:all_enumerables) { [ 'all?',
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
                          ] }

  context 'inject' do
  end

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
    context 'takes a collection and passes each element of the collection to a block. Halts whenever condition is not met' do
      it 'returns true if my condition is met - in this case, if there is a nil value in the collection' do
      	nil_spy = [1, 2, 'three', nil]

      	result = nil_spy.any? { |e| e.nil? }
      	expect(result).to be true
      end

      it 'returns true when there is a substring match' do
        substring_match = ['one', 2, 'three', :four, 'bad one over here']

        result = substring_match.any? { |e| e.to_s.scan(/bad/) }
        expect(result).to be true
      end

      it 'returns false when there is no match' do
        no_match = [1, 2, 3, 4]

        result = no_match.any? { |e| e < 0 }
        expect(result).to be false
      end
    end
  end # any?

  context 'reduce' do
    context 'iterates through elements and returns an accumulator (combined) based on the block supplied' do

      let(:project_euler001) { 1..999 }

      it 'returns a sum correctly -> Project Euler #001' do
        valid_numbers = project_euler001.select do |e|
          e % 3 == 0 || e % 5 == 0
        end

        result = valid_numbers.reduce(:+)

        expect(result).to eq(233168)
      end
    end
  end # reduce

  context 'collect' do
    context 'iterates through a collection and returns an array with the results of running the block that is provided' do

      let(:even_numbers) { [2, 4, 6, 8] }

      it 'returns an array' do
        result = even_numbers.collect { |e| e }

        expect(result).to be_a(Array)
      end

      it 'does math' do
        result = even_numbers.collect { |e| e ** 5 }
        expected = [32, 1024, 7776, 32768]

        expect(result).to eq(expected)
      end

      it 'can save time with annoying operations, such as manipulating data' do
        result = all_enumerables.collect do |e|
          "context '#{e}' do \n end"
        end

        # result.each { |e| puts e } # This is how this could save you time

        expect(result[0]).to eq("context 'all?' do \n end")
      end

      it 'can handle different types' do
        different_types = ['one', 2, 'three', :four, 'bad one over here']
        expected        = [false, true, false, false, false]

        result = different_types.collect do |e|
          e.is_a?(Integer)
        end
        expect(result).to eq(expected)
      end
    end
  end # collect

  context 'chunk' do
    context 'iterates over the items, chunking them together based on the return value of the block' do
      it 'chunks -> aka *combines* values based conditions and returns an enumerator' do
        even_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

        result = even_numbers.chunk { |e| e.even? && e > 5}

        expected = [[false, [3, 1, 4, 1, 5, 9, 2]],
                    [true, [6]],
                    [false, [5, 3, 5]]]

        any_true_matches =  result.any? { |e| e[0] == true }

        expect(result).to be_a(Enumerator)
        expect(any_true_matches).to be true
      end
    end
  end # chunk

  context 'chunk_while' do
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
