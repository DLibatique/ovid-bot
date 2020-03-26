from cltk.tokenize.line import LineTokenizer
from os import listdir, path


#initialize tokenizer
tokenizer = LineTokenizer('latin')

#create list of lines
whole_met = []

list_of_files = sorted([
    file for file in listdir('la') if path.isfile(path.join('la/',file))
])

#iterate through files/books of Metamorphoses
for file in list_of_files:

    if file.startswith('ovid'):

        #get text from each file
        with open('la/' + file) as f:
            raw = f.read()

            #add line-tokenized text to the master list of lines
            whole_met += tokenizer.tokenize(raw)

clean_met = [string.replace('\t',' ') for string in whole_met]
