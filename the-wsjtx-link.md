# The WSJT-X link

Outcome: you can describe exactly what
flows between WSJT-X and GridTracker,
in which format, on which port — and
you know precisely which part of that
this guide's lab proved, and which part
it could not.

## One direction, one port, no connection

WSJT-X does the sending. In its own
settings (Reporting tab) it names a UDP
server: an address, 127.0.0.1 when both
programs share a machine, and port
**2237**. GridTracker binds that port
and receives. There is no login and no
handshake to configure; if the numbers
match, reports arrive. The project's
settings manual states the same
defaults the lab found in the program:
receive on 2237, forward on 2238.

Two refinements matter in real shacks:

- **Several decoders.** More than one
  WSJT-X (or JTDX) window can report to
  the same GridTracker. The parser tags
  every datagram with the sender's
  chosen name — the *instance* — and
  tracks each separately, which is how
  one map serves two radios.
- **Multicast.** If several programs on
  the network all want the reports, the
  listener can join a multicast group
  instead; it is a settings option, off
  by default (the saved settings show
  `app.multicast = false`).

## The format, from the program's own parser

Because GridTracker2 is an Electron
app, its receiver ships as readable
source inside the package:
`src/renderer/lib/wsjtxUdp.js`. The lab
read it rather than guessing, and the
chapters that follow cite it (transcript
`gridtracker-lab/transcripts/t01-asar-inventory.txt`).
A datagram begins:

1. A **magic number**, four bytes,
   `0xADBCCBDA`. Anything else is
   dropped unread — the parser's first
   test.
2. A **schema number** and a **message
   type** number.
3. The sender's **Id** — "WSJT-X" unless
   renamed — after which the fields of
   that message type follow, each in the
   Qt wire order the code spells out.

The types the parser acts on: **0**
Heartbeat, **1** Status, **2** Decode,
**3** Clear (accepted, no action), **5**
QSO Logged, **6** Close (accepted, no
action), **10** WSPR Decode, **12**
Logged ADIF. Three honest behaviours
fall straight out of the code:

- **Order matters.** A Decode from an
  instance whose Status has not arrived
  is refused (`if (!instance.valid)
  return`). Status is what makes an
  instance real: it carries the band,
  the home callsign, and the home grid
  every later report is measured from.
- **Duplicates are dropped.** The exact
  same datagram twice in a row from the
  same port is ignored; the parser
  keeps the last one to compare.
- **Nothing counts before loading
  finishes.** Datagrams that arrive
  while the program is still starting
  are discarded, not queued.

A Status report, fully spelled out,
carries: frequency in hertz (from which
the band is computed), mode, the other
station's call, the report sent, the
transmit mode, three on/off flags
(transmit enabled, transmitting,
decoding), the receive and transmit
frequency offsets, your callsign, your
grid, the other station's grid, and a
tail of optional newer fields. A Decode
carries: new-or-old flag, time, signal
report in dB, time offset, audio
frequency, mode, the message text
itself, and two flags. The **grid on
the map comes from these fields** —
from the message text and the Status —
which is chapter 1's rule at the level
of bytes: the pin is placed at the grid
the report *claims*.

## Forwarding, and replying

GridTracker can pass every datagram it
receives onward, unchanged, to another
address and port — default 127.0.0.1
port 2238, off by default — which is
how a second program (a logger, say)
shares one WSJT-X feed. It can also
send a small set of messages *back* to
WSJT-X, which is how clicking a roster
row can start a contact there; that
direction is covered, briefly, in
chapter 7.

## What the lab proved — and the part it could not send

Proved for real: the program binds UDP
2237 and holds it (transcript t02), and
the format above is the program's own
code, read from the official package.

Not proved: a reaction. The lab wrote
a sender (`gridtracker-lab/send_wsjtx.py`)
that builds a wrong-magic control, a
Heartbeat, a Status, two Decodes and a
QSO Logged for two invented stations —
N0TST in FN42 hearing N0CLL in FN31, on
20 metres — exactly in the parser's
format, and tried to deliver them to
the running program. The sandbox this
lab runs in blocks outbound UDP
entirely, loopback included: every send
failed with `Operation not permitted`,
and a control test — a Python listener
and sender on the same machine, port
18099 — failed identically (transcript
`gridtracker-lab/transcripts/t04-udp-probe-blocked.txt`).
So the map's reaction to a received
datagram is **documented-only in this
guide**. On an ordinary machine the
sender script is yours to run: one
Status datagram should turn the
window's header from `waiting for
message` to the fictional station's
band and frequency, and the Decode
should add N0CLL to the roster.

Check: with GridTracker running,
`ss -lunp | grep 2237` shows the
listener. In WSJT-X's Reporting
settings, the UDP port matches it. If
either number differs, the two programs
are shouting into different rooms.
