# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    file = open(filename, 'r')
    story = file.read()
    return story

def count_words():
    text = read_file_content("readingTextFiles\story.txt")
    words = text.split()
    unique_words = set(words)
    dictionary = {}
    for word in unique_words:
        dictionary.update({word: words.count(word)})
    
    return dictionary

print(count_words())