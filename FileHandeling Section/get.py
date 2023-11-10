# string = "patriarchy monarchy plutocracy gynaecocracy oligarchy ochlocracy gerontocracy diarchy meritocrac democracy technocracy stratocracy aristocracy anarchy theocracy"
# answer = ["ruling of the father","the rule of one","wealthy","women", "rule of teh few", "mob rule", "old people", "two", "people selected according to merit","the people", "skill,art","miltary forces","best qualified citizen","without rulee","priests"]

# string = "agoraphobia necrophobia triskaidekaphobia nyctophobia heliophobia ailurophobia ornithophobia ponophobia zoophobia arachnophobia thanatophobia homophobia photophobia acrophobia xenophobia"
# answer = ["place of assemble","corpse", "number 13", "right","sun", "cats", "bird", "fatigue", "animals", "spider", "death", "gay peopls", "light", "heights", "foreigners"]

# string = "ichthyology dendrology microbiology dermatology gerontology herpetology seismology pathology pharmacology petrology anthropology ethnology conchology speleology oenology"
# answer = ["fish", "tree", "microscopic organisms", "skin", "disease of older people", "amphibians and reptiles", "earthqakes", "diseases", "drugs and medicine", "rock", "humanity", "humans as cultulral beings", "shell", "caves","wines and winemaking"]

# string = "monocle hemiplegia diplopia tripod pentadactyl heptameter hectolitre octamerous monopolize tetrad"
# answer = ["an eyeglass for one eye (1)","paralysis of one side of the body (10)","double vision (1)","a three-legged stand (3)","having five fingers or toes (5)"," a verse of seven metrical feet (7)","a metric unit of 100 liters (100)","having eight parts (8)","to have single control of something (1)","a group of four (4)"]

# question = [" Hollywood (for US film industry)","Marilyn Munroe","buzz", "synergy - collaboration", "Mandela Park","AIDS","love - hate","vein - vain","authentic replica","contract (v) – contract (n)"]
# answer = ["metonymy","pseudonym","onomatopoeia","synonym","eponym","acronym","antonym","homophone","oxymoron","homograph"]

# question = ["identification of a disease","shapeless","offspring","producing fever","inscription on a tomb","teamwork","leader of the people","marriage within a tribe","named after a place","a differing opinion","worship of images","pleasant sound","transparent","dictionary","putting off till tomorrow"]
# answer = ["diagnosis","amorphous","progeny","pyretic","epitath","synergy","demagogue","endogamy","toponym","heterodox","iconolatry","euphonym","diaphonous","lexicon","procrastination"]

# question = ["irritated","dunious","factual","elated","less harsh phrase","puzzling","revelation","peculiarity","coded","educational"]
# answer = ["antagonized","aporyphal","empirical","euphoric","euphemism","cryptic","epiphany","anomaly","encryption","pedagogical"]

# question = ["irregular, unusual","temple dedicated to all the gods","not knowing","at the same time","leading actor","praising","worship of statues","meeting place","many colored","in direct contrast to","science of the structure of the universe","belief that the sun revolves around the earth","believing that one is totally powerful","one who studies handwriting","conventional"]
# answer = ["anomalous","pantheon","agnostic","synchronous","protagonist","eulogistic","iconolatry","synogogue","polychrome","antitheticel","cosmography","geocentrism","megalomaniac","graphologist","orthodox"]

# question = ["Study of the universe: c _ _ _ _ _ _ g _","The art of stuffing dead animals t_ _ _ d _ _ _ _","Moral e _ _ _ _ _ _","New word n_ _ _ _ _ _ s _","Feeling the suffering of others e _ _ _ t _ _","Something that speeds up change c a _ _ _ _ _ _","Prediction p _ _ p _ _ _ _","Inability to speak a _ h _ _ _ _","Study of cause and nature of disease p _ _ _ _ l _ _ _ ","Study of the environment e _ _ _ _ _ _"]
# answer = ["cosmology","taxidermy","ethical","neologism","empathy","catalyst","prophecy","aphasia","pathology","ecology"]

