import random

excuse_list = ["Entschuldigung",
               "Entschuldung",
               "Entschuldame mucho",
               "Entschulderino",
               "Entschul... ja",
               "Enschulgung",
               "Untschuldengung",
               "I'm sorry",
               "Enschuldingungen Sie mir, danke",
               "please, have mercy",
               "Schuldugung",
               "Schuldung"]

spreche_wrong_list = ["spreche",
                 "... uh... speak...",
                 "sprachen",
                 "spruch",
                 "sprecherino",
                 "spreicho",
                 "spresche",
                 "hablo",
                 "kann sprechen",
                 "spr...sprach...sprech... sprachen",
                 "spreak",
                 "spock",
                 "spups"]

brauche_wrong_list = ["brauche",
                      "bracchio",
                      "braucherino",
                      "brennwert",
                      "breuche",
                      "brodo",
                      "broche",
                      "br...brouch...brauch...broucho",
                      "brant",
                      "... uh, need",
                      "willen wollen",
                      "necessito"]

document_part1_list = ["An",
                       "Auf",
                       "Über",
                       "Unter",
                       "Zwischen",
                       "Ab",
                       "An",
                       "Durch",
                       "Arbeitslos",
                       ]

document_part2_list = ["meldung",
                       "bewerbung",
                       "ordnung",
                       "rechtigung",
                       "schutz",
                       "gemein",
                       "haustier",
                       "antrag",
                       "rechti"]

document_part3_list = ["schein",
                       "gung",
                       "schaft",
                       "stelle",
                       "bescheidigung",
                       "keit",
                       ]

exclamation_list = ["Holy Moly Guacamoley",
                    "¡Madre de Dios",
                    "What?",
                    "Wie, Bitta?",
                    "W...was?",
                    "Ma che cazzo ...?",
                    "Oh putain...",
                    "Oh for Pete's sake",
                    "Was",
                    "Say whaaaaaaaaat?",
                    "Scheißerino!",
                    "N...nan desu-ka?!"]

was_ist_das_wrong_list = ["Wat it das",
                          "Was ist das",
                          "Was ist was",
                          "Was ist",
                          "Wasserino ist dasserino",
                          "Walter ist das",
                          "Wasserino ist das",
                          "Was ist es",
                          "Das ist was",
                          "Was...Was it ist"]

def dialogue_part1():
    excuse_marker = random.choice(range(len(excuse_list)))
    excuse= (excuse_list[excuse_marker])
    return excuse

def dialogue_part2():
    spreche_wrong_marker = random.choice(range(len(spreche_wrong_list)))
    spreche_wrong= (spreche_wrong_list[spreche_wrong_marker])
    return spreche_wrong

def dialogue_part3():
    brauche_wrong_marker= random.choice(range(len(brauche_wrong_list)))
    brauche_wrong= (brauche_wrong_list[brauche_wrong_marker])
    return brauche_wrong

def dialogue_part4():
    document_part1_marker = random.choice(range(len(document_part1_list)))
    document_part2_marker = random.choice(range(len(document_part2_list)))
    document_part3_marker = random.choice(range(len(document_part3_list)))
    document1_tuple= (document_part1_list[document_part1_marker],
            document_part2_list[document_part2_marker],
            document_part3_list[document_part3_marker])
    document1= "".join(document1_tuple)
    return document1

def dialogue_part5():
    document_part1_marker = random.choice(range(len(document_part1_list)))
    document_part2_marker = random.choice(range(len(document_part2_list)))
    document_part3_marker = random.choice(range(len(document_part3_list)))
    document2_tuple= (document_part1_list[document_part1_marker],
            document_part2_list[document_part2_marker],
            document_part3_list[document_part3_marker])
    document2= "".join(document2_tuple)
    return document2

def dialogue_part6():
    exclamation_marker =random.choice(range(len(exclamation_list)))
    exclamation= (exclamation_list[exclamation_marker])
    return exclamation 

def dialogue_part7():
    was_ist_das_wrong_marker = random.choice(range(len(was_ist_das_wrong_list)))
    was_ist_das=(was_ist_das_wrong_list[was_ist_das_wrong_marker])
    return was_ist_das
