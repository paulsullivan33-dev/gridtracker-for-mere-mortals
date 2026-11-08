# The neighbours

Outcome: you can place GridTracker
among the tools around a digital-mode
station, and say what each neighbour
does that it does not — characterised,
not benchmarked.

## WSJT-X (and JTDX)

The decoder itself. It receives the
radio, decodes the signals, runs the
contacts, and writes the log. GridTracker
exists only because WSJT-X publishes
its reports; remove GridTracker and
WSJT-X works exactly as before, while
removing WSJT-X leaves GridTracker
sitting at `waiting for message`
forever. JTDX, a WSJT-X offshoot,
speaks the same network protocol and
feeds GridTracker the same way.

## JTAlert

The Windows companion with the same
instincts: decodes as alerts, worked-
before tracking, and a grid of stations
to chase. If GridTracker is the map-
first expression of the idea, JTAlert
is the alert-first one. It is
Windows-only, which is the plainest
reason a Linux or Mac station lands on
GridTracker instead.

## The real loggers

Log4OM, N3FJP's AC Log, Ham Radio
Deluxe, DXKeeper and friends are where
chapter 9 sends the contacts. Their
centre of gravity is the permanent
record — data entry, QSL management,
award submissions — where GridTracker's
is the live picture. The two kinds of
program are complements with an overlap
both sides politely ignore: the logger
can show a map, and GridTracker keeps a
log view, but each is the other's
backup plan, not its replacement.

## PSK Reporter

The website where spots gather. On its
own, in a browser, it answers "where
was my signal heard?" from the reports
of thousands of stations. GridTracker
both feeds it (your decodes, chapter
12) and draws the same idea live around
your own station. Think of PSK Reporter
as the archive of everyone's reports,
and GridTracker as your personal,
live, opinionated view of yours.

## CQRLOG and the Linux bench

On Linux, CQRLOG is the established
full logbook, and programs like WSJT-X
itself, `fldigi` for the wider digital
modes, and radio control libraries sit
underneath everything here. None of
them draws this particular map from
these particular reports; that small,
specific job is GridTracker's alone on
this platform.

Check: for each neighbour, say what
stops working in your station if it
vanishes. Anything whose answer is
"nothing about the radio" belongs to
the same layer as GridTracker — the
believing layer, built on reports.
