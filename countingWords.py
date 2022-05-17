word = input("Enter a word to know the length: ")
countedWord = len(word)
print("The length of the word is: ", countedWord)

# I wasn't sure the question was asking for the length
# of the word or the number of words in a sentence, so I did both

text = input('Enter a text:')
countedText = len(text.split())
print("There are " + str(countedText) + " words in this text.")