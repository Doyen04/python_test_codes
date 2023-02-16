import sys


def split(string, sep):
    spotted = []
    word = ''
    for k in range(len(string)):
        if string[k] != sep:
            word += string[k]
        if string[k] == sep or k == len(string) - 1:
            spotted.append(word)
            word = ''
    return spotted


sent = 'red,is,good,boy for me'
print(sent.split(','))
