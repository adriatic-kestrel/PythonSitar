from flask import Flask, render_template
from datetime import datetime
from phrasal_verb import definition, generated_verb
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
    return render_template(
        "phrasal_verb.html", data={"definition": definition(), "verb": generated_verb()}
    )

@app.route("/burgeramt")
def burgeramt():
    return render_template(
        "burgeramt.html",
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
        },
    )

@app.route("/seinfeld")
def seinfeld_opening():
    return render_template(
        "seinfeld_opening.html",
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