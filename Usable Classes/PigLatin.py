def pig_latin(words):
    vowel = words.replace(words[len(words) - 1],
                          (words[len(words) - 1] + 'ay'), 1)
    consonant = words.replace(words[len(words) - 1],
                              (words[len(words) - 1] + words[0] + 'ay'), 1).replace(words[0], "", 1)
    if (vowel.startswith('a')) \
            or (vowel.startswith('e')) \
            or (vowel.startswith('i')) \
            or (vowel.startswith('o')) \
            or (vowel.startswith('u')):
        print(vowel)
    else:
        print(consonant)


pig_latin(input())