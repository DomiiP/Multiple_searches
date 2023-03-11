import webbrowser
import sys

# --- | (1) Simple command program for multiple searches (with parameters)| ---

# Example of using
# >python searches.py cat dog parrot
# Upper line will search for results of 'cat' and 'dog' and 'parrot'
# >python searches.py cat dog + big
# Upper line will search for results of 'big cat' and 'big dog'
# >python searches.py cat dog + big + red
# Upper line will search for results 'big cat red' and 'big dog red'


# For easier implementation I will just use Google
browser = 'google'
# This will not be implemented in command program
specified_browser = 'chrome'
# All words
words     = sys.argv
#print(words)
arguments = ""
before    = ""
after     = ""
# Delete first item in list
words.pop(0)
#print(words)
# Combine into words
#words = words.split()
# Now we will seperate words looking for '+'
start = 0
counter = 0
i = 0
while i < len(words):
    #print(words[i])
    if words[i] == '+':
        start += 1
    if start == 0:
        arguments += ' ' + words[i]
        counter += 1
    if start == 1:
        before += ' ' + words[i]
    if start == 2:
        after += ' ' + words[i]
    if start == 3:
        break
    i += 1
    #print(i)

if before != '':
    before = before[1:]
if after != '':
    after = after[3:]
    print(after)

# Combine words
def combineWords(words):
    for word in words:
        if '+' in word:
            word = word.replace('+', ' ')
combineWords(words)
# Words before and after will be seperated with '+'
i = 0
while i < counter:
    webbrowser.open(f"https://google.com/search?q={before}+{words[i]}+{after}")
    i += 1
