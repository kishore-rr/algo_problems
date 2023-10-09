def romanToInt(s: str) -> int:
    int_rom = {'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000}
    temp = 0
    int_keys = list(int_rom.keys())
    s = s.upper()
    for chr in s:
        if chr not in int_keys:
            return "Please pass the valid Roman characters"
    prev = ""
    for n, i in enumerate(s):
        if n!=0:
            if int_keys.index(prev) < int_keys.index(i):
                temp -= int_rom[prev]*2
        temp+=int_rom[i]
        prev = i
    return temp


if __name__ == '__main__':
    try:
        inp = input("Please enter a number to convert roman number to Integer: ")
        print(f"{inp} ----->> {romanToInt(inp)}")
    except:
        print("Please enter valid integer")
    

