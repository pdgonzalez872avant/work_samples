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

unless Geom.area(3, 4) == 12 do
  raise "failed 1"
end

unless Geom.area(7, 3) == 21 do
  raise "failed 2"
end

unless Geom.area(12, 7) == 84 do
  raise "failed 3"
end

# tests defaults
unless Geom.area == 1 do
  raise "failed 4"
end

IO.puts "all tests pass"
