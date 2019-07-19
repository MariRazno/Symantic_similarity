from nltk.corpus import wordnet as wn
from nltk.corpus import brown
import math


def i_will_do_it(word1, word2):
    word1 = word1 + '.n.01'
    word2 = word2 + '.n.01'
    lcs = wn.synset(word1).lowest_common_hypernyms(wn.synset(word2))
    print(lcs)
    hyponym = lcs[0].hyponyms()
    p = (len(sorted(lemma.name() for w in hyponym for lemma in w.lemmas())) / len(brown.words()))
    resnik = -math.log(p)
    return 'Семантическая близость ваших слов по методу Резника =', int(resnik)

word1 = input('Введите первое понятие: ')
word2 = input('Введите второе понятие: ')

print(i_will_do_it(word1, word2))