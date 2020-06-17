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


