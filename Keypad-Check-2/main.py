
def lister(string):
    lst = []
    for c in string:
        lst.append(c)
    return lst


def delister(lst):
    string1 = ''
    for e in lst:
        string1 = string1 + e
    return string1


def deint(lst):
    outlist = []
    for i in lst:
        p = str(i)
        outlist.append(p)
    return outlist


def recAdder(code, clist, length, cUsed, percentCarry):
    percentCarry
    if len(clist) - cUsed > length - len(code):
        return []
    outputlst = []
    if len(code) == length:
        if cUsed == len(clist):
            outputlst.append(code)
        return (outputlst)
    else:
        for cIndex in range(len(clist)):
            c = clist[cIndex]
            g = 1 / len(clist)
            percentCarry = percentCarry.copy()
            if len(code) == 0:
                percentCarry[0] = c
            if len(code) == 1:
                percentCarry[1] = c
            if len(code) == 2:
                percentCarry[2] = c
                lev1 = float(percentCarry[0]) * g
                lev2 = float(percentCarry[1]) * g**2
                lev3 = float(percentCarry[2]) * g**3
                percentDone = round(100 * (lev1 + lev2 + lev3), 1)
                print('Creating List:', percentDone, '%')
          
            for i in range(len(code) + 1):
                cUsedIncrease = False
                if c not in code:
                    cUsedIncrease = True

                doit = False
                if i == 0:
                    doit = True
                else:
                    if c == code[i - 1]:
                        doit = False
                    else:
                        if i > 0 and int(code[i - 1]) > int(c):
                            doit = False
                        if i < len(code) and int(code[i]) > int(c):
                            doit = False
                if doit == True:
                    tempcode = lister(code)
                    tempcode.insert(i, c)
                    if cUsedIncrease == True:
                        increase = 1
                    else:
                        increase = 0
                    outputlst += recAdder(delister(tempcode), clist, length,
                                          cUsed + increase, percentCarry)

    return outputlst


def run():
    alls = deint([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    length = int(input('PIN Length: '))
    choice = input(
        'Enter number of keys used, or enter \'c\' to choose specific keys: ')
    if choice == 'c':
        characters = lister(int(input('Enter the keys, without separation: ')))
    else:
        count = int(choice)
        characters = alls[:count]
    emptyCode = ''
    used = 0
    finalList = recAdder(emptyCode, characters, length, used, [0, 0, 0])
    print('Creating List: ', 100, '%')
    print('-----------------------------------------------')
    print('Number of possible PINs: ', len(finalList))
    g = input('press 1 for list:')
    if g == '1':
        print(finalList)
    

def main():
    d = 'go'
    while d != 'q':
        run()
        d = input('type \'q\' to quit.')
main()


