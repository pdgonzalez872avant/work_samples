class Animal
  def to_s
    "I am an animal"
  end
end

# c = Animal.new
# puts c.to_s

class Dog < Animal
  def to_s
    "I am a dog"
  end
end

d = Dog.new
puts d.to_s