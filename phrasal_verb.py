import random

verb_list = ["Get",
        "Give",
        "Keep",
        "Take",
        "Pull",
        "Push",
        "Shrub",
        "Drift",
        "Clog",
        "Stand",
        "Brant",
        "Come",
        "Blob",
        "Plopper",
        "Splup",
        "Yeet",
        "Skunk",
        "Pangia",
        "Club",
        "Bark",
        "Plough",
        "Bear",
        "Goat",
        "Be",
        "Do",
        "Go"
        ]

preposition_list = ["up",
        "down",
        "up onto",
        "over",
        "in",
        "across",
        "through",
        "for",
        "on",
        "up onto for",
        "for",
        "askew",
        "away",
        "up away",
        "inbetween",
        "to the moon",
        "OVAH",
        "after",
        "amid",
        "alof",
        "aside",
        "behind",
        "from",
        "off",
        "out",
        "upon",
        ]
def generated_verb():
    verb_list_marker = random.choice(range(len(verb_list)))
    preposition_list_marker = random.choice(range(len(preposition_list)))

    return "{} {}".format(verb_list[verb_list_marker],preposition_list[preposition_list_marker])

definition_verb = ["reiterate",
        "illustrate",
        "edulcorate",
        "annihilate",
        "destruct",
        "build",
        "abduct",
        "pleasure",
        "hurt",
        "work",
        "become",
        "leave",
        "show",
        "believe",
        "play",
        "write",
        "pay",
        "remember",
        "hit",
        "strike",
        "kiss",
        "wait",
        "pull",
        "treasure",
        "absorb",
        "grasp",
        "advance",
        "amend",
        "attack",
        "ignite",
        "scratch",
        "slash",
        "command",
        "deviate",
        "detect",
        "poison",
        "treat",
        "yank",
        "suction"]

definition_object = ["someone",
        "something",
        "somebody"]

definition_adverb = ["viciously",
        "bravely",
        "with awe",
        "with despise",
        "uncontrollably",
        "reiteratedly",
        "with extreme care",
        "bearing grudge",
        "in laughter",
        "delightfully",
        "lightheartedly",
        "frolically",
        "restlessly",
        "in despair",
        "desperately",
        "with passion",
        "with lust",
        "in an Italian way",
        "as Berliners do",
        "just like in Michigan",
        "in Siena, Italy",
        "with embarrassment",
        "with serendipity",
        "timidly",
        "with audacity",
        "in secrecy"]


def definition():
    definition_verb_marker = random.choice(range(len(definition_verb)))
    definition_object_marker = random.choice(range(len(definition_object)))
    definition_adverb_marker = random.choice(range(len(definition_adverb)))

    return "To {} {} {}.".format(
            definition_verb[definition_verb_marker],
            definition_object[definition_object_marker],
            definition_adverb[definition_adverb_marker])


grammar_label_list = ["vi phrasal",
        "vtr phrasal sep",
        "vtr phrasal insep",
        "vtr phrasal, very informal",
        "vi phrasal, Berlin only",
        "vtr phrasal, archaic",
        "vi phrasal, regional (Siena)"]

example_list = ["Every Monday my manager tries to {} the whole team.",
        "You can't just {} a sandwich like that.",
        "We decided to {} the budget meeting.",
        "Please don't {} the cat.",
        "Nobody knows how to {} properly anymore.",
        "My nonna used to {} the tomatoes every Sunday.",
        "If you {} the printer one more time, it will quit.",
        "The landlord threatened to {} the whole building.",
        "I only came here to {} and leave.",
        "In Berlin it is perfectly normal to {} on a Tuesday."]


def grammar_label():
    return random.choice(grammar_label_list)


def example(phrase):
    return random.choice(example_list).format(phrase.lower())
