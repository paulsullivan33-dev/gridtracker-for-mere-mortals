# The map

Outcome: you can read the main window —
what a pin, a path, and a coloured grid
square each mean, and which reports put
them there.

*Verification note: this chapter
describes the map's behaviour from the
program's documentation and its own
code and defaults. The lab photographed
the empty first-run map (chapter 4);
a populated map needs live datagrams,
which the lab could not deliver
(chapter 5), so live map behaviour is
documented-only.*

## What gets drawn

- **Your station** sits at the grid
  from the current Status report — or,
  until one arrives, from the Center
  Gridsquare setting. Every distance
  and bearing is measured from it.
- **Pins** mark stations in the reports:
  a station decoded calling CQ appears
  at the grid its message carried; a
  station in a contact appears at the
  grid from the exchange. No grid in the
  report, no precise pin — the Map
  settings offer a fallback that places
  grid-less callsigns at the centre of
  their country, which is a guess
  wearing a pin's clothing, and the
  setting (`qrzDxccFallback` in the
  saved defaults) is off unless you
  turn it on.
- **Paths** are lines between the two
  ends of a conversation the reports
  describe — who is calling whom. With
  animation on (the default) the line
  crawls in the direction of the call:
  the "running ants" of the settings.
- **Grid squares** shade as they are
  heard, worked, and confirmed, in the
  colours of the Grids settings. Live
  squares fade as they age — the Live
  Grid Decay — so a bright square is a
  recent report and a dim one is going
  stale. The default decay in the saved
  settings is 300 seconds.

## The filters decide what survives

The first-run screenshot shows the Map
View Filters in their fresh state:
Band, Mode, and Propagation *Mixed*
(everything passes), Data *Logbook &
Live* (both the log and the live
reports are drawn), Award *None*. These
five choices are the difference between
a map of "everything heard" and a map
of "grids I still need on 20 metres" —
and a common source of confusion,
because a filtered-out station vanishes
without any message saying why. When
the map looks wrongly empty, the
filters are the first suspects, before
the radio.

## Layers and looks

Thirty-odd base maps are offered
(Esri, OpenStreetMap variants, satellite
and dark styles among them); the saved
defaults name `Street by Esri
(English)` for the day map and a dark
Esri style for the optional automatic
night map. Overlays add the greyline,
the Moon's position, range rings, US
radar weather, and the award layers of
chapter 8. Two details from inside the
package are worth knowing:

- **Some maps work offline.** The
  program bundles tile sets inside
  itself — the lab found offline tile
  pyramids for a toner-style map and a
  satellite map, thousands of small
  images, plus a game-style map — and
  the settings carry separate
  "offline" choices for day and night
  maps. Chapter 12 puts this together
  with the offline mode.
- **The map is a web page.** Zoom,
  pan, and click behaviour are the
  usual web-map habits, and clicking a
  grid square lists the stations the
  reports placed in it — the mouseover
  popups of the Grids settings do the
  same on hover.

## The rule, on the map

A pin is a claim, repeated. If a
station sends a grid that is wrong —
a typo, a stale setting at their end,
a portable operation reported from
home — the map draws the wrong place
with the same confidence as the right
one, the roster lists it, and the
distance and bearing are computed to
the wrong square. GridTracker has no
independent way to check; it was told,
and it believed. Treat a surprising
pin as a surprising *report*, and you
will read the map the way it deserves.

Check: hover or click a shaded grid
square and read the station list the
program shows. Every name there is a
report it heard — find one in the Call
Roster (chapter 7) and confirm the
grid matches what the station sent.
