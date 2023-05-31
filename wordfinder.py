from random import randint

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    
    def __init__(self, file):
        """Initializes WordFinder with a file and the list of words"""
        self.file = file
        self.words = self.get_word_list()        
        
    def get_word_list(self):
        """Reads file and returns a list of words"""
        with open(self.file, 'r') as file:
            lines = [line.strip() for line in file]
        print(f"{len(lines)} words read")
        return lines
        
    def random(self):
        """Returns a random word from list of words"""
        return self.words[randint(0, len(self.words)-1)]
    
    
WordFinder("words.txt")

        
        
            


        
