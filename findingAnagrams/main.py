# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    return sorted(word) == sorted(anagram)

word = str(input("Enter a word: "))
anagram = str(input("Enter an anagram: "))

print(find_anagram(word, anagram))
