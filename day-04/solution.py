#to Count the vowels in a string

word = "Hello Python"
vowels = "AEIOUaeiou"
count = 0

for char in word:
    if char in vowels:
        count+=1

print(count)

    
    
