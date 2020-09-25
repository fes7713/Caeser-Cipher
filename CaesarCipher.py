import random

def CaesarCipher(sentence, key):  # input string / output array
    scrambled = []
    for i in range(0, len(sentence)):
        scrambled.append(chr(ord(sentence[i]) + key))
    return scrambled


#alt fxn
def CaesarCipher(sentence, key):
    encrypted = ""
    for i in range(len(sentence)):
        char = sentence[i]
        encrypted += chr((ord(char) + key - 32) % 95 + 32) #ASCII charactors from 32 (Space) to 127 (Delete) 95 charactors

    return encrypted


def print_new_str(scrambled):  # input array / output print(string)
    for i in range(0, len(scrambled)):
        print(scrambled[i], end="")


def fixScramble(scrambled, key):  # input string / output array
    sentence = []
    for i in range(0, len(scrambled)):
        sentence.append(chr(ord(scrambled[i]) - key))
    return sentence


########################## MAIN
type = int(input("Scramble Data : 1, Unscramble Data : 2"))

if type == 1:
    sentence = input("Scrambling Sentence : Type Sentence : ")
    ran_scrambling = random.randrange(26)
    print("your key: ", ran_scrambling)
    scrambled_sentence = CaesarCipher(sentence, ran_scrambling)
    print_new_str(scrambled_sentence)
elif type == 2:
    sentence = input("Unscrambling Sentence : Type Sentence : ")
    key = int(input("Type Key"))
    fixed_Sentence = fixScramble(sentence, key)
    print_new_str(fixed_Sentence)
else:
    print("Invalid Input")

