import random

greeting_list = ["Hello, ",
        "Good morning, ",
        "Hey, ",
        "Ahoi, ",
        "Dear ",
        "My beloved ",
        "'Sup, ",
        "Oh, hai ",
        "Hallo ",
        "Hullo ",
        "Heyyyyy "]

appreciation_list  = ["We are so happy ",
        "We are so grateful ",
        "We treasured ",
        "We feel blessed ",
        "You made us feel very special with the fact ",
        "We are delighted ",
        "It feels so good ",
        "We were psyched ",
        "It is so energizing ",
        "We are feeling so good about ourselves ",
        "We feel all tingly ",
        "We will be forever in debt with you for the fact ",
        "Ohhhh yeaahhh, it felt A-MA-ZING "]

effort_list = ["dedicated your time ",
        "consacrated your efforts ",
        "dedicated aaaaaallll thaaaaaat tiiiiimeeeee ",
        "were so dedicated",
        "were adamant",
        " - against all the odds! - dedicated your efforts ",
                ]
sad_adverb_list = ["Unfortunately, ",
        "Sadly, ",
        "However, ",
        "It's just not fair!!!, but ",
        "It sucks, dewde, but ",
        "We regret to inform you that ",
        "We'we supew dupew sowwy to infowm you that ",
        "Howeverrrrrr ",
        "It's such an itty bitty kitten pity that ",
        "It's so unfortunate, but ",
        "You were awesome -FOR REALZ!!!! - but ",
        "But- uuuuuuuhhhhhh :(((( ",
        "Well, uh... you know... there's a catch: ",
        "Surprise surprise, ",
        "The world can be, however, a very cruel place. In fact ",
        ]

explanation_list = ["It's not you. It's us.",
        "Something didn't quite click with your profile, though.",
        "We were looking for a profile more compatible with our needs.",
        "No. Nevermind. We're just trying to be polite.",
        "And, uh, yeah. That's it",
        "It was not an easy decision",
        "We found a candidate with a higher compatibility",
        "We swear, boss.",
        "Sucks to be you, huh?",
        "In this case, we decided to proceed with someone with a higher compatibility degree, even though we were very impressed with your profile",
        "You had a rockstar profile, but we weren't tuned-in.",
        "You had a superhero profile, but we were the town you needed but didn't deserve",
        "You had an epic profile, but it was not the right time",
        "You had a huge profile, but that was too much for us to handle",
        "Your profile rocked, but we swinged - and missed.",
        "Skidaadle skidoodle: Your application is now a noodle!"]

sympathy_list = ["We wish you all the best for",
        "We're sure you'll be fine in",
        "Best of luck for",
        "All the best for",
        "You're super cool though, you'll have no problem in ",
        "It's gonna be a loooong journey with ",
        "Keep being awesome with",
        "Keep rocking",
        "Keep being a superhero with",
        "If you're upsetti, have spaghetti. Good luck with",
        "Soooooorriiiii, all the best with"]

def hr_part1():
    greeting_marker = random.choice(range(len(greeting_list)))
    greeting= (greeting_list[greeting_marker])
    return greeting

def hr_part2():
    appreciation_marker = random.choice(range(len(appreciation_list)))
    appreciation= (appreciation_list[appreciation_marker])
    return appreciation

def hr_part3():
    effort_marker = random.choice(range(len(effort_list)))
    effort= (effort_list[effort_marker])
    return effort

def hr_part4():
    sad_adverb_marker = random.choice(range(len(sad_adverb_list)))
    sad_adverb= (sad_adverb_list[sad_adverb_marker])
    return sad_adverb

def hr_part5():
    explanation_marker = random.choice(range(len(explanation_list)))
    explanation= (explanation_list[explanation_marker])
    return explanation

def hr_part6():
    sympathy_marker = random.choice(range(len(sympathy_list)))
    sympathy= (sympathy_list[sympathy_marker])
    return sympathy

