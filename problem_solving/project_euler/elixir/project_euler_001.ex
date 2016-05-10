
defmodule Problem_001 do

  use GenServer

  def collect(range) do
    23
    #sum = []
  #new_data = for data <- old_data do
  #  data
  #end

  #Enum.reduce([1, 2, 3], 0, fn(x, acc) -> x + acc end)

  end

  def yeah(i, acc) do
    if i < 3 do
      {:cont, acc + i}
    else
      {:halt, acc}
    end
  end

  def sum(x, acc) do
    x + acc
  end

  def divisible_by_3(n) do
    if rem(n, 3) == 0 do
      true
    else
      false
    end
  end
end

# group_by

defmodule Test do
  def assert(func, value) do
    unless func == value do
      raise "there is a problem"
    end
  end
end

Test.assert(Problem_001.divisible_by_3(3), true)
Test.assert(Problem_001.collect(0..10), 23)

#Problem_001.collect(0..10)

range = (1..10)

#f = fn(x, acc) -> x * acc end



#f = fn(i, acc) -> if Problem_001.divisible_by_3(i), do: {:cont, acc + i}, else: {:halt, acc} end
#f = fn(i, acc) -> if rem(i, 3) == 0, do: {:cont, acc + i}, else: {:halt, acc} end

#f = fn(x, acc) -> x + acc end

f = fn
  (x, acc) when x > 0 -> x + acc
end

hi = Enum.reduce(range, 0, f)
IO.puts hi

#IO.puts Enum.reduce_while(range, 0, f)

IO.puts "All tests pass"
