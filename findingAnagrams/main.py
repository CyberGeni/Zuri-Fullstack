# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


### def find_anagram(word, anagram):
#    if (sorted(word) == sorted(anagram)):
 #       return True
 #   else:
  #      return False
#
#word = 
#anagram = )
#find_anagram(word, anagram) 


def check(s1, s2):
    # the sorted strings are checked
    if(sorted(s1)== sorted(s2)):
        return True
    else:
        return False    
         
# driver code 
s1 = str(input('Enter the word: '))
s2 = str(input('Enter the anagram: '))
check(s1, s2)