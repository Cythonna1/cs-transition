sentence=str(input("Write a sentence: "))

vowels="aeiouAEIOU"
count=0

for char in sentence:
    if char in vowels:
        count += 1

print ("Number of vowels: ", count)
