def get_most_common_letter(text):
    counter = {}
    for char in text:
        print(text)
        counter[char] = counter.get(char, 0) + 1
        print(char)
        print(counter[char])
    letter = sorted(counter.items(), key=lambda item: item[1])[10][0]
    print(sorted(counter.items()))
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")