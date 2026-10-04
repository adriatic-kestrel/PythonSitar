from flask import Flask, render_template
from datetime import datetime
from phrasal_verb import definition, example, generated_verb, grammar_label
from burgeramt import (
    dialogue_part1,
    dialogue_part2,
    dialogue_part3,
    dialogue_part4,
    dialogue_part5,
    dialogue_part6,
    dialogue_part7,
)
from hrrejection import hr_part1, hr_part2, hr_part3, hr_part4, hr_part5, hr_part6
from seinfeld import seinf_part1, seinf_part2, seinf_part3, seinf_part4

app = Flask(__name__)
from flask import redirect, request
from flask import send_from_directory


@app.context_processor
def inject_year():
    return {"current_year": datetime.now().year}


# Short loops shown in the Lab section. Each one was generated from a text prompt.
LAB_CLIPS = [
    {
        "slug": "hero-magpie",
        "title": "Magpie take-off",
        "model": "Seedance 2.5 via Higgsfield",
        "prompt": "Cinematic slow-motion shot of a single black-and-white magpie spreading its wings and taking flight in a pure black void. Its iridescent blue-green tail feathers catch a warm coral-orange rim light. Tiny glowing orange particles and fine digital light fragments drift around it like dust. Shallow depth of field, anamorphic lens, high contrast, deep blacks, film grain, bird off-center to the right.",
    },
    {
        "slug": "lab-pipeline",
        "title": "Light through the pipeline",
        "model": "Seedance 2.5 via Higgsfield",
        "prompt": "Abstract macro shot: thin streams of coral-orange light flow through a dark lattice of sharp black glass triangles, like data moving through a pipeline. Slow dolly forward, volumetric haze, deep black background, high contrast, glossy reflections, cinematic.",
    },
    {
        "slug": "lab-screens",
        "title": "Ten years of screens",
        "model": "Seedance 2.5 via Higgsfield",
        "prompt": "Dozens of small floating vintage screens and film frames drift slowly through black space, each glowing with soft abstract coral-orange and warm white light, no readable content. Gentle parallax, slow camera drift, shallow depth of field, bokeh, film grain, moody, nostalgic.",
    },
    {
        "slug": "lab-obsidian",
        "title": "Obsidian triangles",
        "model": "Seedance 2.5 via Higgsfield",
        "prompt": "Large shards of black obsidian glass shaped like triangles rotate slowly in darkness, their edges lit by a thin coral-orange rim light, soft smoke drifting behind. Very slow motion, centered composition, deep blacks, high contrast, premium cinematic look.",
    },
]

# Background loop for the Seinfeld page, credited on the page like the Lab clips.
SEINFELD_CLIP = {
    "slug": "seinfeld-surreal",
    "model": "Seedance 2.5 via Higgsfield, from a GPT Image 2.5 start and end frame",
    "prompt": "Surreal, wacky low-poly stand-up comedy. The faceless coral zentai comedian tells a joke and his body goes absurd: his arms stretch like rubber far beyond the spotlight and snap back, his head spins a full turn on his neck, the microphone floats up out of his hand and drifts back into it, the spotlight circle wobbles like jelly on the brick wall. Then he settles back into exactly the same relaxed pose as the start. Flat-shaded faceted polygons, retro 3D game look, total darkness around the spotlight, static camera, seamless loop. No text, no audience.",
}

# Background loop for the Burgeramt page.
BURGERAMT_CLIP = {
    "slug": "burgeramt-counter",
    "model": "Seedance 2.5 via Higgsfield, from a GPT Image 2.5 start and end frame",
    "prompt": "Surreal, wacky low-poly scene at a German public office counter. The faceless coral zentai man is terrified while he talks: he trembles, shrinks into himself, clutches the folder tighter, peeks up at the clerk, flinches, makes small pleading apologetic gestures with one hand and nervously shifts his weight. The faceless white zentai woman behind the grey desk barely moves at all: she stays rigid and upright, only a tiny slow tilt of her head, completely unimpressed. Then everything settles back into exactly the starting poses. Flat-shaded faceted polygons, retro 3D game look, dark background, single overhead lamp, static camera, seamless loop. No text, no logos.",
}

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

