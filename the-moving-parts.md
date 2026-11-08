# The moving parts

Outcome: you can name the parts inside
GridTracker, what passes between them,
and which part is responsible when
something on screen surprises you.

## The listener

The program's ear is a **UDP listener**.
UDP is one of the two basic ways
programs send messages over a network:
small self-contained packets
(**datagrams**), no connection, no
delivery guarantee. WSJT-X sends its
reports this way, to this machine, on
port **2237** by default, and GridTracker
binds that port and waits. This guide's
lab watched the real program do it:
within about ten seconds of launch, the
operating system showed GridTracker2
holding UDP port 2237 (transcript
`gridtracker-lab/transcripts/t02-first-launch.txt`).

Each datagram is a **WSJT-X Network
Message** — a fixed binary format the
app parses field by field. The kinds
that matter day to day:

- **Heartbeat** — "I am here, this is
  my name." Sent when WSJT-X starts and
  periodically after.
- **Status** — the state of one WSJT-X
  window: frequency, mode, the calls at
  both ends, both grids, whether it is
  transmitting or decoding.
- **Decode** — one decoded station:
  time, signal-to-noise ratio, the
  message text itself, such as
  `CQ N0CLL FN31`.
- **QSO Logged** and **Logged ADIF** —
  a finished contact, first as fields,
  then as a ready-made log record.

Chapter 5 takes this link apart in
full, from the app's own parser code.

## The map

The map is the main window: a world
map with your station at the centre,
pins for stations being heard, and
paths drawn between stations that are
talking to each other. Overlays add
the day/night line (the **greyline**),
worked and confirmed grid squares, and
award layers. It is drawn from the
Status and Decode reports plus the log
— chapter 6.

## The Call Roster

The roster is a second window: the
same live reports as a sortable table —
one row per station heard, with
columns for callsign, grid, country,
band, mode, signal report, age, and
whether you want or have worked them.
Where the map answers "where?", the
roster answers "who, exactly, and
should I care?" — chapter 7.

## The logbook view

GridTracker keeps its own view of your
contacts, built from ADIF log files —
**ADIF** is the standard text format
amateur logbooks exchange, a list of
records made of named fields. It scans
for WSJT-X's own log, loads files you
point it at, and can fetch confirmed
records from Logbook of the World. The
project's own manual is blunt about the
role this plays: "GridTracker is a log
viewer, not a logging program."
Chapter 8 covers what it loads and
chapter 9 what it can send onward to
real logbooks.

## Lookups and databases

A callsign alone says little, so the
program enriches it: online lookup
services (Callook by default, QRZ and
others with accounts) and four
downloadable databases — the US FCC
callsign list, and lists of Logbook of
the World, eQSL, and Club Log users —
which the lab watched it fetch on its
own, about 20 MB in all, on a later
first run (transcript
`gridtracker-lab/transcripts/t03-saved-settings.txt`).
Chapter 10.

## Alerts, spots, and feeds

On top of the reports sit the noisy
parts: spoken and visual **alerts**
when something you want appears,
reception **spots** shared with PSK
Reporter and other GridTracker users,
and incoming **feeds** of other
people's spots, including Parks on the
Air and Summits on the Air activations.
Chapters 11 and 12.

## Settings and state

Everything above is steered by one
settings file,
`app-settings.json`, kept in the
program's own folder under your config
directory. The lab read the real file
the program wrote on a clean exit:
37 top-level sections, from `app` and
`map` to `roster`, `awardTracker`, and
the logbook integrations. Chapter 13
reads the keys that matter.

Check: name the part responsible for
each of these — hearing WSJT-X (the
listener), showing where a station is
(the map), deciding "worked before"
(the logbook view over your log file).
