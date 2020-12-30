def max_sequence(arr):
	# 1. List containing all subarrays
	subs = []
	i = 0
	while i < len(arr)-1 :
		j = i+1
		while j < len(arr) :
			subs.append(arr[i:j+1])
			j += 1
		i+= 1
	# 2. Calculating the maximum subarray
	s = 0
	for sub in subs :
		if sum(n for n in sub) > s :
			s = sum(n for n in sub)
	return s


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

input()
