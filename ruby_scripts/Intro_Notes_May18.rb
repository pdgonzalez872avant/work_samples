# t = """
# This is a longer string

# Let's see what happens if I print this to the screen
# """
# puts t



list = ["this", "is", "a", "list"]
puts "#{list[1]} --- This is a slice! list[1]}"


# Enumerate
list.each_with_index {|itm,index| 
	puts " This is the item: #{itm}, This is the index: #{index}"
} 

# Iterates to the next number
puts 5.next

# Frequencies

hash = Hash.new(0)
text = "This is a cool text This is is is is"
text.split(' ').each {|word| 
	if hash.include? word
		hash[word] += 1
	else	
		hash[word] = 1
		#puts "nope"
	end
}

puts hash.length

hash.each {|k, v| puts "#{k} has frequency of #{v}"}








