# DESIGN.md: arnaldopangia.com

The design system for the personal site of Arnaldo Pangia, AI Creative Producer in Berlin.
Read this before generating or editing any page, component or copy on this site.

## 1. Visual theme and atmosphere

The site is a screening room for AI-made creative. Full-bleed, AI-generated video is the primary
content, and the interface steps back so the footage can carry the page. Pure black, one coral
accent and the brand triangle are the whole vocabulary. Headlines are wide, heavy and tight, like
film titles. Long reading moves onto a light "paper" band so the dark video sections around it
feel like cuts back to the screen.

The site has to prove a skill, not describe it. Wherever possible, show the generated work and
how it was made (model, prompt) instead of adjectives about it.

**Key characteristics**
- AI-generated video loops as heroes and section backgrounds, never as decoration on top of text
- One shape only: the triangle (logo, hero reveal, award marker, play button)
- One typeface: Archivo variable, using its width axis as the main expressive tool
- True black `#000000`, not tinted near-black
- Coral `#EE6C4D` as the single accent; magpie teal `#3FA7A1` only for AI metadata
- Square corners everywhere; no shadows, no gradients as decoration
- One orchestrated motion moment per page; everything else moves only when the visitor acts

## 2. Colour palette and roles

### Core
| Token | Hex | Role |
|---|---|---|
| `--ink` | `#000000` | Page background, text on paper |
| `--carbon` | `#141414` | Raised surfaces on dark (cards, video placeholders) |
| `--ash` | `#2A2A2A` | The only divider and border colour on dark |
| `--bone` | `#EBE9E6` | Body text on dark |
| `--muted` | `#9A9894` | Secondary text and notes on dark (7.3:1 on black) |
| `--coral` | `#EE6C4D` | Brand accent: links, primary button, logo bar, triangles (6.9:1 on black) |
| `--plume` | `#3FA7A1` | Magpie tail-feather teal. Only for "this was made with AI" metadata (model names, credit markers) |

### Light reading band
| Token | Hex | Role |
|---|---|---|
| `--paper` | `#EFEFED` | Background for long-form case studies. Cool neutral, never cream |
| `--graphite` | `#3A3A38` | Body text on paper (9.9:1) |
| `--coral-ink` | `#B2421F` | Coral for text and links on paper (4.9:1). Plain `--coral` is only for fills on paper |

### Rules
- Coral never fills large areas except the primary button and the brand triangle.
- Teal never appears outside AI metadata. If it shows up anywhere else, it stops meaning "AI made this".
- Text over video always sits on a black gradient scrim (see `.hero-shade`); never rely on the footage being dark.

## 3. Typography

### Family
**Archivo** (variable: weight 100 to 900, width 62% to 125%), self-hosted from `static/fonts/`
under the SIL Open Font License. Do not load fonts from Google; the site is hosted for a German
audience and self-hosting avoids the GDPR issue.

### Width is the voice
| Token | Width | Used for |
|---|---|---|
| `--wide` | 125 | All headlines, the contact email, big numbers |
| default | 100 | Body text, buttons, navigation |
| `--narrow` | 82 | Small metadata: case meta, model names, years, credits |

### Hierarchy
| Role | Size | Weight | Width | Line height | Tracking |
|---|---|---|---|---|---|
| Hero title | `clamp(3.2rem, 1.2rem + 9vw, 9.5rem)` | 800 | 125 | 0.86 | -0.035em |
| Page title | `clamp(3.5rem, 1.5rem + 9vw, 9rem)` | 800 | 125 | 0.86 | -0.02em |
| Section title | `clamp(2rem, 1.4rem + 2.6vw, 3.5rem)` | 800 | 125 | 0.95 | -0.02em |
| Contact title | `clamp(1.8rem, 1rem + 3.4vw, 4rem)` | 800 | 125 | 0.95 | -0.02em |
| Lede | `clamp(1.05rem, 1rem + .4vw, 1.3rem)` | 400 | 100 | 1.5 | 0 |
| Body | `clamp(1rem, .95rem + .25vw, 1.125rem)` | 400 | 100 | 1.6 | 0 |
| Metadata | 0.8 to 0.9rem | 400 | 82 | 1.4 | 0 |

### Principles
- Sentence case everywhere. No all-caps labels, no eyebrow text above headings.
- Never highlight a single word inside a headline. The one exception is the hero, where the
  second line ("Producer") is coral because it is a separate line, not an inline accent.
- Body text measure stays under 64ch.
- No monospace anywhere, including for "technical" metadata. Use the narrow width instead.

## 4. Components

### Buttons
- **Solid**: coral fill, black text, 2px coral border, 48px tall, square. Hover inverts to transparent with coral text.
- **Ghost**: transparent, white text, 2px border at 50% white. Hover turns border and text coral.
- Labels say exactly what happens: "See the work", "Explore the lab", "Get in touch". No arrows appended.

### Navigation
Fixed, 64px tall. Starts as a black-to-transparent gradient over the hero and turns solid black with
an `--ash` bottom border after 40px of scroll. The last item, "Get in touch", is outlined in coral.
On screens under 820px it collapses into a full-width panel revealed with a clip-path wipe.

### Video hero (`.hero`)
Full viewport height, video `object-fit: cover`, left and bottom scrims, copy anchored bottom-left.
The video enters through the brand triangle: `clip-path` grows from a small centred triangle until
it covers the frame (1.6s, `cubic-bezier(.7,0,.2,1)`). Headline lines and lede rise in after it.
A small credit in the corner, marked with a teal triangle, says the footage is AI-generated and
links to the Lab.

