chinese = "杯桵湩歬㈰㈳筎ㅣ敟剥癥牳ㅮ杽"

flag_lol = ""

for i in range(0, len(chinese)):
    
    combine = ord(chinese[i])

    
    first_letter = chr((combine >> 8) & 0xFF)

    second_letter = chr(combine & 0xFF)

    
    flag_lol += first_letter + second_letter

print(flag_lol)