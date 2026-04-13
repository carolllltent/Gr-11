word = input("What is your word: ").lower()

def count_consonants(word): 
    count = 0 
    for letter in word: 
        if letter not in "aeiou":
            count += 1
    return(count)

result = count_consonants(word)
print(result)



        


