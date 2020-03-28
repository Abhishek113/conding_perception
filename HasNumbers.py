def des_bin_search(subtractions, high, low, num):

	if high >= low:
		if subtractions[high] == num or subtractions[low] == num:
			return True
		else:
			med = int((low + high)/2)
			med_num = subtractions[med]
			if med_num == num:
				return True
			else:
				if num < med_num:
					low = med+1
				else:
					high = med-1
				return des_bin_search(subtractions, high, low, num)

	return False


def has_numbers(arr, k):
	arr.sort()  # trim sort = merge sort + insertion sort complexity = N*logN
	subtractions = list()
	for num in arr:
		sub = 0
		if num > k:
			break
		else:
			sub = k - num
			if not subtractions:
				subtractions.append(sub)
			elif subtractions[-1] <= num:
				if des_bin_search(subtractions, len(subtractions)-1, 0, num):  # complexity = logN
					print("searched number: ", num)
					return True
				else:
					subtractions.append(sub)
			else:
				subtractions.append(sub)

	return False


# print(has_numbers([10, 5, 2, 20, 19, 3, 9, 15, 7, 25, 14], 100))
print(has_numbers([10, 15, 3, 7], 17))
