import os

from playsound import playsound

Title = '\n' + '【 Python Media Player 】' + '\n'

print(Title)

print('----------------------------' + '\n')

def EnterDirectory():

    print(' Enter the Music Directory' + '\n')

    SoundDirectory = input(' ＞ ')

    Log = ' Still Playing ...'
    print('\n' + Log)

    playsound(SoundDirectory)

    print('')

    EnterDirectory()

EnterDirectory()