from random import choice as Pick
from random import randint as Rand
from time import time as Time
from tkinter import W

def PhraseGen(): # randomly generate "phrases"
    Alphabet = "abcdefghijklmnopqrstuvwxyz"
    Prompt = ""

    for i in range(Rand(8, 15)): # loop for amount of words
        for _ in range(Rand(2, 9)): # loop for amount of characters in string
            Prompt += Pick(Alphabet) # add a char to the phrase
        
        Prompt += " " # add space between "words"

    return Prompt[: -1]

def TimeElapsed(Start = 0.0, End = 0.0): # compute elapsed time
    return round(End - Start, 2)

def Errors(Prompt = '', Input = ''): # compute errors from the prompt and the input
    return sum(a != b for a, b in zip(Input, Prompt))

def TypingSpeedWPM(Prompt = '', Input = '', DeltaTime = 0.0): # compute the WPM in the elapsed time
    AvgWordLength = sum([len(Word) for Word in Prompt.split(' ')]) // len(Prompt.split(' ')) # calculate the average char length rounding to int
    WPM = (len(Input) / AvgWordLength) - Errors(Prompt, Input) # remove the errors from the input
    MinuteTime = DeltaTime / 60 #convert seconds to minutes
    return WPM / MinuteTime

def PrintResult(WPM = 0.0, Time = 0.0, Mystypes = 0.0): # print the result
    print(f'WPM: {WPM}')
    print(f'Time: {Time}')
    print(f'Errors: {Mystypes}')

if __name__ == "__main__":
    print('-' * 80)
    Prompt = PhraseGen()
    print(f'Type this:\n{Prompt}')
    input('press ENTER when ready')

    Start = Time()
    Input = input()
    End = Time()

    if len(Input) > len(Prompt):
        Prompt += '-' * (len(Input) - len(Prompt))
    if len(Input) < len(Prompt):
        Input += '-' * (len(Prompt) - len(Input))

    DeltaTime = TimeElapsed(Start, End)
    MistypeErrors = Errors(Prompt, Input)
    WPM = TypingSpeedWPM(Prompt, Input, DeltaTime)

    PrintResult(WPM, DeltaTime, MistypeErrors)

    print('-' * 80)
    input()