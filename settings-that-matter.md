# Settings that matter

Outcome: you can find, read, and back
up the program's real settings file,
and you know the handful of keys that
decide most of its behaviour.

Most of GridTracker's settings window
is taste — colours, columns, voices.
This chapter is about the file
underneath it, which the lab read in
full: once as the defaults baked into
the program's code
(`src/renderer/lib/settings/defaults.js`
inside the package) and once as the
file the program itself saved on a
clean exit (transcript
`gridtracker-lab/transcripts/t03-saved-settings.txt`).

## The file

```
~/.config/GridTracker2/Ginternal/app-settings.json
```

JSON, grouped in 37 top-level sections.
The ones a mere mortal will meet:
`app` (81 keys), `map` (50), `roster`
(23), `feedRoster` (21), `callsignLookups`
(15), `msg` (12), and one small section
per logging partner — `acLog`, `log4OM`,
`adifLog`, and their kin. Two entries
bookend the file's story: `defaultsApplied:
true`, set when the baked-in defaults
were merged in, and `currentVersion`,
written as a bare number — `22610195`,
the version 2.261019.5 with its dots
removed.

## The keys that decide behaviour

Quoted from the saved file of a fresh,
untouched install:

| Key | Fresh value | What it decides |
| --- | --- | --- |
| `app.wsjtUdpPort` | 2237 | The ear of chapter 5. In the code's defaults it starts as 0, meaning "find it" — from WSJT-X's own configuration, or 2237 — and the resolved number is what gets saved. |
| `app.wsjtIP` | `""` | Which address to bind; empty is the ordinary local case. |
| `app.multicast` | false | Join a multicast group instead of a plain bind (chapter 5). |
| `app.wsjtForwardUdpPort` | 2238 | Where received datagrams are repeated to, when forwarding is enabled. |
| `app.adifBroadcastPort` | 2333 | Where logged records are re-broadcast, when enabled. |
| `app.myCall` | `NOCALL` | Whose station this is, until a Status report says otherwise. |
| `app.myGrid` | `""` | The map's centre, likewise. |
| `app.lookupService` | `CALLOOK` | Which lookup service chapter 10 asks first. |
| `app.loadAdifAtStartup` | false | Whether the log view reloads its file at launch (chapter 8). |
| `app.distanceUnit` | `MI` | Miles, until you say kilometres. |
| `app.spottingEnable` | true | Whether your decodes are spotted onward (chapter 12). |
| `app.feedMaxAge` | 300 | Seconds a feed spot survives. |
| `map.offlineMode` | false | The offline switch of chapter 12. |
| `map.zoom` | 4 | The first-run map's zoom — the whole world, more or less, as the screenshot shows. |

Two lessons hide in that table. First,
the fresh program is not neutral: it
spots onward by default and keeps its
park-hunting on, so a first run is
worth a slow pass through the General
and Features settings before a radio is
involved. Second, the port's journey
from 0 to 2237 is the whole WSJT-X
relationship in miniature — the program
would rather learn your setup from
WSJT-X's files than ask you, and it
falls back to the standard number when
it cannot.

## Backing up and moving

The settings window's Export writes
`gt_settings.json` to your Documents
folder, and Import reads that exact
filename back. Treat the export as a
secrets-bearing file (chapter 9): it
carries your lookup and logbook
credentials in plain text. The lab's
advice is boring and sufficient: keep
one export, keep it private, and
re-export after any session where you
changed something you would miss.

Check: open the file in a text editor,
find `wsjtUdpPort`, and confirm the
number matches the port in WSJT-X's
Reporting settings. Then make one
Export from the settings window and
confirm `gt_settings.json` exists in
Documents.
