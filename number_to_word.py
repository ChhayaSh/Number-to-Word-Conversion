def typeofstring(n):
    try:
        a = float(n)
        if a%int(a) == 0:
            return("int")
        else:
            return("float")
    except:
        return("string")

def num_to_word(smallnum, suff_ind):
    # First lets define major lists which we will be needing in naming the number
    ones = ["", "one", "two", "three","four", "five", "six", "seven","eight","nine"]
    twos = [ "ten", "eleven", "twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens = [ "twenty", "thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    suffix = ["", "thousand", "million", "billion"]

    if len(smallnum) > 3:
        return('Error while giving small parts of number')
    else:
        output = []
        if len(smallnum) == 1:
            output.append(ones[int(smallnum)])
        elif len(smallnum) == 2:
            if smallnum[0] == "1":
                output.append(twos[int(smallnum)%10])
            else:
                output.append(tens[int(smallnum[0]) - 2])
                output.append(ones[int(smallnum[1])])
        else:
            output.append(ones[int(smallnum[0])])
            if smallnum[0] != "0":
                output.append("hundred")
            if smallnum[1] == "1":
                output.append(twos[int(smallnum[1:3])%10])
            elif smallnum[1] == "0":
                output.append(ones[int(smallnum[2])])
            else:
                output.append(tens[int(smallnum[1]) - 2])
                output.append(ones[int(smallnum[2])])
        output.append(suffix[suff_ind-1])
        final = (" ".join(elem for elem in output))
        return(final)

def convert_word(n):

    #Dividing the number into parts of three
    wordlist = []
    i = 0
    if len(n)%3 == 0:
        count = len(n)//3
    else:
        count = len(n)//3+1
        b = len(n)%3
        wordlist.append(num_to_word(n[i:b], count))
        i = b
        count -= 1

    while count>0:
        wordlist.append(num_to_word(n[i:i+3], count))
        i = i+3
        count -= 1

    return(" ".join(words for words in wordlist))

def convert_decimal(n):
    ones = ["zero", "one", "two", "three","four", "five", "six", "seven","eight","nine"]
    #Dividing the number into parts of three
    wordlist = []

    for elem in list(n):
        wordlist.append(ones[int(elem)])

    return(" ".join(words for words in wordlist))


#Taking input
number = input("Please give your input here : ")

#Now checking if the given string is number or not
if len(number) == 0:
    print("You did not give any number")
elif typeofstring(number) == "string":
    print("It's not a number")
else:
    if typeofstring(number) == "int":
        if len(number) > 12:
            print("I only work for 12 digit numbers")
        else:
            print(convert_word(number))
    else:
        a, b = map(str, number.split("."))
        first = convert_word(a)
        second = convert_decimal(b)
        print(first+"point "+second)
