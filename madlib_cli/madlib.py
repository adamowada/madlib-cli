# https://stackoverflow.com/questions/47782353/python-using-regex-to-search-for-a-string-then-append-each-match-to-a-new-list
# https://www.geeksforgeeks.org/python-regex-re-search-vs-re-findall/
# https://stackoverflow.com/questions/413071/regex-to-get-string-between-curly-braces?newreg=c69f3c6ab1a34d9889687842884323b7

# https://docs.python.org/2/library/re.html
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

template =""

with open('sample_template.txt', 'r') as template:
  template = template.read()

regex1 = '{([^}]*)}'
regex2 = '({[^}]*})'

match = re.findall(regex1, template)

responses = []

for i in match:
  print(i)
  responses.append(str(input()))
  print('\n')



print(responses)
