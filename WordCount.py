import re
import sys
import nltk
import os
from collections import Counter
import pprint

reload(sys)
sys.setdefaultencoding('utf8')

def word_count(filename, lemmatized = False):
    try:
        file = open(filename, "rb")
        text = file.read()
        file.close()
    except:
        return 

    # Ignore hypen or apostrophe? What if apostrophe used as quotation marks?
    word_array = re.split('[^\w\-\']', text.lower())

    if lemmatized:
        lemma = nltk.wordnet.WordNetLemmatizer()
        word_array = [lemma.lemmatize(a, pos = 'v') if lemma.lemmatize(a, pos = 'v') != a else lemma.lemmatize(a) for a in word_array]

    # Is this efficient?
    word_dict = {a: word_array.count(a) for a in word_array if a not in ['', '-','\'']}

    return word_dict

def parseTXT(file_name):
    if not os.path.exists(file_name): return "File not found."
    txt_str = open(file_name, 'r').read()
    clean_txt = re.sub(r'[^\w\'\-]',' ',txt_str).lower().split(' ')
    return {a:clean_txt.count(a) for a in set(clean_txt) - {''}}

def parseBIGtxt(file_name):
    if not os.path.exists(file_name): return "File not found."
    result_dict = {}
    with open(file_name, 'r') as txt_file:
        for line in txt_file:
            clean_line = re.sub(r'[^\w\'\-]',' ',line).lower().split(' ')
            for word in clean_line: 
                if word in result_dict:
                    result_dict[word] += 1
                else:
                    result_dict[word] = 1
    del result_dict['']
    return result_dict

def read_file(file_name):
    open_file = open(file_name, 'r')
    word_list =[]
    contents = open_file.readlines()
    for i in range(len(contents)):
         word_list.extend(contents[i].split())    
    open_file.close()
    tuples_list = [(word, len(word)) for word in word_list]
    return tuples_list

pattern = re.compile("[^\w'-]|_")
with open(sys.argv[1], 'r') as content_file:
    content = content_file.read().strip().lower()
    stripped_content = pattern.sub(' ', content)
    arr = stripped_content.split()
    counter = Counter()
    for word in arr:
        counter[word] += 1

    pprint.pprint(counter)
