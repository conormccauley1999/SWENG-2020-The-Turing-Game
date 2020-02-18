# Class worked on by: Claire, Diego, Kishore, Leo
import re
from word2number import w2n
from string import digits
#from keras.preprocessing.text import text_to_word_sequence

class DataPreProcessor:
    input = 0
    # Creates an instance of the preprocessor with input being input from commandline passed to it from main class.
    def __init__(self, input):
        self.input = input

    # Processes the input.
    def processInput(self):
        self.convertAccentedCharsToAscii()
        self.removeNumbers()
        self.convertNumberWordToDigit()
        #self.input = text_to_word_sequence(self.input)
        return

    # Change accented characters eg. é to e. - Diego
    def convertAccentedCharsToAscii(self):
        self.input = re.sub(r'[àáâãäåæÀÁÂÃÄÅÆ]', 'a', self.input)
        self.input = re.sub(r'[èéêëÈÉÊË]', 'e', self.input)
        self.input = re.sub(r'[ìíîïÌÍÎÏ]', 'i', self.input)
        self.input = re.sub(r'[òóôõöðøōŏőÒÓÔÕÖØŌŎŐ]', 'o', self.input)
        self.input = re.sub(r'[ùúûüũūŭůűųÙÚÛÜŨŪŬŮŰŲ]', 'u', self.input)
        self.input = re.sub(r'[ýÿŷÝŸ]', 'y', self.input)
        self.input = re.sub(r'[^A-Za-z0-9]+', '_', self.input)
        return

    # Convert one to 1. - Kishore
    def convertNumberWordToDigit(self):
        try:
            self.input = w2n.word_to_num(self.input)
        except Exception as e:
            print(e)    
        return 

    # Remove all numeric characters. - Kishore
    def removeNumbers(self):
        self.input = ''.join([i for i in self.input if not i.isdigit()])
        self.input = (self.input).replace("_", " ")
        return 

    # Resolve words that have a '_' character
    # ie. if "h3llo" is passed through convertAccentedCharsToAscii(), it becomes "h_llo"
    # try to dictionary match the string to a word that will fit, and return that
    def resolveUnderscores(self):
        return

    # Just an idea, perhaps it would be outside of scope or too hard
    def resolveMisspellings(self):
        return
