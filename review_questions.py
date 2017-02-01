# Review questions
# 1. Which of the following are operators, and which are values?

# *				# multiplication / string replication operator
# 'hello'		# string value
# -88.8			# floating point value
# -				# subtraction operator
# /				# divison operator
# +				# addition / string concatenation operator
# 5				# integer value

# 2. Which of the following is a variable, and which is a string?

# spam			# variable
# 'spam'		# string value

# 3. Name three data types.
				# strings
				# integers
				# floating points

# 4. What is an expression made up of? What do all expressions do?
				# expressions contain values that reduce down to single value
				
# 5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?
				# expressions return a value, where as statements assign a value
				
# 6. What does the variable bacon contain after the following code runs?

# bacon = 20	# bacon contains the value 20, because we didn't re-assign a value to it
# bacon + 1

# 7. What should the following two expressions evaluate to?

# 'spam' + 'spamspam' # in python prompt these would return
# 'spam' * 3          # spamspamspam

# 8 Why is eggs a valid name  while 100 is invalid
				# variable names can't start with a number
				
# 9. What three functions can be used to get the integer, floating-point number, or string version of a value?
				# str()
				# int()
				# float()
				
# 10. Why does this expression cause an error? How can you fix it?

# 'I have eaten ' + 99 + ' burritos.'
				# this causes an error because you can't concatenate the strings and integers, you must first convert 99 into a string wig
				# "I have eaten " str(99) + " burritos" 