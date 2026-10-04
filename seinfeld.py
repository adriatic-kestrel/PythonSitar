import random

topic_list = [
    "YouTubers",
    "Twitter",
    "Instagram",
    "Tik Tok",
    "vegans",
    "woke culture",
    "cancel culture",
    "iPhones",
    "Elon Musk",
    "Donald Trump",
    "Amazon",
    "Netflix",
    "LinkedIn",
    "Crypto-values",
    "Game Stop stocks",
    "boomers",
    "zoomers",
    "Arnaldo Pangia",
    "Brexit",
    "China",
    "climate change",
    "electric cars",
    "Greta Thunberg",
    "Covid",
    "Coronavirus",
    "Jeff Bezos",
    "memes",
    "Tesla",
    "LGBTQ+",
    "Reddit",
    "Black lives matter",
    "Marc Zuckerberg",
    "Joe Biden",
    "all lives matter",
    "systemic racism",
    "AI",
    "ChatGPT",
]

adjective_list = [
    "whimsical",
    "smart",
    "deep",
    "informed",
    "funny",
    "likeable",
    "insightful",
    "clever",
    "scary",
    "hip",
    "derivative",
    "cutting-edge",
    "progressive",
    "intelligent",
    "well informed",
    "environmentally friendly",
    "cosmopolite",
    "up to date",
    "disruptive",
    "silly",
    "German",
    "Polish",
    "bland",
]

judgement_list = [
    "virus",
    "movement",
    "entrepeneur",
    "object",
    "singer",
    "natural phenomenon",
    "trend",
    "philosophy",
    "brand of chips",
    "fastfood chain",
    "dog breed",
    "dictatorship",
    "sauce dip",
    "spaghetti brand",
    "neighborhood in Berlin",
    "climate activist",
    "Italian guy",
    "language",
    "video game",
    "bowel movement",
    "stink",
    "smell",
    "billionaire",
    "tropical island",
    "walrus",
    "computer",
]
place_list = [
    "at the movies",
    "having a steak",
    "having a beer",
    "at the swimming pool",
    "at the thrift store",
    "at the park",
    "at a barbecue",
    "at the beach",
    "at a museum",
    "downtown",
    "in Termoli",
    "in a chinese restaurant",
    "at the bar",
    "at the club",
    "at the country club",
    "having falafel",
    "at a Israeli restaurant",
    "at a Jamaican restaurant",
    "at a Greek restaurant",
    "in a nudist beach",
    "anywhere in the world",
    "in a hospital",
]

explanation_list = [
    "It's not you. It's us.",
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
    "Skidaadle skidoodle: Your application is now a noodle!",
]

sympathy_list = [
    "We wish you all the best for",
    "We're sure you'll be fine in",
    "Best of luck for",
    "All the best for",
    "You're super cool though, you'll have no problem in ",
    "It's gonna be a loooong journey with ",
    "Keep being awesome with",
    "Keep rocking",
    "Keep being a superhero with",
    "If you're upsetti, have spaghetti. Good luck with",
    "Soooooorriiiii, all the best with",
]


def seinf_part1():
    topic_marker = random.choice(range(len(topic_list)))
    topic = topic_list[topic_marker]
    return topic


def seinf_part2():
    adjective_marker = random.choice(range(len(adjective_list)))
    adjective = adjective_list[adjective_marker]
    return adjective


def seinf_part3():
    judgement_marker = random.choice(range(len(judgement_list)))
    judgement = judgement_list[judgement_marker]
    return judgement


def seinf_part4():
    place_marker = random.choice(range(len(place_list)))
    place = place_list[place_marker]
    return place


def hr_part5():
    explanation_marker = random.choice(range(len(explanation_list)))
    explanation = explanation_list[explanation_marker]
    return explanation


def hr_part6():
    sympathy_marker = random.choice(range(len(sympathy_list)))
    sympathy = sympathy_list[sympathy_marker]
    return sympathy
