from random import choice as Pick
from random import randint as Rand
from time import time as Time
from tkinter import W

def PhraseGen(Min = 8, Max = 15): # randomly generate "phrases"
    Alphabet = "abcdefghijklmnopqrstuvwxyz"
    Prompt = ""

    for i in range(Rand(Min, Max)): # loop for amount of words
        for _ in range(Rand(2, 9)): # loop for amount of characters in string
            Prompt += Pick(Alphabet) # add a char to the phrase
        
        Prompt += " " # add space between "words"

    return Prompt[: -1]

def FilePhraseGen(Min = 8, Max = 15): # randomly generate phrases from a a wordlist taken from a file
    with open('words.txt') as File:
        WordsList = [Word.strip() for Word in File.readlines() if 2 < len(Word.strip()) < 9] # extracting all the words from the words file
        WordsList = [Word for Word in WordsList if '.' not in Word] #filtering
        WordsList = [Word for Word in WordsList if '-' not in Word] #filtering
        WordsList = [Word for Word in WordsList if not any(Char.isdigit() for Char in Word)] #filtering

    Prompt = [Pick(WordsList) for i in range(Rand(Min, Max))] #generating the phrase
    
    return ' '.join(Prompt)

def TimeElapsed(Start = 0.0, End = 0.0): # compute elapsed time
    return round(End - Start, 2)

def Errors(Prompt = '', Input = ''): # compute errors from the prompt and the input
    return sum(a != b for a, b in zip(Input, Prompt))

def TypingSpeedWPM(Prompt = None, Input = '', DeltaTime = 0.0): # compute the WPM in the elapsed time
    AvgWordLength = sum([len(Word) for Word in Prompt]) // len(Prompt) # calculate the average char length rounding to int
    WPM = (len(Input) / AvgWordLength) - Errors(Prompt, Input) # remove the errors from the input
    MinuteTime = DeltaTime / 60 #convert seconds to minutes
    return WPM / MinuteTime

def PrintResult(WPM = 0.0, Time = 0.0, Mystypes = 0.0): # print the result
    print(f'WPM: {WPM}')
    print(f'Time: {Time}')
    print(f'Errors: {Mystypes}')

if __name__ == "__main__":
    print('-' * 100)
    Prompt = FilePhraseGen()
    print(f'Type this:\n{Prompt}')
    input('press ENTER when ready')

    Start = Time()
    Input = input()
    End = Time()

    Prompt = [Word for Word in Prompt.split(' ') if len(Word)]
    Input = [Word for Word in Input.split(' ') if len(Word) > 0]

    if len(Prompt) != len(Input):
        if len(Prompt) > len(Input):
            Input += ['*'] * abs(len(Prompt) - len(Input))
        else:
            Prompt += ['*'] * abs(len(Prompt) - len(Input))

    DeltaTime = TimeElapsed(Start, End)
    MistypeErrors = sum([Errors(WordPrompt, WordInput) for WordPrompt, WordInput in zip(Input, Prompt)])
    WPM = TypingSpeedWPM(Prompt, Input, DeltaTime)

    PrintResult(WPM, DeltaTime, MistypeErrors)

    print('-' * 100)
    input()