import re

#define the dictionary
code = {'a': '00', 
'b': '01',
'c': '10',
'd': '1100',
'e': '1101',
'f': '1110',
'g': '111100',
'h': '111101',
'i': '111110',
'j': '1111110000',
'k': '1111110001',
'l': '1111110010',
'm': '1111110011',
'n': '1111110100',
'o': '1111110101',
'p': '1111110110',
'q': '1111110111',
'r': '1111111000',
's': '1111111001',
't': '1111111010',
'u': '1111111011',
'v': '1111111100',
'w': '1111111101',
'x': '1111111110',
'y': '1111111111',
'z': '11111111110000',
' ': '11111111110001'}

encoded_instruction = """1111101111111111000111111100101111110101111111110011011111111111000100111111010
0111100110111111100101111010010111111000111111111110001101111110101110011011111
1111110001101111010011111100101111110010110111111101001111001101111111111100010
11101100011111110111111111001110111111111110001111110111111101011111111110001111
11011111110011111111111000111101111111011111111010011111111110001001111110100110
01111111111000111011111111110101111101111111010111110111111010011110011111111110
00100111111010011001111111111000111111011111111110001110011111011111110011111110
01011111011111100011101111111111100011111111010111101110111111111110001111111110
11111110101111111100011001111111111000111111111110001111111111100011111111010111
1010011111110101111111111000100111111011011111101101101001111111000111111100111
11111111000111111011111101001111111111000111111110101111011101111111111100011111
11011011110111111110000011111110011101"""

#define find and replace
def fnr(encd, cd):
    twos = []
    fours = []
    six = []
    tens = []
    fteens = []
    sp = cd[" "]
    nencd = encd.replace(sp," ")
    chunks = nencd.split(" ")
    #chunks = encd.split(" ")
    for i in cd:
        if len(cd[i]) == 2:
            twos.append(cd[i])
        elif len(cd[i]) == 4:
            fours.append(cd[i])
        elif len(cd[i]) == 6:
            six.append(cd[i])
        elif len(cd[i]) == 10:
            tens.append(cd[i])
        elif len(cd[i]) == 14:
            fteens.append(cd[i])
    chk = []
    chk.append(chunks[0])
    chk.append(chunks[1])
    chk.append(chunks[2])
    #print("{} chunck".format(chunks[2]))
    for j in chunks:
        word = ""
        todecode = j
        while len(todecode)>0:
            #print("todecode: {}".format(todecode))
            if len(todecode) >= 14:
                letter = todecode[0:14]
                e_letter = find14(letter, cd, fteens)
                if e_letter == "not":
                    letter1 = todecode[0:10]
                    e_letter1 = find10(letter1, cd, tens)
                    if e_letter1 == "not":
                        letter2 = todecode[0:6]
                        e_letter2 = find6(letter2, cd, six)
                        if e_letter2 == "not":
                            letter3 = todecode[0:4]
                            e_letter3 = find4(letter3, cd, fours)
                            if e_letter3 == "not":
                                letter4 = todecode[0:2]
                                e_letter4 = find2(letter4, cd, twos)
                                if e_letter4 == "not":
                                    print("{} not found". format(letter4))
                                    break
                                else:
                                    word += e_letter4
                                    todecode = todecode[2:]
                            else:
                                word += e_letter3
                                todecode = todecode[4:]
                        else:
                            word += e_letter2
                            todecode = todecode[6:]
                    else:
                        word += e_letter1
                        todecode = todecode[10:]
                else:
                    word += e_letter
                    todecode = todecode[14:]
            elif len(todecode) >= 10:
                letter1 = todecode[0:10]
                e_letter1 = find10(letter1, cd, tens)
                if e_letter1 == "not":
                    letter2 = todecode[0:6]
                    e_letter2 = find6(letter2, cd, six)
                    if e_letter2 == "not":
                        letter3 = todecode[0:4]
                        e_letter3 = find4(letter3, cd, fours)
                        if e_letter3 == "not":
                            letter4 = todecode[0:2]
                            e_letter4 = find2(letter4, cd, twos)
                            if e_letter4 == "not":
                                print("{} not found". format(letter4))
                                break
                            else:
                                word += e_letter4
                                todecode = todecode[2:]
                        else:
                            word += e_letter3
                            todecode = todecode[4:]
                    else:
                        word += e_letter2
                        todecode = todecode[6:]
                else:
                    word += e_letter1
                    todecode = todecode[10:]
            elif len(todecode) >= 6:
                letter2 = todecode[0:6]
                e_letter2 = find6(letter2, cd, six)
                if e_letter2 == "not":
                    letter3 = todecode[0:4]
                    e_letter3 = find4(letter3, cd, fours)
                    if e_letter3 == "not":
                        letter4 = todecode[0:2]
                        e_letter4 = find2(letter4, cd, twos)
                        if e_letter4 == "not":
                            print("{} not found". format(letter4))
                            break
                        else:
                            word += e_letter4
                            todecode = todecode[2:]
                    else:
                        word += e_letter3
                        todecode = todecode[4:]
                else:
                    word += e_letter2
                    todecode = todecode[6:]
            elif len(todecode) >= 4:
                letter3 = todecode[0:4]
                e_letter3 = find4(letter3, cd, fours)
                if e_letter3 == "not":
                    letter4 = todecode[0:2]
                    e_letter4 = find2(letter4, cd, twos)
                    if e_letter4 == "not":
                        print("{} not found". format(letter4))
                        break
                    else:
                        word += e_letter4
                        todecode = todecode[2:]
                else:
                    word += e_letter3
                    todecode = todecode[4:]
            elif len(todecode) >= 2:
                letter4 = todecode[0:2]
                e_letter4 = find2(letter4, cd, twos)
                if e_letter4 == "not":
                    print("{} not found". format(letter4))
                    break
                else:
                    word += e_letter4
                    todecode = todecode[2:]

        print(word)

def find14(letter, cd, fteens):
    e_letter = "not"
    for k in fteens:
        if k == letter:
            for key, value in cd.items():
                if letter == value:
                    e_letter = key
                    break
            break
    if e_letter == "not":
        return "not"
    else:
        return e_letter
    
def find10(letter, cd, tens):
    e_letter = "not"
    for k in tens:
        if k == letter:
            for key, value in cd.items():
                if letter == value:
                    e_letter = key
                    break
            break
    if e_letter == "not":
        return "not"
    else:
        return e_letter
    
def find6(letter, cd, six):
    e_letter = "not"
    for k in six:
        if k == letter:
            for key, value in cd.items():
                if letter == value:
                    e_letter = key
                    break
            break
    if e_letter == "not":
        return "not"
    else:
        return e_letter
    
def find4(letter, cd, fours):
    e_letter = "not"
    for k in fours:
        if k == letter:
            for key, value in cd.items():
                if letter == value:
                    e_letter = key
                    break
            break
    if e_letter == "not":
        return "not"
    else:
        return e_letter

def find2(letter, cd, twos):
    e_letter = "not"
    for k in twos:
        if k == letter:
            for key, value in cd.items():
                if letter == value:
                    e_letter = key
                    break
            break
    if e_letter == "not":
        return "not"
    else:
        return e_letter


fnr(encoded_instruction, code)