@app.route('/llms.txt')
def llms():
    return send_from_directory('static', 'llms.txt')

@app.route('/google20d3949ac7d286d0.html')
def google_verification():
    return send_from_directory('static', 'google20d3949ac7d286d0.html')

@app.route('/sitemap.xml')
def sitemap():
    base_url = 'https://www.arnaldopangia.com'
    urls = [
        {'loc': f'{base_url}/', 'changefreq': 'weekly', 'priority': 1.0},
        {'loc': f'{base_url}/projects', 'changefreq': 'monthly', 'priority': 0.9},
        {'loc': f'{base_url}/wacky', 'changefreq': 'monthly', 'priority': 0.5},
        {'loc': f'{base_url}/phrasal_verb', 'changefreq': 'weekly', 'priority': 0.3},
        {'loc': f'{base_url}/burgeramt', 'changefreq': 'weekly', 'priority': 0.3},
        {'loc': f'{base_url}/hrrejection', 'changefreq': 'weekly', 'priority': 0.3},
        {'loc': f'{base_url}/seinfeld', 'changefreq': 'weekly', 'priority': 0.3},
        {'loc': f'{base_url}/ai-calculator', 'changefreq': 'monthly', 'priority': 0.3},
    ]
    return render_template('sitemap.xml', urls=urls), 200, {'Content-Type': 'application/xml'}


@app.before_request
def redirect_to_www():
    host = request.host
    if host.startswith("arnaldopangia.com"):
        return redirect(f"https://www.arnaldopangia.com{request.full_path}", code=301)

@app.route("/")
def index():
    return render_template("index.html", lab_clips=LAB_CLIPS)

@app.route("/projects")
def previous():
    return render_template("projects.html", current_year=datetime.now().year)

@app.route("/wacky")
def wacky():
    return render_template("wacky.html", current_year=datetime.now().year)

@app.route("/phrasal_verb")
def phrasal_verb():
    # A searched term gets its own entry; otherwise invent a phrasal verb.
    query = " ".join(request.args.get("q", "").split())[:40]
    verb = query or generated_verb()
    return render_template(
        "phrasal_verb.html",
        data={
            "verb": verb,
            "searched": bool(query),
            "label": grammar_label(),
            "senses": [
                {"definition": definition(), "example": example(verb)},
                {"definition": definition(), "example": example(verb)},
            ],
            "see_also": [generated_verb() for _ in range(4)],
        },
    )

@app.route("/burgeramt")
def burgeramt():
    return render_template(
        "burgeramt.html",
        clip=BURGERAMT_CLIP,
        data={
            "part1": dialogue_part1(),
            "part2": dialogue_part2(),
            "part3": dialogue_part3(),
            "part4": dialogue_part4(),
            "part5": dialogue_part5(),
            "part6": dialogue_part6(),
            "part7": dialogue_part7(),
        },
    )

@app.route("/hrrejection")
def hrrejection():
    return render_template(
        "hrrejection_input.html",
        data={
            "hr_part1": hr_part1(),
            "hr_part2": hr_part2(),
            "hr_part3": hr_part3(),
            "hr_part4": hr_part4(),
            "hr_part5": hr_part5(),
            "hr_part6": hr_part6(),
            "sent": datetime.now().strftime("%a %d %b %Y, %H:%M"),
        },
    )

@app.route("/ai-calculator")
def ai_calculator():
    return render_template("ai_calculator.html")

@app.route("/seinfeld")
def seinfeld_opening():
    return render_template(
        "seinfeld_opening.html",
        clip=SEINFELD_CLIP,
        data={
            "seinf_part1": seinf_part1(),
            "seinf_part2": seinf_part2(),
            "seinf_part3": seinf_part3(),
            "seinf_part4": seinf_part4(),
        },
    )

# if __name__ == "__main__":
#     import os
#     port = int(os.environ.get("PORT", 80))
#     app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 80))
    app.run(host="0.0.0.0", port=port, debug=True)