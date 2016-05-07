defmodule Geom do
  @moduledoc """
  This is one etude from many.
  """

  @doc """
  This is the doc. I wonder how to print the docs for functions.
  """

  def area(length \\ 1, height \\ 1) do
    length * height
  end
end

defmodule Assertions do
  @moduledoc """
  This is to scope assertions
  """

  @doc """
  To make assertions easier
  """

  def assertions(func, result) do
    unless func == result do
      raise "failed: func result is #{func} and result is #{result}"
    end
  end
end

# tests
Assertions.assertions(Geom.area(3, 4), 12)
Assertions.assertions(Geom.area(7, 3), 21)
Assertions.assertions(Geom.area(12, 7), 84)
Assertions.assertions(Geom.area, 1)

IO.puts "all Geom tests pass"

defmodule Test do
  def sum(a \\ 3, b, c \\ 7) do
    IO.puts "#{a} a"
    IO.puts "#{b} b"
    IO.puts "#{c} c"
    IO.puts "---"
    a + b + c
  end
end

IO.puts Test.sum(11, 22, 33)
IO.puts Test.sum(11, 22)
IO.puts Test.sum(11) # Interesting. The argument goes to the first item that does not have a default when possible.