# question = ["Dogmatic and canine are etymologically related.","A dekalitre is one tenth of a litre.","Petrified indicates that one has been turned into rock/stone out of fear.","A necrophiliac would love to work in a mortuary.","Demotic writing refers to the symbols of black magic.","The metre as a unit of length is defined in terms of the speed of light.","A photosensitive person is camera-shy.","The Oxford dictionary is a famous lexicon.","A man who suffers from gynaephobia is likely to be a philanderer.","A polymath is knowledgeable in many disciplines.","Xenogamy refers to cross-fertilization.","Cosmonaut and astronaut are synonyms.","Pantheism refers to the study of panthers and their habits.","Hieroglyphics is an archaic form of writing.","Encrypted writing is easily understood."]
# answer = ["F","F","T","T","F","T","T","T","F","T","T","T","F","T","F"]

# question = [
#     "The anomalous test results mean that the rocket is ready to launch.",
#     "It may sound odd, but I actually enjoy the cacophonous sound of an orchestra tuning up.",
#     "Cartography has helped scientists gain a good understanding of the fundamental workings of the human brain.",
#     "Catalysts for change on the school board blocked attempts to implement reforms.",
#     "Demographic trends in Japan show that the proportion of old people to young people is increasing.",
#     "In many traditional societies women wear diaphanous clothing to hide their bodies.",
#     "Knowing the entomology of a difficult word can help you remember it.",
#     "It is advisable to see a doctor before traveling to countries in which malaria or other infectious diseases are endemic.",
#     "The patient was given euthanasia before undergoing major surgery.",
#     "The euphoria in the stadium rose to a fever pitch as the seconds ticked down to the Stormers’ rugby team’s victory in the final.",
#     "The ethnocentric villagers have no interest in anything outside their own little world.",
#     "The eulogy talked only about the many flaws in the dead man’s character.",
#     "The poem harks back to an imagined halcyon Golden Age.",
#     "Religious leaders are arguing that the only way to save the country is to establish a theocracy.",
#     "Since he regularly questioned conventional wisdom, the philosopher Socrates can be described as an iconoclast.",
#     "The heterodox pastor teaches only doctrines approved by his church.",
#     "“Not only do I not like human beings in the abstract, I don’t like even one individual member of the human race!” the misanthrope declared.",
#     "Mnemonic devices currently supply nearly 20% of the country’s electric power.",
#     "The speaker’s misogynistic comments drew the anger of several women’s rights groups.",
#     "The emergency room doctor trained herself to be phlegmatic despite the great suffering she witnessed every day."
# ]

# answer = ["NS","S","NS","NS","S","NS","NS","S","NS","S","S","NS","S","S","S","NS","S","NS","S","S",]

# question = string.split()

def generate(file):
    with open(file, 'r') as file:
        question = []
        answer = []
        i = 0
        # Read and print each line
        for line in file:
            index1 = line.find("–")
            index2 = line.find("-")
            if index1 >= 0:
                index = index1
            elif index1<0 and index2>=0 and (line[index2-1]==" " or line[index2+1]==" "):
                index = index2
            else:
                index = -1
            if index >= 0:
                if line[index+1]==" ":  space_f = 1
                else: space_f = 0
                if line[index+1]==" ":  space_b = 1 
                else: space_b = 0
                question.append(line[:index-space_b])
                answer.append(line[index+1+space_f:].replace("\n",""))
                i = i + 1
            else:
                answer[i-1] = answer[i-1] + line.replace("\n","")
    return question, answer

question, answer = generate("FileHandeling Section/qnas/sll/og_chapter6.txt")

if len(answer) != len(question):
    print("not the same number of q and as")
    exit
line = ""
for qa in range(0,len(question)):
    line = line + "#\n"
    line = line + question[qa] + "\n"
    line = line + answer[qa] + "\n"
line = line + "#"
with open("FileHandeling Section/qnas/sll/out.txt", 'w') as file:
    # Write the content to the file
    file.write(line)

# def remove_empty_lines(input_file, output_file):
#     with open(input_file, 'r') as file:
#         lines = file.readlines()

#     # Remove empty lines
#     lines = [line.strip() for line in lines if line.strip()]

#     with open(output_file, 'w') as file:
#         file.write('\n'.join(lines))

# remove_empty_lines('FileHandeling Section/qnas/sll/og_chapter6.txt', 'FileHandeling Section/qnas/sll/og_chapter6.txt')