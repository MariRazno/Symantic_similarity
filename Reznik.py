from nltk.corpus import wordnet as wn
from nltk.corpus import brown
import math

'''enwords = [a.lower() for a in set(brown.words()) if len(a)>3]
#wn.synset('bowl.n.01').lowest_common_hypernyms(wn.synset('polyhedron.n.01'))
host = wn.synset('host.n.01')
sobersides = wn.synset('sobersides.n.01')
rez = wn.res_similarity(host, sobersides, brown.row())
print(rez)'''

lcs = wn.synset('host.n.01').lowest_common_hypernyms(wn.synset('sobersides.n.01'))
print(lcs)
hypernym = lcs[0]
hyponym = hypernym.hyponyms()
ic = (len(sorted(lemma.name() for w in hyponym for lemma in w.lemmas()))/len(brown.words()))
print('Вероятность появления слова adult.n.01 в корпусе brown = ', ic)
resnik = -math.log(ic)
print('Семантическая близость слов host.n.01 и sobersides.n.01 по методу Резника = ', int(resnik))