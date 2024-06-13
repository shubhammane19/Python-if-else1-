char  = input("Enter Character: ")

if(len(char) == 1 and (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u')):
    print(char , end  = " is an vowel ")
elif(len(char) == 1 and ('a' <= char <= 'z') and (char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u')):
    print(char, end = " is a consonant ")
else:
    print(char, end = " is special char ")