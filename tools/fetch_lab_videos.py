"""Download the AI-generated video loops and prepare them for the web.

Run once from the repo root:

    python3 tools/fetch_lab_videos.py

It downloads each clip into static/video/, re-encodes it into a small,
silent, streamable MP4 (H.264, +faststart) and grabs a JPG poster frame.
Needs ffmpeg on your PATH (sudo apt install ffmpeg). Without ffmpeg the
raw files are kept as they are and no posters are made.
"""

import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "static" / "video"
CDN = "https://d8j0ntlcm91z4.cloudfront.net/user_3Efye6NBSsbmfot1HFi752160rK/"

# slug: (source file, max width, poster time in seconds)
CLIPS = {
    "hero-magpie": ("hf_20261003_070204_a9b314b8-b450-4d0b-a8eb-17f9950becf0.mp4", 1920, 2.5),
    "lab-pipeline": ("hf_20261003_070204_3e9de0b5-d8e9-4654-b08c-52447cf9661a.mp4", 1280, 2.0),
    "lab-screens": ("hf_20261003_070204_86745554-39c6-4b11-9036-bf63108a2d00.mp4", 1280, 2.0),
    "lab-obsidian": ("hf_20261003_070204_b354db97-5208-4222-8797-23a7d21d89a8.mp4", 1280, 2.0),
}


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    has_ffmpeg = shutil.which("ffmpeg") is not None
    if not has_ffmpeg:
        print("ffmpeg not found: clips will be saved unoptimised and without posters.")

    for slug, (src, width, poster_at) in CLIPS.items():
        raw = OUT / f"{slug}.raw.mp4"
        mp4 = OUT / f"{slug}.mp4"
        jpg = OUT / f"{slug}.jpg"

        print(f"Downloading {slug} ...")
        req = urllib.request.Request(CDN + src, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as r, open(raw, "wb") as f:
            shutil.copyfileobj(r, f)

        if not has_ffmpeg:
            raw.replace(mp4)
            continue

        print(f"  encoding {mp4.name}")
        run([
            "ffmpeg", "-y", "-i", str(raw),
            "-an",
            "-vf", f"scale='min({width},iw)':-2,format=yuv420p",
            "-c:v", "libx264", "-preset", "slow", "-crf", "26",
            "-movflags", "+faststart",
            str(mp4),
        ])
        print(f"  poster {jpg.name}")
        run([
            "ffmpeg", "-y", "-ss", str(poster_at), "-i", str(mp4),
            "-frames:v", "1", "-q:v", "4", str(jpg),
        ])
        raw.unlink()

    total = sum(p.stat().st_size for p in OUT.glob("*.*")) / 1_000_000
    print(f"Done. static/video/ is {total:.1f} MB.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001
        print(f"Failed: {exc}")
        sys.exit(1)
