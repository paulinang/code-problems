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
    # if stack is empty and bank1 is empty but bank2 is not
    # elif not stack and not bank1 and bank2:
    #     return
    # if
    # elif not stack and not bank2 and bank1:
    #     return

    if not stack and bank1:
        return add_paran(combo + '(', bank1[1:], bank2, stack + ['('])

    if stack and bank2:
        return add_paran(combo + ')', bank1, bank2[1:], stack[1:])
