import doctest
# HailStone Sequence
# If n is 1 then the sequence ends.
# If n is even then the next n of the sequence = n/2
# If n is odd then the next n of the sequence = (3 * n) + 1

# Create a routine to generate the hailstone sequence for a number.
# Use the routine to show that the hailstone sequence for the number 27 has 112 elements starting with 27, 82, 41, 124 and ending with 8, 4, 2, 1
# Show the number less than 100,000 which has the longest hailstone sequence together with that sequence's length.
# (But don't show the actual sequence!)
def hailstone(n):
	"""Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
	print(int(n))
	if (n == 1):
		return 1
	else:
		if (n % 2 == 0):
			return hailstone(n/2) + 1
		else:
			return hailstone((3 * n) + 1) + 1

doctest.testmod()