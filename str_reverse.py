def reverse(s):
	return s[::-1]

#example
words = "andela"
print reverse(words)	

def reverse(s):
	new_s =list(s)
	for i in range(len(new_s)//2):
		new_s[i], new_s-i-1 = new_s(new_s)-i-1], new_s[i]

'''		temp = new_s[i]
		new_s[i] = new_s [len(new_s)-i-1]
		new_s[len{new_s-i-1] = temp '''

