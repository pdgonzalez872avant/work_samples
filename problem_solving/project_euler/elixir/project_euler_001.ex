defmodule Problem_001 do

  def valid?(e) do
    if (rem(e, 3) == 0) || (rem(e, 5) == 0) do
      true
    end
  end

  def main(range) do
    Enum.reduce(range, 0, fn(e, acc) ->
      if valid?(e) do
        IO.puts(e)
      end
    end)
  end
end

defmodule Test do
  def assert(func, value) do
    unless func == value do
      raise "there is a problem"
    end
  end
end

Test.assert(Problem_001.valid?(3), true)
Test.assert(Problem_001.valid?(5), true)
Test.assert(Problem_001.valid?(9), true)
Problem_001.main(1..9)

#f = fn(x) -> ((rem(x, 3) == 0) || (rem(x, 5) == 0)) end
#result = Enum.filter((1..9), f)
#result = Enum.sum(result)
#IO.inspect "#{result}"


IO.puts "All tests pass"
