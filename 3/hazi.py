

def palindrome(a):
    return a == a[::-1]

def fordit(a):
    return int(str(a)[::-1])






def main():
    print(palindrome("görög"))
    print(palindrome("test"))
    print(fordit(1977))
    print(len(str(2**256)))

    pass

if __name__ == "__main__":
    main()