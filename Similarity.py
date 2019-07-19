from nltk.corpus import wordnet as wn

def root_similarity():
    shortest_path_distance = wn.synset('hostess.n.01').shortest_path_distance(wn.synset('liberal.n.01'))
    print(shortest_path_distance)
    pathlen = 1 + shortest_path_distance
    simpath = 1/pathlen
    print(simpath)
    shortest_path_distance2 = wn.synset('hostess.n.01').shortest_path_distance(wn.synset('host.n.01'))
    print(shortest_path_distance2)
    pathlen2 = 1 + shortest_path_distance2
    simpath2 = 1 / pathlen2
    print(simpath2)
    if simpath > simpath2:
        print('hostess and liberal are more simmilar than hostess and host, or their similarity is equal')
    elif simpath == simpath2:
        print('their similarity is equal')
    else:
        print('hostess and host are more simmilar than hostess and liberal')

def root():
    hostess = wn.synset('hostess.n.01')
    liberal = wn.synset('liberal.n.01')
    print(wn.synset('hostess.n.01').path_similarity(wn.synset('liberal.n.01')))



print(root_similarity())
print('root', root())