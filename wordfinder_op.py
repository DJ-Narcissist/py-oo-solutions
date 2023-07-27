import random
class WordReader:
    def __init__(self,file_path):
        self.file_path = file_path
        self.words = []
        self._read_words_file()

    def _read_words_file(self)
        with open(self.file_path, 'r') as file:
            self.words = [line.strip() for line in file]
        print(f"{len(self.words)} words read")

    def random(self):
        return random.choice(self.words)

        
class WordFinder:

    def __init__(self, file_path):
        self.words = self._read_words_file(file_path)

    def(_read_words_file)(self,file_path):
        with open(file_path,'r') as file:
            words = [line.strip() for line in file]
        print(f"{len(words)} words read")
        return words

    def random(self):
        return random.choice(self.words)

file_path ="/downloads/python-oo-practice/python-oo-practice/words.txt"
word_finder = WordFinder(file_path)
print(word_finder.random())
print(word_finder.random())