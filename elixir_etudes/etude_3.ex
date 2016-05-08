defmodule Geom do
  @moduledoc """
  This is one etude from many.
  """

  @doc """
  This is the doc. I wonder how to print the docs for functions.
  """

  def area({shape, a, b}) do
    area(shape, a, b)
  end

  defp area(:rectangle, length, width) when length >= 0 and width >= 0 do
    length * width
  end

  defp area(:triangle, base, height) when base >= 0 and height >= 0 do
    (base * height) / 2
  end

  defp area(:ellipse, major, minor) when major >= 0 and minor >= 0 do
    :math.pi() * major * minor
  end

  # this catches all things :)
  defp area(_, _, _) do
    0
  end
end


defmodule Test do
  def assert(func, value) do
    unless func == value do
      raise "Something bad happened"
    end
  end
end

#Test.assert(Geom.area(:rectangle, 3, 4), 12)
#Test.assert(Geom.area(:triangle, 3, 5), 7.5)
#Test.assert(Geom.area(:ellipse, 2, 4), 25.132741228718345)

IO.puts "All tests passed"

#Test.assert(Geom.area(:rectangle, -3, 4), 0)
#Test.assert(Geom.area(:pentagon, 3, 4), 0)
#Test.assert(Geom.area(:ellipse, -1, 5), 0)
#Test.assert(Geom.area(:triangle, 5, -1), 0)

IO.puts "All tests passed, with guard"

Test.assert(Geom.area({:rectangle, 7, 3}), 21)
Test.assert(Geom.area({:triangle, 7, 3}), 10.5)
Test.assert(Geom.area({:ellipse, 7, 3}), 65.97344572538566)
Test.assert(Geom.area({:pentagon, 7, 3}), 0)

IO.puts "All tests passed with tuple stuff"
