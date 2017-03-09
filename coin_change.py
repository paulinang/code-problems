# Compute number of combinations to make an amount given a list of coins
# [1, 2, 3] -> amount 5
# [1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 3], [1, 2, 2s], [2, 3] -> 5 ways
# Think of it as a matrix
#   Ones to 5: 0, 1, 2, 3, 4, 5
# Coins:    1  1, 1, 1, 1, 1, 1    each number is ways to make amount 1, given coin 1
#           2  1, 1, 2, 2, 3, 3
#           3  1, 1, 2, 3, 4, 5

#              only 1 way to make 0 amount for all coins
# Coin 2: jump to column with amount = coin
# column 0 and 1 carry over from row 1
# amount 2 - coin 2 = 0 -> [row 1, column 2] + [row 2, column 0] = 1 + 1 = 2
# amount 3 - coin 2 = 1 -> [row 1, column 3] + [row 2, column 1] = 1 + 1 = 2
# amount 4 - coin 2 = 2 -> [row 1, column 4] + [row 2, column 2] = 1 + 2 = 3
# amount 5 - coin 2 = 3 -> [row 1, column 5] + [row 2, column 3] = 1 + 2 = 3
# adds ways to make amount, with previous coin amount 1
# with ways to make left over amount from amount - current coin using current coin

# Coin 3: column 0, 1, 2 carry over from row 2 : 1, 1, 2
# amount 3 - coin 3 = 0 -> [r 2, c 3] + [r 3, c 0] = 2 + 1 = 3
# amount 4 - coin 3 = 1 -> [r 2, c 4] + [r 3, c 1] = 3 + 1 = 4
# amount 5 - coin 3 = 2 -> [r 2, c 5] + [r 3, c 2] = 3 + 2 = 5

# n combos = 5


def n_coin_combos(coins, amount):
    # create row with amount + 1 'columns'
    row = [0] * (amount + 1)
    row[0] = 1
    for i in coins:
        for j in range(1, amount + 1):
            # can start range at 1, because ways to make 0 is always 1
            if j >= i:
                # once you hit an amount that = coin value
                row[j] += row[j - i]
                # can add ways to make amount j with amount to make amount - coin value

    return row[amount]

# with another example coin [2, 3] amount 6
# row = [1, 0, 0, 0, 0, 0, 0]
# when amount = 2, add ways to make 0 to ways to make 2 using coin 2
# row = [1, 0, 1 + 0, 0, 0, 0, 0]
# amount = 3, ways to make 3 - 2 = 1 with coin 2
# row = [1, 0, 1, 0 + 0, 0, 0, 0]
# amount = 4, ways to make 4 - 2 = 2 with coin 2
# row = [1, 0, 1, 0, 0 + 1, 0, 0]
# amount = 5
# row = [1, 0, 1, 0, 1, 0 + 0, 1]
# amount = 6
# row = [1, 0, 1, 0, 1, 0, 1 + 0]

# coin 3 and row = [1, 0, 1, 0, 1, 0, 1]
# amount = 3
# row = [1, 0, 1, 0 + 1, 1, 0, 1]
# amount = 4
# row = [1, 0, 1, 1, 1 + 0, 0, 1]
# amount = 5
# row = [1, 0, 1, 1, 1, 0 + 1, 1]
# amount = 6
# row = [1, 0, 1, 1, 1, 1, 1 + 1]

# row[6] = 2
