'''
Print entire character stream in reverse 
hello world 
olleh dlrow
'''


def reverseWordSentence(Sentence): 

    # Spliting the Sentence into list of words. 
    words = Sentence.split(" ") 
    
    # Reversing each word and creating a new list of words 
    # List Comprehension Technique 
    newWords = [word[::-1] for word in words] 
    
    # Joining the new list of words to for a new Sentence 
    newSentence = " ".join(newWords) 

    return newSentence 

# Driver's Code 
Sentence = input('Enter String: ')
# Calling the reverseWordSentence 
# Function to get the newSentence 
print(reverseWordSentence(Sentence))