# The Call Roster

Outcome: you can use the roster window
to answer "who is on, who do I want,
and who have I already got" — the
questions the map answers slowly.

*Verification note: the roster is a
separate interactive window fed by live
datagrams. The lab could not deliver
datagrams (chapter 5), so this chapter
is documented-only, from the project's
manual and the roster code and defaults
inside the package.*

## A table of the reports

Open the roster and every station the
reports name gets a row: callsign,
grid, country (DXCC), state or county
for US stations, band, mode, signal
report, how long since last heard
(Age), and a column of flags — LoTW
user, eQSL user, OQRS — answered from
the downloaded databases of chapter 10.
Rows appear as Decode reports arrive
and age out as the reports stop. It is
the same information as the map, in
the shape a hunter actually works in:
sortable, filterable, scannable.

The columns are yours to arrange. The
current version keeps each roster's
column set, order, visibility, and
colours in Settings under a Columns
tab — the package's own changelog
describes the change in detail — and
the saved settings carry a `roster`
section of 23 keys and a separate
`feedRoster` section for the feed
roster of chapter 12.

## Wanted, worked, and the log behind the colours

A row's colour is GridTracker's opinion
of the station *for you*: never worked,
worked but unconfirmed, confirmed, or
**wanted** — matching something on your
want list (a grid, a country, a state,
a callsign). Every one of those
judgements is a lookup in the logbook
view of chapter 8 against the reference
you choose — this band and mode, this
band any mode, any band any mode, and
so on. The roster's honesty is exactly
the log's honesty: a contact missing
from the loaded log reads as "new",
and the roster will cheerfully send you
to work an old friend again. That is
chapter 1's rule wearing a table's
clothing.

Two roster habits worth knowing:

- **Band changes clear the deck** —
  an optional setting (`clearRosterOn
  BandChange` in the code) empties the
  roster when the Status report says
  the band changed, because yesterday's
  40-metre crowd is not today's.
- **Clicking can act.** A click on a
  row can send WSJT-X the instruction
  to call that station — the one place
  GridTracker talks back — and the
  Feed Roster lets a click on a park or
  summit spot start a manual log entry.
  Convenient, and worth remembering:
  a listener that can start contacts is
  a listener whose clicks you should
  mean.

## Exceptions and ignores

The settings file keeps lists with
names that explain themselves:
`ignoredCalls`, `ignoredGrid`,
`ignoredDxcc`, `ignoredCQ`, and more.
Stations matching them are hidden or
de-emphasised. They are the roster's
answer to the regulars you have worked
a hundred times and the beacons you
never intend to answer.

Check: sort the roster by Age and watch
a row fade as its station goes quiet;
then find the same callsign on the map.
One report stream, two views — if a
station is in one and not the other,
a filter in one of them is the reason.
