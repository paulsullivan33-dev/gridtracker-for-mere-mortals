# What GridTracker is

By the end of this chapter you can say,
in one sentence, what GridTracker does
with what it is told — and state the one
rule that decides how much of its map
you should believe.

## The screen a digital operator stares at

Run WSJT-X on a busy band and you get a
waterfall and a list of decoded text:
callsigns, signal reports, grid squares,
scrolling past every fifteen seconds.
The information is all there, but it is
in the wrong shape to answer the
questions you actually have. *Where is
that station? Have I worked that grid
before? Is the band open to anywhere
interesting? Who just called me?*

**GridTracker** is the companion program
that reshapes it. It listens to the
reports WSJT-X sends out, reads your
log file, and draws the result: a live
world map with pins and paths, a table
of who is on the air right now (the
**Call Roster**), counters of what you
have received and worked, and running
totals for awards — all built from
those reports. Its own home page sums
up the original idea in one line:
"GridTracker listens to traffic from
WSJT-X and displays it on a map. It
will also load ADIF log files."

Nothing in that sentence involves a
radio. GridTracker does not receive,
decode, or transmit anything itself.
WSJT-X does the radio work; GridTracker
believes what WSJT-X tells it and draws
the picture. The current line is
**GridTracker2** — a complete rewrite
of the original, installed in its own
place — and it is the version this
guide covers. This guide's lab ran
**GridTracker2 2.261019.5**, the
current official Linux package at the
time of writing.

## The rule: it knows only what it is told

Everything GridTracker shows you
arrives from exactly two sources: the
reports WSJT-X sends it, moment by
moment, and the log file you feed it.
There is no third source of truth. So:

> **GridTracker knows only what it is
> told. Everything on its map is a
> report it heard, believed. A station
> it was never told about does not
> exist for it, and a wrong grid in a
> report becomes a wrong pin on the
> map.**

This is not a flaw to apologise for; it
is the tool, working as described. But
it shapes everything in this guide:

- A decode with a mistyped or made-up
  grid draws a confident line to the
  wrong place, and the program has no
  way to know.
- "Worked before" means "present in
  the log you loaded" — no more. Leave
  half your log unloaded and the map
  will happily call old friends new.
- An award total is arithmetic over
  that same log. Feed it a partial log
  and you get a partial truth, neatly
  coloured.

Later chapters point back to this rule
where it bites: the map chapter, the
logbook chapter, and the limits
chapter, which is the rule written out
in full.

## What it costs and where it runs

GridTracker is free, written and
maintained by the GridTracker team,
and runs on Windows, macOS, and Linux.
On Linux it arrives as a package for
your distribution's package manager
(chapter 3). Under the skin it is an
**Electron** application — a bundled
web browser engine with the program
written as web pages and scripts —
which is why the download is over
100 MB and why, later, this guide can
read its own source code out of the
package and quote it.

Check: say the two sources everything
on GridTracker's map comes from, and
then say the rule out loud once. If you
can do both, you have this chapter.
