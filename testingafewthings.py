'''
Keras is a neural network library (tensorflow derivative) that is used for the Siamese Network in the code.
Numpy is a Linear Algebra library, but all I'm using is the array tool for compatibility with tensorflow
'''
from keras.models import Sequential
from keras.layers import Dense, Dropout
import numpy as np
import string

# Remove these with the title, and what the user inputs
str_to_compare = input()
str2_to_compare = input()

word1 = str_to_compare.split(' ')
word2 = str2_to_compare.split(' ')


alphabets = list(string.ascii_lowercase)

'''
Convert phrase (that is converted to a list) into a list where each word is an array of arrays (with length being the length of word), and letter is depicted as a list of 26 with all values being 0 except one, which indicates the current letter
'''


def encode_string(phrase: list) -> list:
    encoded_list = [[[0 for _ in range(len(alphabets))] for word in phrase for _ in word] for _ in range(len(phrase))]
    for i, word in enumerate(phrase):
        for j, letter in enumerate(''.join([c.lower() for c in word.lower() if c.isalpha()])):
            encoded_list[i][j][alphabets.index(letter)] = 1

    return encoded_list

'''
Similarity score. Simply just the sum of the encodings squared. If the value is less than 1, the two phrases are similar, otherwise they're not.
'''


def return_score(s1: list, s2: list) -> bool:
    s1_score = 0
    s2_score = 0
    for i, arr in enumerate(s1[0]):
        s1_score += sum(arr)
    for i, arr in enumerate(s2[0]):
        s2_score += sum(arr)
    score = sum((s1_score - s2_score)**2)
    print(score)
    if score <= 1:
        return True
    else: return False
    # return (sum(s1[0]) - sum(s2[0]))**2


dict_of_words = list(set(word1))
'''
With the two strings above, convert letters to ints using the encode_string function above to predict. 
'''
word1_decoded = np.array([encode_string(word1)])
word2_decoded = np.array([encode_string(word2)])
print(word1_decoded)
'''
Siamese network architecture is below. 4 dense layers and 1 dropout layer, with the architecture outputting 32 encodings to be used in the similarity function. 
'''
model = Sequential()
model.add(Dense(64, input_shape=word1_decoded.shape, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(16, activation='relu'))
# model.add(Dropout(0.3))
model.add(Dense(32, activation='relu'))
# model.compile(loss='mse', optimizer='adam')
# for i in range(50):
'''
Predict the two strings, and calculate the similarity of the encodings
'''
p = model.predict(word1_decoded)
p2 = model.predict(word2_decoded)
print(return_score(p, p2))

