
def roman_to_interger(num):
    if num ==0:
        return "Cannot generate roman number for 0"
    rom_int = {1:'I',
                5:'V',
                10:'X',
                50:'L',
                100:'C',
                500:'D',
                1000:'M'}

    temp = []
    flag = False
    for key in reversed(rom_int.keys()):
        if key <= num and not flag:
            quo = num//key
            num = num % key
            temp_num = num
            for i in range(quo):
                if quo > 0:
                    temp.append(rom_int[key])
                    temp_num = temp_num//quo
                if temp_num == key:
                    temp.append(rom_int[key])
                    flag = True
                    break
        if num > 3 and key-1 == num and not flag:
            temp.append(rom_int[1] + rom_int[key])
            flag = True
    return ''.join(temp)


if __name__ == '__main__':
    try:
        inp = int(input("Please enter a number to convert integer to roman number"))
        print(f"{inp} ----- {roman_to_interger(inp)}")
    except:
        print("Please enter valid integer")
    

