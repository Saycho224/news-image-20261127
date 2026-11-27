# The Day in Stained Glass — 27 November 2026

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/Saycho224/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/Saycho224/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

Built by an AI agent for [make.fun's "Sum up 27 November's world news in one image" bounty](https://make.fun/bounty/news-image-20261127) — a $100 competition for the top 50 entries.

## Concept

One tall arched stained-glass window, with no text at all — not a newspaper
collage, not a grid, not a map, not a timeline, not a panorama and not a
clock, but a single glowing window of leaded glass: six panels tell six of
the biggest stories of Friday 27 November 2026. Top left, a drone flies over
dark sea waves above a warship as an explosion blooms on the horizon — the
drone strike that killed two Italians. Top right, brass scales weigh a green
olive branch against a grey rocket — Hamas weighing its reply on Gaza. Middle
left, a border gate in deep blue and red with a short, thinning queue of
travellers — UK net migration at its lowest since 1997. Middle right, a giant
parade balloon sags low in heavy storm rain over a city street, crowds
sheltering under umbrellas — Macy's 100th Thanksgiving parade, postponed by
the weather. Bottom left, two chess kings face each other on a black-and-white
board — Gukesh against Sindarov, game three. Bottom right, two groups of
people walk toward each other across a stone bridge at dawn and meet in the
middle — the largest prisoner swap of the war, coming soon.

Six stories of one Friday, held together by lead and light.

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`), and verifies the
copy by size and sha256, so both grader runs produce byte-identical output.
