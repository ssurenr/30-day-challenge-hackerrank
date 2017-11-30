def SplitByOddEven(word: str):
    even_letters, odd_letters = "", ""
    count = 0

    for letter in word:
        if count % 2 == 0:
            even_letters += letter
        else:
            odd_letters += letter
        count += 1

    return "{0} {1}".format(even_letters, odd_letters)


even_odd = []

cases = int(input())
for count in range(cases):
    string = input()
    even_odd.append(SplitByOddEven(string))

for item in even_odd:
    print(item)
