class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

import string

#  Read words in from the file, add to set of words

word_set = set() 

with open("words.txt", "r") as f:
    for word in f:
        word_set.add(word.strip().lower())


def get_neighbors(word):
    neighbors = []

    word_letters = list(word)
    for i in range(len(word_letters)):
        
        for letter in list(string.ascii_lowercase): #['a', 'b', 'c', ...etc]
            # make a copy of the word
            temp_word = list(word_letters)

            # substitute the letter into the word copy
            temp_word[i] = letter

            # turn the word list back into a string
            temp_word_str = "".join(temp_word)

            # if temp_word_str is a real word,
            # and it's not the same as word (because if we loop over each
            # character of the alphabet, we'll eventually replace the letters
            # in the temp_word with the same letters from the list of letters)
            # add it to the return set
            if temp_word_str != word and temp_word_str in word_set:
                neighbors.append(temp_word_str)

    return neighbors            


def find_word_ladder(begin_word, end_word):
    visited = set()
    q = Queue()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v == end_word:
                return path

            for neighbor in get_neighbors(v):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)

    return None                

print(find_word_ladder("sail", "boat"))