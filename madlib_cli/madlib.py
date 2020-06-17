# https://stackoverflow.com/questions/47782353/python-using-regex-to-search-for-a-string-then-append-each-match-to-a-new-list helped me with regex
# https://www.geeksforgeeks.org/python-regex-re-search-vs-re-findall/ helped me with regex findall
# https://stackoverflow.com/questions/413071/regex-to-get-string-between-curly-braces?newreg=c69f3c6ab1a34d9889687842884323b7 helped me with the regular expression string itself
# https://docs.python.org/2/library/re.html helped me a lot with regex methods
# https://stackoverflow.com/questions/59313087/python-regex-how-to-replace-each-match-individually helped me with the idea to use match objects
# https://docs.python.org/3/library/re.html#match-objects helped me with match objects

import re

print("""
Welcome to the Madlib cli app!

Prompts will ask you to input
certain types of words. For example,
if the prompt asks for a color you
might type "red". 

After you type your response press
enter to continue.

After all prompts have been entered, 
the finished madlib will be displayed 
and saved as a text file. Have fun!

""")

template = ""

with open('sample_template.txt', 'r') as template:
  template = template.read()

regex1 = '{([^}]*)}'
regex2 = '({[^}]*})'

matches = re.findall(regex1, template)

for i in range(len(matches)):
    m = re.search(regex2, template)
    print(matches[i])
    template = template[:m.start()] + input() + template[m.end():]
    print('\n')

print(template)


