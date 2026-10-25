# Higher or Lower: Follower Count Game

A terminal guessing game where players compare two public figures, brands, or organizations and choose which has the larger follower count.

## Features

- Random account comparisons
- Duplicate-choice prevention
- Running score across correct answers
- Bundled comparison data and ASCII artwork

## Run

```bash
python main.py
```

No third-party packages are required. The follower counts are stored locally in `game_data.py` and represent a static learning dataset rather than live social-media data.

## Structure

- `main.py` — game logic
- `game_data.py` — account descriptions and follower counts
- `art.py` — terminal artwork
