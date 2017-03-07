def balance_paran(n):
    bank1 = ['('] * n
    bank2 = [')'] * n
    stack = []
    combo = ''
    return add_paran(combo, bank1, bank2, stack)


def add_paran(combo='', bank1=[], bank2=[], stack=[]):
    print 'combo' + str(combo)
    print 'bank1' + str(bank1)
    print 'bank2' + str(bank2)
    print 'stack' + str(stack)
    # if all are empty
    if not stack and not bank1 and not bank2:
        return combo

    if not stack and bank1:
        # all parantheses balanced so far, can only add open
        return add_paran(combo + '(', bank1[1:], bank2, stack + ['('])

    if stack:
        # there are parantheses to close
        if not bank1:
            # there are no more open parantheses
            return add_paran(combo + ')', bank1, bank2[1:], stack[1:])

        return [add_paran(combo + '(', bank1[1:], bank2, stack + ['(']),
                add_paran(combo + ')', bank1, bank2[1:], stack[1:])]
