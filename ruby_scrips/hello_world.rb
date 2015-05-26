# ruby scrips trying this out

#File.open()

# print Dir.pwd

class Dog
	
	def initialize(name, breed)
		@breed = breed
		@name = name
	end

	def bark
		puts "Ruff Ruff wow"
	end

	def display
		puts "I am #{@name} and I am a #{@breed}"
	end
end

# # Puttin it to work
# d = Dog.new("Kasey", "Mutt")
# d.bark
# d.display


class CreateFiles

	def initialize(file_name)
		@file_name = file_name
	end

	def creates_new_file(word)
		f = File.new("#{@file_name}.txt", "w")
		f.write("#{word}")
		puts "#{word}"
		return f
	end

end

# # Putting class to work
# c = CreateFiles.new("paulo")
# cf = c.creates_new_file("dog")
# cf.write("great!")
# cf.close


# # Creates csv
# new_csv = File.new("csv_test.csv", "w")
# new_csv.write("Name,Address\n")
# new_csv.write("Second,Line")

# Opens csv and reads in lines
require 'csv'
arr_of_arrs = CSV.read("expenses.csv")

# Creates new array
paulo_total = []

# # This adds an item to an array
#paulo_total.push(itm)

# slice to skip the header == arr_of_arrs[2..-1]
# This adds sliced items of an array to another array
arr_of_arrs[2..-1].each do |itm| 
	case itm[1]
		when "Paulo"
			paulo_total.push(itm[4])
		when "Kelsey"

		when "Joint"
			paulo_total.push(itm[4].to_f/2)
	end
end

# # Loop technique for only one action
# object.each {|x| puts x}
# # Loop technique for multiple actions
# object.each do <code> <code1> end


# Apparently there is no array sum function in Ruby, I doubt it, but so far thats what I saw
# Therefore, we create the functions ourselves, mainly using counters and iteration
sum = 0 # Starts counter
paulo_total.each {|i| sum = sum + i.to_f} # or paulo_total.each {|i| sum += i}
puts sum


# # Creates unique value array
categories = []

# Loops through the array looking for unique values
arr_of_arrs[2..-1].each do |itm|

	category, amount = itm[2], itm[4]

	if categories.include?(category)
		# do nothing
	else
		categories.push(category)
	end
end

puts "#{categories.to_s} are the categories"

# # Practice a little bit of hash stuff -> k, v pairs



t = """
This is a longer string

Let's see what happens if I print this to the screen
"""

puts t

list = ["this", "is", "a", "list"]
puts list[1]

list.each {|x| puts x}

# # Conditionals
# if <code> end



















