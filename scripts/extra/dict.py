#!/usr/bin/env python3

import os 
import subprocess
import datetime
import csv

file_path = "~/.config/hypr/scripts/extra/storage/dict_searches.csv"
# file_path = "~/dict_searches.csv"
file_path = os.path.expanduser(file_path)

def createFileIfNot(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w"):
            pass


def showWord(text):
    '''
    return word being searched
    '''
    command = f'''echo "{text}" | wofi --show dmenu'''
    return subprocess.getoutput(command)

def getWord():
    createFileIfNot(file_path)
    word_string = ""
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        csv_reader = list(csv_reader)
        csv_reader.reverse()
        for row in csv_reader:
            word_string += '|'.join(row) + '\n'
    word_string = word_string.rstrip("\n")
    return word_string

def saveNewWordToFile(word):
    createFileIfNot(file_path)
    # Regard string with spaces empty
    if word.strip():
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if word in row[1]:
                    return
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, word])


def showGoldenDict(word):
    cmdDict = f'''goldendict "{word}"'''
    cmdWofi = cmdDict
    subprocess.getoutput(cmdWofi)
    
if __name__ == "__main__":
    word = showWord(getWord())
    if word.strip():
        if "|" in word:
            word = word.split("|")[1].strip()
        showGoldenDict(word)
        saveNewWordToFile(word)