### Lab stage (`.lab`)
Full-viewport section. All `LAB_CLIPS` loops are stacked behind the copy and crossfade every 8s
(1.4s opacity fade), each with a slow 9s push-in from `scale(1.02)` to `scale(1.1)`. A left-weighted
scrim (92% black at the left edge, 15% at the right; vertical on mobile) keeps all copy at AA
contrast even over a bright frame. The left column carries the title, a lede and a 2x2 list of
skills. Bottom-right, a "Now playing" control shows four progress bars (coral fill, clickable), the
clip title, the model in teal and a "Show the prompt" disclosure. Cycling pauses when the section
is off screen, the tab is hidden, the prompt is open or reduced motion is on. Only the active and
next clip are preloaded.

### Case study (`.case`)
Two columns, 7:5, media and text, alternating sides (`.case-flip`). Sits inside `.band-light`.
Key facts are a definition list with a 2px coral left rule. Awards are a line of bold text led by
a small coral triangle.

### YouTube facade (`.yt`)
Thumbnail plus a coral triangle play button. The iframe (youtube-nocookie) loads only on click.

### Story band (`.story`)
Dark section over a dimmed video loop (35% opacity, top and bottom fade to black). Big numbers in a
four-column row (two on mobile) with the label in muted text underneath.

### Contact (`.contact`)
Dimmed video background with a radial vignette, a wide question as the headline, the email address
as the single big coral element with a 3px underline, then a plain text row of social links.

## 5. Layout

- Max content width `1320px`, side gutter `clamp(16px, 4vw, 56px)`.
- Left-aligned throughout. Centred text is reserved for the Wacky Code mini-apps.
- Section padding scales with `clamp(72px, 9vw, 128px)` or similar; heroes are `100svh` (home) and `72svh` (inner pages).
- Grids: intro 5:7, case 7:5, teasers 1:1, everything single column under 900px.
- Corners are square. The only radius in the system is zero.

## 6. Depth and elevation

No shadows. Hierarchy comes from surface change (`ink` to `carbon` to `paper`), scrims over video
and borders in `--ash`. Hover states change colour or border, never lift or glow.

## 7. Motion

- **One orchestrated moment per page.** On the home page it is the triangle opening into the hero video. Do not add scroll-triggered fade-ins to sections.
- The Lab crossfade is ambient footage, not an entrance effect, and it must stay slow: no cut faster than 6s, no transform faster than the clip itself.
- Background loops play only while on screen (IntersectionObserver) and are muted, looping and `playsinline`.
- User-triggered motion is welcome: menu wipe, prompt reveal, thumbnail zoom on hover.
- `prefers-reduced-motion: reduce` disables all animation and transitions, removes the hero clip-path and stops autoplay. The posters must still look intentional on their own.

## 8. Video and imagery

### Producing a loop
- Text-to-video, 5 to 6 seconds, 16:9, no audio. Hero at 1080p, everything else at 720p.
- Prompt recipe: subject in a pure black void or darkness, coral-orange rim light, high contrast, deep blacks, film grain or haze, slow continuous motion, "no text, no logos, no people" unless people are the point.
- Triangles, glass, light streams and the magpie are on-brand subjects. Avoid stock-looking scenes (offices, laptops, handshakes, glowing brains).
- Keep the subject off the left third of hero clips; that is where the headline sits.

### Shipping a loop
- `tools/fetch_lab_videos.py` downloads, re-encodes (H.264, CRF 26, `+faststart`, max 1920px or 1280px wide) and writes a JPG poster.
- Every clip needs `static/video/<slug>.mp4` and `<slug>.jpg`.
- Every clip in the Lab rotation needs its real prompt and model in `LAB_CLIPS`. Do not paraphrase a prompt into something it wasn't.

### Photography
The portrait is black and white (`grayscale(1)`) over the coral triangle. Third-party logos sit on
`--bone` tiles so they read on dark.

## 9. Writing

- First person, plain and direct. Short sentences, active voice.
- No em dashes. Use commas, colons or parentheses.
- Title is "AI Creative Producer". Current employer: Kleinanzeigen. Past work is described as past.
- Only state numbers that are documented (15M+ views, 17K+ students, ~200 assets a month, 77K/20K/10K followers). Do not round up.
- Credit generated media honestly: say it was generated and name the model.

## 10. Agent prompt guide

### Quick reference
```
background  #000000   surface #141414   border #2A2A2A
text        #EBE9E6   muted   #9A9894
accent      #EE6C4D   AI-meta #3FA7A1
paper       #EFEFED   paper-text #3A3A38   paper-link #B2421F
font        Archivo variable, headlines wdth 125 / wght 800, body wdth 100 / wght 400
radius 0, shadows none, one triangle motif
```

### Example prompts
- "Add a new case study for <project> to the Work page using the `.case` component inside `.band-light`, video on the left, three facts as a `.facts` list."
- "Add a Lab clip: generate a 5s 720p loop following section 8, then add it to `LAB_CLIPS` with its exact prompt."
- "Create a new page in the site's style: 72svh video page hero, wide 800-weight title, sections from section 4 only."

### Before you ship, check
1. Is there more than one animated entrance on the page? Remove the extras.
2. Does any text sit on video without a scrim?
3. Is teal used for anything that is not AI metadata?
4. Any em dashes, all-caps labels, or rounded corners?
5. Does the page still look right with reduced motion and with videos missing (posters only)?
