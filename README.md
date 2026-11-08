# GridTracker for Mere Mortals

A busy FT8 band, as WSJT-X shows it, is
a waterfall and a scrolling list of
text. The stations are in there —
callsigns, reports, grid squares — but
not in a shape that answers the
questions you are actually asking.
Where is that station? Have I worked
that grid? Who just called me, and is
the band open anywhere interesting?
**GridTracker** takes those questions
over: it listens to the reports WSJT-X
sends, reads your log file, and draws
the answers — a live map of pins and
paths, a roster of who is on right
now, and running totals for the awards
you chase.

One rule governs everything it shows,
and this guide states it in chapter 1
and keeps pointing back to it:
**GridTracker knows only what it is
told — it hears WSJT-X's reports and
your log file, and everything on its
map is those reports, believed.** A
station it was never told about does
not exist for it. A wrong grid in a
report is a wrong pin on the map, drawn
with full confidence. Its award totals
are only as true as the log you feed
it. None of that makes the program
dishonest; it makes it a listener and
a ledger, not a radio — and the guide
reads it that way throughout.

The lab behind this guide ran the real
thing: **GridTracker2 2.261019.5**, the
project's official Linux package from
its own download server, unpacked and
run under a virtual screen with an
empty home directory. The lab verified
the package three ways against the
window's own version line; read the
program's source out of its own
package, including the WSJT-X message
parser, and took the protocol chapter
from that code; watched the first run
for two minutes — the listener binding
UDP port 2237, the `waiting for
message` window, the state folders and
log it creates; watched it download
its callsign databases; and read the
full settings file it wrote on a clean
exit, 37 sections of real keys.

What the lab could not do, it did not
fake. Its sandbox blocks outbound UDP
entirely, so the probe datagrams the
lab wrote — a fictional Status and
Decodes in the parser's own format —
never reached the running program, and
the map's reaction to live traffic is
described from the documentation and
the code, not from a screenshot of a
populated map. Nothing touched a radio,
no real log was used, and nothing was
uploaded anywhere. Every example
station in this guide is invented.
`criteria.md` keeps the full ledger of
what was run and what was only read.

## What this guide covers

- [**What GridTracker is**](what-gridtracker-is.md) —
  the scrolling-list problem, the
  companion that reshapes it, and the
  one rule
- [**The moving parts**](the-moving-parts.md) —
  the listener, the map, the roster,
  the logbook view, lookups, alerts,
  and settings
- [**Installing GridTracker**](installing-gridtracker.md) —
  the official package the lab used,
  how it is laid out, and the version
  check every install must pass
- [**The first run**](first-run.md) —
  the empty window, the state it
  creates, and what a clean exit saves
- [**The WSJT-X link**](the-wsjtx-link.md) —
  UDP 2237 and the Network Message
  format, read from the program's own
  parser — plus the probe the lab
  could not send
- [**The map**](the-map.md) — pins,
  paths, shaded grids, filters, and
  the offline tiles inside the package
- [**The Call Roster**](the-call-roster.md) —
  the reports as a table, wanted and
  worked colours, and the log behind
  them
- [**Your logbook in GridTracker**](your-logbook-in-gridtracker.md) —
  where the view of your past comes
  from, and why its totals can argue
  with your real logbook
- [**Logging onward**](logging-onward.md) —
  sending contacts to real loggers and
  web logbooks, and the credentials
  that ride along
- [**Lookups and databases**](lookups-and-databases.md) —
  Callook and QRZ, and the 20 MB of
  callsign lists the program fetches
  itself
- [**Alerts**](alerts.md) — spoken and
  sounded warnings, and what an alert
  is really claiming
- [**Spots, feeds and offline working**](spots-feeds-and-offline.md) —
  PSK Reporter, other people's spots,
  POTA and SOTA, and what survives
  without a network
- [**Settings that matter**](settings-that-matter.md) —
  the real settings file, read whole,
  and the keys that decide behaviour
- [**The neighbours**](the-neighbours.md) —
  WSJT-X, JTAlert, the real loggers,
  and PSK Reporter, characterised
- [**Limits**](limits.md) — a listener
  and a ledger, not a radio, and the
  limits of this guide's own evidence
- [**Troubleshooting**](troubleshooting.md) —
  the silent window, the wrong pin,
  and the totals that disagree
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Operating WSJT-X itself, radio
technique, or antenna work — this
guide starts where the decoder's
reports leave the decoder. Contest
operation and the deep award rules are
named where they belong and left to
their own rulebooks. And it does not
teach you to trust the map more than
the reports it is drawn from; several
chapters teach the opposite.

## How to use this guide

Read chapter 1 for the rule and
chapter 2 for the map of parts;
chapters 3 and 4 get the program
installed and through its first run,
and chapter 5 takes the link apart —
read it before your first session with
both programs running, because its
port-matching checks are the ones
troubleshooting will send you back to.
The lab lives in `gridtracker-lab/`:
its transcripts in `transcripts/`, its
fictional ADIF fixture in `fixtures/`,
the first-run screenshot as
`first-run-window.png`, and the WSJT-X
probe sender as `send_wsjtx.py` —
yours to run on a machine where
loopback UDP is allowed. Its distilled
commands are `examples/commands.txt`
and its notes `examples/lab-notes.txt`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Text Processing for Mere Mortals](https://paulsullivan33-dev.github.io/text-processing-for-mere-mortals/)
- [Vim for Mere Mortals](https://paulsullivan33-dev.github.io/vim-for-mere-mortals/)
- [Markdown for Mere Mortals](https://paulsullivan33-dev.github.io/markdown-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/gridtracker-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/gridtracker-for-mere-mortals/blob/main/LICENSE-CODE).
