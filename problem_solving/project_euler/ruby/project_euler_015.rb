# This was very interesting. I didn't even know how to begin, so I researched
# this problem.

# The key seems to be to think about the grid as grid points.

# Somehow want to add a x,y coord to a data structure so we can use the coordinates
# to calculate the path

# I will use a hash to do this

def lattice (size)

  # Create data structure
  coords = {}

  # We need to use both 0,0 and also size,size, therefore must add 1 to size.
  new_size = size + 1

  # Create x,y coords
  new_size.times do | i |
    new_size.times do | j |
      # coords["S#{i}#{j}"] = [i-1, j]
    end
  end

  return coords
end

p lattice(5)
