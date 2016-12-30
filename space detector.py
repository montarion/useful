#---imports regular expressions
import re
sentence = 'what is thy sentence? '

for test in re.finditer(' ', sentence):
         spaces = 'space found', test.end()
         print(spaces)

#---variants incoming---#
import re
sentence = 'what is thy sentence?'

for test in re.finditer(' ', sentence):
    spaces = 'first letter from every word found', (test.end())
    print(spaces)
    firstletter = (test.end())
    print(sentence[firstletter])
