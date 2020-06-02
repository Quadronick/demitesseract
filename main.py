#!/usr/bin/env python
"""Module to play with a Kindle vocab.db file"""

import json
import sqlite3
import os.path
import random
import urllib

def db_output(db_name):
    """Recieve DB filename and return initial list of words"""
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
    """Recieve list and return list without duplicated elements"""
    return list(set(items))

def made_elements_lowercace(items):
    """Recieve list and return list with lowercased elements"""
    return list(map(str.lower, items))

def retrive_definition(item):
    """Recieve string and return definition from lexico.com"""
    url = "https://www.lexico.com/en/definition/" + item
    pass

def retrive_pronunciation(item):
    """Recieve string and return pronuciation from lexico.com"""
    pass

def open_json_dict():
    """"Recieve JSON file and return its content as dict"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'vocab.json')
    with open(db_path) as json_data:
        result = json.loads(json_data)
        json_data.close()
        return result

def save_json_dict(data):
    """Recieve list and save it as JSON file"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'vocab.json')
    with open(db_path, 'w+') as thing:
        json.dump(data, thing)

def list_to_empty_dict(data):
    """Recieve list of and return dict with empty keys"""
    return {i : "" for i in data}

initial_wordlist = db_output('vocab.db')
wordlist = made_elements_lowercace(initial_wordlist)
wordlist = remove_duplicates(wordlist)
wordlist.sort()

data = list_to_empty_dict(wordlist)

while True:
    word = (random.choice(list(data.keys())))
    print(word)
    breaker = input()
    if breaker == ':q':
        save_json_dict(data)
        break
    elif breaker == ':r':
        del data[word]
        
        
