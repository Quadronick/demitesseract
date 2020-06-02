#!/usr/bin/env python
"""Module to play with Kindle vocab.db file"""

import sqlite3
import os.path
import random

def db_output(db_name):
    """Get DB filename and return initial list of words"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, db_name)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM WORDS")
    raw_list = cursor.fetchall()
    result = list()
    for element in raw_list:
        result.append(element[1])
    return result

def remove_duplicates(items):
    """Just takes list and uses set() to remove duplicates"""
    return list(set(items))

def made_elements_lowercace(items):
    """Just takes list and made every it element lowercase"""
    return list(map(str.lower, items))

def retrive_definition(item):
    pass

def retrive_pronunciation(item):
    pass

def open_json_dict(filename):
    pass

def save_json_dict(data):
    pass

initial_wordlist = db_output('vocab.db')
wordlist = made_elements_lowercace(initial_wordlist)
wordlist = remove_duplicates(wordlist)
wordlist.sort()

while True:
    print(wordlist[random.randrange(len(wordlist))])
    breaker = input()
    if breaker == '.':
        break
