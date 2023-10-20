# string = "patriarchy monarchy plutocracy gynaecocracy oligarchy ochlocracy gerontocracy diarchy meritocrac democracy technocracy stratocracy aristocracy anarchy theocracy"
# answer = ["ruling of the father","the rule of one","wealthy","women", "rule of teh few", "mob rule", "old people", "two", "people selected according to merit","the people", "skill,art","miltary forces","best qualified citizen","without rulee","priests"]
# string = "agoraphobia necrophobia triskaidekaphobia nyctophobia heliophobia ailurophobia ornithophobia ponophobia zoophobia arachnophobia thanatophobia homophobia photophobia acrophobia xenophobia"
# answer = ["place of assemble","corpse", "number 13", "right","sun", "cats", "bird", "fatigue", "animals", "spider", "death", "gay peopls", "light", "heights", "foreigners"]
string = "ichthyology dendrology microbiology dermatology gerontology herpetology seismology pathology pharmacology petrology anthropology ethnology conchology speleology oenology"
answer = ["fish", "tree", "microscopic organisms", "skin", "disease of older people", "amphibians and reptiles", ""]
question = string.split()
line = ""
for qa in range(0,len(question)):
    line = line + "#\n"
    line = line + "What fears are indicated by this word: " + question[qa] + "\n"
    line = line + answer[qa] + "\n"
print(line)
