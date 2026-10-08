def _1(l):
    return [m.upper() + "!" for m in l]

def _2(l):
    return [m.capitalize() for m in l]

def _3():
    return [0 for x in range(10)]

def _4(l):
    return [x * 2 for x in l]

def _5(l):
    return [int(x) for x in l]

def _7(l):
    return [len(x) for x in l.split()]

def _8(l):
    return [x[0] for x in l.split()]

def _9(l):
    return [(x,len(x)) for x in l.split()]

def _10():
    return [x for x in range(0,10,2)]

def _11():
    return [x**2 for x in range(20) if x**2 % 2 == 0]

def _12():
    return [x**2 for x in range(20) if str(x**2)[-1] == '4']

def _13():
    return "".join([chr(x) for x in range(65,91)])

def _14(l):
    return [x.strip() for x in l]

def _15(l):
    return "".join([str(x) for x in l])

def main():
    l = ['auto', 'villamos', 'metro']
    print("1:", _1(l))
    l = ['aladar', 'bela', 'cecil']
    print("2:", _2(l))
    print("3:", _3())
    l = list(range(1,11))
    print("4:", _4(l))
    l = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    print("5:", _5(l))
    l = "1234567"
    print("6:", _5(l))
    l = 'The quick brown fox jumps over the lazy dog'
    print("7:", _7(l))
    l = "python is an awesome language"
    print("8:", _8(l))
    l = 'The quick brown fox jumps over the lazy dog'
    print("9:", _9(l))
    print("10:", _10())
    print("11:", _11())
    print("12:", _12())
    print("13:", _13())
    l = [' apple ', ' banana ', ' kiwi']
    print("14:", _14(l))
    l = [1, 0, 1, 1, 0, 1, 0, 0]
    print("15:", _15(l))
    print(type(_15(l)))

if __name__ == "__main__":
    main()