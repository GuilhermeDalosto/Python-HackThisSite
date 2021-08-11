#
#    This level is about unscrambling words.
#
#Find the original (unscrambled) words, which were randomly taken from a wordlist.<--
#Send a comma separated list of the original words, in the same order as in the list below.
#
#
#You have 30 seconds time to send the solution.
#List of scrambled words:
#tecrse
#lnhateep
#teovrmn
#vkigin
#leubrt
#leloacbt
#cugroas
#usenirs
#daaern
#keyohc
#
#
#Answer:            (Example:   word1,word2,word3, ... word9,word10)

from collections import Counter

def contains(s1, s2):
    s2set = Counter(s2)
    return all(count <= s2set[c] for c, count in Counter(s1).items())

result = []

request = """  
perlup
cotnewur
rizdtz
me1oyn
odorth
smshiang
aabenn
heaeaddd
ttlaes
egirdb
""".split()

with open('wordList.txt') as file:
    text = [line.strip() for line in file]



for substring in request:
    for string in text:         
        if contains(substring,string) and len(string) == len(substring):
            result.append(string)


file.close()
result = ','.join(result)
print(result)




