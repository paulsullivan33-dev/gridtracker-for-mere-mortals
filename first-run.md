# The first run

Outcome: you know what a fresh
GridTracker2 window is telling you
before WSJT-X says a word, where the
program keeps its state, and what it
writes when it leaves.

Everything in this chapter was watched,
not imagined: the lab ran the real
program under a virtual screen with an
empty home directory, photographed the
window at 60 seconds, and read the
files afterwards (transcripts
`gridtracker-lab/transcripts/t02-first-launch.txt`
and `t03-saved-settings.txt`, screenshot
`gridtracker-lab/first-run-window.png`).

## The window before any message

The first-run window is two halves. On
the left, a pale world map with zoom
controls and a scale bar — pale because
a fresh program has no station of its
own yet and little to draw. On the
right, the control column:

- The title block reads **GridTracker2**,
  then `0.000.000 Hz (?)` — no frequency,
  because no Status report has arrived
  — and the current UTC date and time.
- A green band says **waiting for
  message**. That is the whole state of
  a fresh install: ear open, nothing
  heard. Below it, `...no data yet...`.
- The counters: **Rx Calls 0, QSO 0,
  Rx DXCC 0, QSL 0**. Received stations,
  logged contacts, countries heard,
  confirmations — all zero, honestly.
- **Map View Filters**: Band, Mode and
  Propagation all *Mixed*, Data set to
  *Logbook & Live*, Award *None*. These
  decide which of the things it is told
  actually get drawn; chapter 6.
- A grid of buttons — the features of
  chapters 6 to 12, one icon each — and
  at the bottom, the version line.

Leave it sitting and two things happen
quietly. The UDP listener binds port
2237 within about ten seconds (the
operating system showed it held by the
program for the whole two-minute run).
And the program phones home in its own
way: it checks for a new version, and
on a later run it downloads its
callsign databases (chapter 10). In the
lab's sandbox the version check failed
on a certificate error because of the
sandbox's network path; the program
carried on regardless, which is the
right behaviour and worth seeing once.

## Where the state lives

With its home redirected, the program
created exactly one tree that matters:
`~/.config/GridTracker2/`. Inside it,
alongside the browser engine's caches:

- `Ginternal/` — the program's own
  drawer: the settings file, the
  downloaded callsign databases, and
  `spots.json`, its record of spots,
  which after an idle run reads,
  completely, `{"spots":{}}`.
- `logs/main.log` — its log file. A
  first run's most informative lines are
  its confessions: `Could not load:
  .../Ginternal/app-settings.json` and
  `Defaults will be applied`. First run
  means there is no settings file yet,
  and the defaults are a real, readable
  list baked into the program (chapter
  13 quotes them).
- Folders it prepares for later: `Backup
  Logs`, `Call Roster Scripts`,
  `Screenshots`, `Extra Media`.

One more first-run behaviour, spotted
in the log: the program goes looking
for WSJT-X's own configuration, to learn
the UDP port and callsign you already
set there — in the lab it tripped over
the empty home directory while scanning
for log folders and logged the error
rather than dying of it. On a machine
where WSJT-X is already set up, this
is why GridTracker so often "just
works" with no port typing at all
(chapter 5).

## What a clean exit writes

Killed mid-run, the program leaves the
settings unwritten. Closed properly —
the lab's second run ended it with a
normal terminate signal — it saves
`Ginternal/app-settings.json`, 25,366
bytes of JSON: every section of chapter
13, with the defaults it had applied
now written down as your settings,
including the resolved UDP port, 2237.
That file is the program's memory, and
the settings window's Export button
copies the same material to
`~/Documents/gt_settings.json` for
backup or a move to another machine.

Check: start GridTracker2 with WSJT-X
closed. Within a minute you should see
`waiting for message`, four zero
counters, and — with `ss -lunp | grep
2237` in a terminal — the program
holding its port. If the band says
anything else, WSJT-X is already
talking; chapter 5 explains what it is
saying.
