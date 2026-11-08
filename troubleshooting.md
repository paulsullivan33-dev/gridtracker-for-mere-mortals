# Troubleshooting

Outcome: the six troubles a GridTracker
station actually meets, each with the
check that separates its causes.

## "Waiting for message", forever

The ear is open and nothing arrives.

- **Ports must match.** GridTracker's
  receive port (`app.wsjtUdpPort`,
  normally 2237) and WSJT-X's UDP server
  port are the same number or nothing
  works. Check both; check with
  `ss -lunp | grep 2237` that the
  listener exists at all.
- **WSJT-X must be told to send.** In
  its Reporting settings the UDP server
  is enabled and the "accept UDP
  requests" side is sane; a fresh WSJT-X
  with reporting off is silent by
  choice.
- **Two programs, one port.** Another
  listener holding 2237 first can starve
  GridTracker — the parser gives up on a
  bind error and the status line shows
  it. Close the rival, restart
  GridTracker.
- **Started too close together.**
  Datagrams sent while GridTracker is
  still loading are discarded by design
  (chapter 5). Restart WSJT-X's
  reporting — or just wait for the next
  heartbeat and Status.

## The map is empty but the roster is not

A filter, not a failure. Read the Map
View Filters in the main window: Band,
Mode, Data, or Award is excluding what
the roster shows. Set them back to
Mixed / Logbook & Live / None and the
two views agree again.

## A station is pinned in the wrong place

Believe the report, not the pin. The
grid came from the station's own
message or Status, from a spot, or
from a lookup filling a gap (chapters
6 and 10). Portable stations sending a
home grid are the classic case. The
fix is at the sending end; GridTracker
is faithfully drawing what it was told.

## "New" stations you have worked for years

The log view is partial (chapter 8).
Load the full ADIF export from your
master logger, confirm `loadAdifAtStartup`
if you want it every time, and check the
QSO counter against the file's record
count before blaming the colours.

## Counters disagree with Logbook of the World

Different sets again: the LoTW download
is dated, GridTracker's view includes
unconfirmed contacts, and the QSL
counter counts what the view holds.
Refresh the LoTW download, then compare
like with like — confirmed against
confirmed.

## It will not start, or starts and vanishes

- Read its own log first:
  `~/.config/GridTracker2/logs/main.log`.
  A first run's `Could not load:
  app-settings.json / Defaults will be
  applied` is normal, not an error.
- A damaged settings file is the usual
  self-inflicted wound: move
  `app-settings.json` aside, restart,
  and the program rebuilds it from
  defaults; re-import your export
  afterwards.
- On Linux, the package needs its
  desktop libraries (chapter 3 lists
  them); a binary that will not start
  under a minimal window manager is
  usually missing one, and the terminal
  error names it.

Check: work the "waiting for message"
list top to bottom on any station you
run. Four of its five items can be
verified without touching the radio —
which is fitting, for a program that
never touches one either.
