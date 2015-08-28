import doctest

# Calculates a^b using only addition
def expFromAdd(a,b):
	"""Calculates a^b using only addition
    >>> expFromAdd(2,3)
    8
    >>> expFromAdd(5,5)
    3125
    """
	result = 1
	for j in range(0, b):
		temp = 0
		for j in range(0, a):
			temp += result
		result = temp
	return result

doctest.testmod()