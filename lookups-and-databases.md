# Lookups and databases

Outcome: you know where the name, place,
and flags beside a callsign come from,
which of it arrived over the network,
and which of it the program fetched
before you asked.

## Two kinds of enrichment

A Decode report carries a callsign and
often a grid. The roster wants more: a
name, a state or county, whether the
station uses Logbook of the World.
GridTracker gets it two ways.

**Online lookups**, one callsign at a
time, from the service you pick in the
Lookups settings. The saved defaults
name the choice plainly:
`app.lookupService = "CALLOOK"` — the
free US callsign database — with QRZ,
HamQTH, and QRZCQ as the alternatives,
the last three behind accounts whose
usernames and passwords sit in the
settings (`lookupLoginQrz` and family).
Two lookup behaviours deserve a read
before you rely on them:

- **Add lookup data to the log event**
  can write the looked-up name and place
  into GridTracker's record of a
  contact. The manual notes it does not
  flow back into WSJT-X's file.
- **Fill a missing grid from the
  lookup** (`lookupMissingGrid`, off by
  default) is chapter 1's rule with the
  safety off: the pin goes to the
  grid the *database* has for that
  callsign — their home square — even
  when the station is operating from
  somewhere else entirely and simply
  didn't send a grid. It is a guess,
  labelled in the settings as working
  "pretty well" for standard US calls,
  and it fails exactly where you would
  want it most, on the portable and
  special-event stations.

**Downloaded databases**, whole lists
at once, used locally: the FCC's US
callsign data as repackaged by the
project (needed for the roster's state
and county columns), and the membership
lists of Logbook of the World, eQSL,
and Club Log's OQRS. Each can be
switched off in the Lookups settings.

## What the lab watched it fetch

The downloaded side is verified, in
the plainest way: the lab gave the
program an empty home, and on a later
run the `Ginternal` folder held five
new files it had fetched for itself
(transcript
`gridtracker-lab/transcripts/t03-saved-settings.txt`):

```
528727    dxcc-info.json          (country data)
2784792   eqsl-callsigns.json
3506950   lotw-ts-callsigns.json
1350359   canada-callsigns.txt
12034232  uls-fz-callsigns.txt    (the US callsign list)
```

About 20 MB of other people's data,
arriving unrequested on first run and
refreshed roughly weekly after that,
per the manual. None of it is checked
against reality by the program — a
callsign in the FCC list is listed
because the FCC says so, and a station
the lists have never heard of gets no
flags and, for US state and county
purposes, no answer. Missing from the
database reads as "not a member",
which is a different statement, and the
roster does not distinguish them.

Check: find one callsign in the roster
showing LoTW or eQSL flags, then look
for the same callsign in the matching
file under `Ginternal`. The flag on
screen is that line in the file, and
nothing more.
