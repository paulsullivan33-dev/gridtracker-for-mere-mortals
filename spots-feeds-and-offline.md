# Spots, feeds and offline working

Outcome: you know which parts of
GridTracker depend on the internet and
other people's reports, which parts are
yours alone, and how the program behaves
when the network goes away.

*Verification note: the network features
in this chapter need live services; the
lab's sandbox broke the program's TLS
connections and blocked its UDP, so the
behaviours are documented-only. The
offline bundle — map tiles inside the
package — was inventoried for real
(transcript t01).*

## Spots out: telling the world what you heard

A **spot** is a small public claim:
"station X heard station Y, at this
frequency, at this time." GridTracker
both makes and consumes them.

- **PSK Reporter** receives reception
  reports of the stations your WSJT-X
  decodes. Inside the package, the
  mechanism is plain: a bundled MQTT
  client connects to
  `mqtt://mqtt.pskreporter.info:1883`
  and publishes your decodes, tagged
  with your call and grid from the
  Status reports. The project's own
  comment in that file says the topic
  names are built from your callsign
  with "/" standing in for "." — your
  reports go out under your name.
- **Other GridTracker users** can see
  your activity through the program's
  own online service (the OAMS settings:
  `app.spottingEnable` is true in the
  fresh defaults), and you can see
  theirs.

Both are on the sending side of
chapter 1's rule: the spots are only
your reports, repeated to strangers,
with your callsign attached.

## Feeds in: other people's reports

The Feed Roster is the Call Roster's
cousin, fed not by your decoder but by
incoming spot streams — DX cluster and
skimmer spots and the project's feed —
merged, aged (a spot is kept 300
seconds by default, `app.feedMaxAge`),
and filtered by the same wanted-logic.
On top of the feeds sit two activity
layers:

- **Parks on the Air (POTA)** —
  activators at parks, refreshed from
  the POTA site every five minutes,
  drawn on the map, with the program
  able to spot a park station you work
  back to the site. On by default in
  the saved settings.
- **Summits on the Air (SOTA)** —
  the same treatment for summit
  activators arriving via the feeds;
  off by default, newer, and described
  at length in the package's changelog.

A feed spot that names a park or summit
can substitute its location for a
station that sent no grid — useful,
and another entry in the rule's ledger:
that pin is the *spot's* claim about
where the activator is, not the
activator's own report.

## Offline: what still works in a field

The home page advertises a 100% offline
mode for field events, and the package
backs the claim structurally. The
listener, the parser, the roster, the
log view, and the alerts are all local.
The map has bundled offline tile sets
inside the program (chapter 6), the
callsign databases are files already on
disk (chapter 10), and the settings
carry a plain switch, `map.offlineMode`.
What goes dark without a network is
exactly what you would list: online
lookups, map tiles beyond the bundled
sets, spots in either direction, feeds,
LoTW downloads, and the version check
the lab watched fail without
consequence. A field laptop running
GridTracker is a listener and a ledger
again — which is the shape of the whole
program, with the internet as an
optional adviser.

Check: turn on offline mode, restart
the program, and confirm the map, the
listener on port 2237, and your loaded
log all still work while the lookup
window reports it cannot reach its
service. That split is the chapter in
one experiment.
