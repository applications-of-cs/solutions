import doctest

# Calculates a^b using only addition
def expFromAdd(a,b):
	"""Calculates a^b using only addition
    >>> expFromAdd(2,3)
    8
    >>> expFromAdd(5,5)
    3125
    """
	if (b == 0):
		return 1
	result = 1
	for c1 in range(0, b):
		temp = 0
		for c2 in range(0, a):
			temp += result
		result = temp
	return result

doctest.testmod()