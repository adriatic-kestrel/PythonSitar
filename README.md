## Python SitArr

As in *Python* Web*Sit*e *Arr*naldo Pangia.

A Python Flask web application that acts as the portfolio of Arnaldo Pangia, AI Creative Producer in Berlin.

## How to run locally

```bash
pip install -r requirements.txt
python3 tools/fetch_lab_videos.py   # first time only: downloads and compresses the AI video loops
PORT=5000 python3 app.py
```

Then open http://localhost:5000 in your browser.

## Video loops

The hero, Lab and section backgrounds use short AI-generated loops stored in `static/video/`
(an MP4 plus a JPG poster per clip). The prompts that generated them live in `LAB_CLIPS` in `app.py`
and are shown on the homepage. To add a clip, drop `<slug>.mp4` and `<slug>.jpg` into
`static/video/` and add an entry to `LAB_CLIPS`.

## Fonts

Archivo (variable, width and weight axes) is self-hosted from `static/fonts/` under the SIL Open Font License.
