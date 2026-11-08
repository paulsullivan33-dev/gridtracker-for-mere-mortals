# Logging onward

Outcome: you can route a finished
contact from GridTracker to the
logbooks and services where it
permanently belongs — and you know that
this guide read about every one of
those routes rather than sending a
single real contact anywhere.

*Verification note: every route in this
chapter is documented-only. No lab
account exists for any of these
services, no real log was used, and no
contact left the machine.*

## The point of the chapter

Chapter 8 ended with the rule: your
master log is not in GridTracker. These
are the conveyor belts out. When a QSO
Logged report arrives from WSJT-X,
GridTracker can pass the record onward,
at once, to any combination of:

- **Local loggers on the same machine
  or network** — N3FJP's AC Log, Log4OM,
  Ham Radio Deluxe, DXKeeper — each with
  its own section in the saved settings
  (`acLog`, `log4OM`, `HRDLogbookLog`,
  `dxkLog`, `N1MM`), which tells you the
  integrations are per-program
  conversations, not a generic export.
- **Web logbooks** — QRZ Logbook,
  Logbook of the World, eQSL, and Club
  Log — whose buttons sit in the main
  window's button grid in the first-run
  screenshot, one icon each. Each needs
  your credentials for that service,
  entered in the Logging settings.
- **An ADIF broadcast** — the record
  re-sent as a UDP datagram (default
  port 2333, off in the defaults) for
  anything else on the network that
  listens for log records, plus plain
  ADIF files written to disk.

The settings manual's warning is worth
keeping beside all of this: contact
data stored by GridTracker itself lives
in ADIF files on your local disk (or
OneDrive, on Windows) — convenient
copies, not the archive. The archive is
the service or logger you trust, and
the belt only runs for contacts
GridTracker was told about while it was
awake, or that arrive in a file it
loads.

## A word about credentials

Each web route wants a password or an
API key, and those live in the settings
file in plain JSON, alongside the
lookup logins of chapter 10
(`lookupLoginQrz`, `lookupPasswordQrz`
are literal key names in the defaults).
That is ordinary for this class of
program, and it means the settings
file — and its `gt_settings.json`
exports — are worth the same care as
any other file full of passwords: share
a settings export to help a friend and
you may have shared more than your
window layout.

Check: in Settings, open the Logging
tab and count the destinations listed.
Every ticked one is a place a copy of
your next contact will go — if a name
there surprises you, untick it before
your next session, not after.
