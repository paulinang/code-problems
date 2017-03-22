# Hamming distance between two integers
def hamming_dist(a, b):
    """ # positions at which corresponding bits are different """

    # convert both ints to binary
    small_bin = int2bin(min(a, b))
    big_bin = int2bin(max(a, b))

    # compare each corresponding digit, incrementing a counter
    big_len = len(big_bin)
    dist = 0
    for i in range(big_len - 1, -1, -1):
        if i >= len(small_bin):
            if big_bin[i] != 0:
                dist += 1
        elif big_bin[i] != small_bin[i]:
            dist += 1

    return dist


def int2bin(num):
    """ Convert integer to binary string"""

    if num == 0:
        return '0'

    bin_str = ''
    while num:
        if num & 1 == 1:
            bin_str = '1' + bin_str
        else:
            bin_str = '0' + bin_str

        num /= 2

    return bin_str


# Number complement
def find_complement(num):

    num_s = int2bin(num).lstrip('1')
    comp = 0

    for i in range(len(num_s)):
        if num_s[i] == '0':
            comp += 2 ^ i

    return comp
