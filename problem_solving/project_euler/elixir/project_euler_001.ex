defmodule Problem_001 do

  def valid?(e) do
    if (rem(e, 3) == 0) || (rem(e, 5) == 0) do
      true
    else
      false
    end
  end

  def main(range) do
    valid_numbers = for n <- range, valid?(n), do: n
    Enum.sum(valid_numbers)
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
Test.assert(Problem_001.valid?(4), false)
Test.assert(Problem_001.valid?(9), true)
Test.assert(Problem_001.main(1..9), 23)

#f = fn(x) -> ((rem(x, 3) == 0) || (rem(x, 5) == 0)) end
#result = Enum.filter((1..9), f)
#result = Enum.sum(result)
#IO.inspect "#{result}"





IO.puts "All tests pass"
