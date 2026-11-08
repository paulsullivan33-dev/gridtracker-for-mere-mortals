# Limits

Outcome: you can recite what GridTracker
cannot do, and recognise the failures
that are not failures — the program
believing exactly what it was told.

## It is a listener and a ledger, not a radio

GridTracker cannot transmit, cannot
decode, and cannot verify that a
contact happened. It owns no receiver
and no opinion about the ionosphere.
When the map shows a station, it shows
that a *report named* that station.
When a contact enters its view, a
report said WSJT-X logged one. The
program trusts those reports
completely, because trusting them is
its entire design; everything it adds —
colour, distance, totals — is
decoration on trust.

## "Worked before" is only as true as the log you fed it

Award counts, roster colours, alert
judgements, shaded grids: all of them
are arithmetic over the log view of
chapter 8. A partial log produces
confident, complete-looking, partial
answers, with no banner saying the log
was partial. The program cannot know
what your real history is; it can only
know what it was given. If you keep one
habit from this guide, let it be
loading the full export.

## Its databases and maps are other people's data

Callsign flags, states and counties,
country names, lookup results, feed
spots, the base map itself: all are
fetched from services run by others,
refreshed on their schedules, and
exactly as accurate as those services
are. A station missing from a list is
treated as a non-member; a wrong entry
upstream becomes a wrong label here,
with no local way to appeal.

## It sees one station's reports, from one chair

One GridTracker hears what its WSJT-X
instances report. It has no view of the
band beyond them — not the stations too
weak to decode, not the other modes,
not the band next door. The map looks
like the world; it is one receiver's
mail.

## Interaction needs a person; verification needs a radio

Finally, the limits of this guide's own
evidence, stated as plainly in
`criteria.md`: the lab ran the program
for real and read its code and files,
but delivered no live datagrams (the
sandbox blocked them), worked no radio,
clicked no map, and uploaded nothing
anywhere. Everything on-air in these
chapters is the project's documentation
and the program's own code, labelled as
such. The program's claims deserve a
real station's test; its *files* have
already had theirs.

Check: pick any strong claim in
chapters 6 to 12 — an award total, a
roster colour, a spot — and trace it
back to the report or file it came
from. If you can do that for each,
you are using the program with its
limits in view, which is the only safe
way to use it at all.
