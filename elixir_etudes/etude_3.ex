defmodule Geom do
  @moduledoc """
  This is one etude from many.
  """

  @doc """
  This is the doc. I wonder how to print the docs for functions.
  """

  def area(:rectangle, length, width) do
    length * width
  end

  def area(:triangle, base, height) do
    (base * height) / 2
  end

  def area(:ellipse, major, minor) do
    :math.pi() * major * minor
  end
end


defmodule Test do
  def assert(func, value) do
    unless func == value do
      raise "Something bad happened"
    end
  end
end

Test.assert(Geom.area(:rectangle, 3, 4), 12)
Test.assert(Geom.area(:triangle, 3, 5), 7.5)
Test.assert(Geom.area(:ellipse, 2, 4), 25.132741228718345)

IO.puts "All tests passed"
