"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(floor, ceiling)
	
	palindromes = []
	
	input_range = floor..ceiling

	max_palindrome = 0

	ct = floor

	while ct <= ceiling

		input_range.each {|i| 
			
			i = i * ct

			if i.to_s == i.to_s.reverse
				
				if i > max_palindrome then max_palindrome = i end
			
			else
				# not palindrome
			end
		}

		ct += 1
	end
	
	return max_palindrome
end


puts is_palindrome(100, 999) # 997799
