# Your logbook in GridTracker

Outcome: you can say where GridTracker's
picture of your past contacts comes
from, how to feed it a log, and why its
totals can differ from your real logbook
without anything being broken.

*Verification note: loading a log is a
file-picker action in the window, which
the lab did not perform. The scanning
behaviour is quoted from the program's
log and code; the loading itself is
documented-only. The lab's own fictional
log is `gridtracker-lab/fixtures/example-log.adi`.*

## A viewer of logs, not your logbook

Start with the project's own sentence,
from its settings manual: "**GridTracker
is a log viewer, not a logging
program.**" It keeps a view — enough to
colour grids, judge "worked before",
and count awards — but your master log
belongs in a real logger, and chapter 9
is about feeding contacts to one.
Everything in this chapter is the view.

## Where the view comes from

- **WSJT-X's own log.** At startup the
  program scans for the log files of the
  programs it keeps company with — the
  lab's first-run log shows it mid-scan,
  walking folders looking for other
  applications' logs and tripping,
  harmlessly, over the empty lab home.
  WSJT-X writes an ADIF of everything
  you log there, and GridTracker adopts
  it: contacts you log in WSJT-X appear
  in the view as the Logged ADIF reports
  arrive, and past ones arrive with the
  file.
- **Files you load.** The logbook
  controls accept `.adi` and `.adif`
  files — the file selector in the code
  takes exactly those two extensions —
  from any logger that can export ADIF.
  Load a full export and the view
  becomes your whole history; load last
  month's and the view is last month.
- **Downloads from Logbook of the
  World.** With your LoTW credentials
  the program can fetch the confirmed
  records as an ADIF from the ARRL's
  report address (the URL is in the
  code, login and all), which is how the
  QSL side of the counters gets fed.
- **Its own backup log.** GridTracker
  can keep a local ADIF of the contacts
  it sees logged — the `Backup Logs`
  folder it creates on first run is part
  of that machinery, and features like
  Parks on the Air hunting turn it on,
  because the program needs a memory of
  today even if your real logger is
  elsewhere.

The startup switch is a single setting,
`app.loadAdifAtStartup` — false in the
fresh defaults the lab read, because a
big log costs time to swallow. And note
what is *not* here: no editing. The
view is read-and-count; corrections
happen in the real logbook and are
re-imported.

## Reading a record

The lab fixture is four contacts, small
enough to read whole: the fictional
N0TST, in FN42, works N0CLL in FN31
twice (20 m and 40 m), N0DXA in EM79,
and N0WST in DM04, all FT8. Every field
is a named tag — `<call:5>N0CLL`,
`<gridsquare:4>FN31`, `<band:3>20m` —
and those four records are all
GridTracker would know about N0TST's
life: three grids worked, one country,
one station worked on two bands. The
fixture is invented from end to end, as
every example in this guide is; real
logs say the same things at greater
length and with real callsigns.

## Why the totals argue with your logbook

They are counting different sets. Your
logger counts every record it holds.
GridTracker counts the records it was
*given*: the files loaded, the reports
heard while it was running, the LoTW
download as of its date. A contact made
while GridTracker was closed arrives
only if the log file it later loads
contains it. A contact in a file you
never loaded does not exist — chapter
1's rule, at ledger scale. When the
numbers disagree, the fix is almost
never in GridTracker; it is a fuller
export from the master log.

Check: load the lab fixture (or your
own export) and read the QSO and QSL
counters in the main window. They
should equal the record count of the
file you loaded — and nothing else's.
