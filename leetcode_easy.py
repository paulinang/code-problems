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


# Find keyboard row words
def find_keyboard_words(words):

    row1 = set('qwertyuiop')
    row2 = set('asdfghjkl')
    row3 = set('zxcvbnm')

    keyboard_words = []
    for word in words:
        if word[0] in row1:
            if not (set(word) & row2) or not (set(word) & row3):
                keyboard_words.append(word)
        elif word[0] in row2:
            if not (set(word) & row1) or not (set(word) & row3):
                keyboard_words.append(word)
        else:
            if not (set(word) & row2) or not (set(word) & row1):
                keyboard_words.append(word)

    return keyboard_words


# Fizz for multiples of 3, buzz for multiples of 5, fizzbuzz for both
def fizzbuzz(num):

    result = []
    for i in range(1, num + 1):
        s = ''
        if i % 3 == 0:
            s = 'Fizz'
        if i % 5 == 0:
            s += 'Buzz'

        result.append(s or str(i))

    return result
