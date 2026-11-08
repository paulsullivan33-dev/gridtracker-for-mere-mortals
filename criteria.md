# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's traffic is the lab talking to itself.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** The limits chapter names what the
   tool cannot do: it is a listener and a ledger, not a radio —
   it cannot transmit, decode a signal, or verify that a
   contact happened, and it trusts the reports it is fed
   completely; its awards and "worked before" judgements are
   only as true as the log file you give it, and go silently
   wrong on a partial log; its callsign databases, lookup
   results, feed spots, and base maps are other people's data,
   fetched over the internet and exactly as accurate as those
   services are; and on-air behaviour is documented-only in
   this guide's lab by construction, because the lab has no
   radio and its sandbox blocked even loopback test datagrams.
8. **The one rule is in the text, early.** Chapter 1 and the
   README state the rule plainly — *GridTracker knows only
   what it is told: everything on its map is a report it heard,
   believed; a station it was never told about does not exist
   for it, and a wrong grid in a report is a wrong pin on the
   map* — before any procedure depends on it, and later
   chapters point back to it where the rule bites: the pin
   drawn from a claimed grid, the roster colour drawn from a
   partial log, and the award total drawn from both.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is an Ubuntu sandbox (x86-64) with Xvfb
available. GridTracker2 **2.261019.5** was the project's
current official Linux package,
`GridTracker2-2.261019.5-amd64.deb` (112,973,364 bytes,
SHA-256 `4b192de09ed78eb78a2191a5e300e24268fe364a4c5f2684f157078c8587a3d7`),
downloaded from the project's own download server
`download2.gridtracker.org` — the server named in the package's
own updater config. The package was **unpacked with dpkg-deb,
not installed system-wide**, and the program was run in place
from the unpacked tree under Xvfb with `HOME` redirected into
the lab's scratch folder, so all state it created could be
inspected. The lab is in `gridtracker-lab/`: the transcripts,
a fictional four-contact ADIF fixture
(`fixtures/example-log.adi`), the WSJT-X probe sender
(`send_wsjtx.py`), and a screenshot of the first-run window
(`first-run-window.png`). Every station in the lab is invented
(N0TST in FN42, N0CLL in FN31, and friends); no real callsign,
log, or location appears anywhere in this guide.

Run for real, with transcripts as evidence:

- The download and the package itself (t00): control fields
  (`Version: 2.261019.5-991`, dependencies, `/opt/GridTracker2`
  layout, AppArmor post-install step), the desktop entry
  (categories Utility and HamRadio), the two-line launcher
  script (runs `gridtracker2.bin` with `--no-sandbox`), and
  the bundled changelog. Only the current version and one
  back answered on the download server; older filenames
  returned 404, matching the project's stated policy.
- Inside the package (t01): `resources/app.asar` read with a
  small Python asar reader — `package.json` and `build.env`
  both state version 2.261019.5; the app's own source was
  extracted and read, including the WSJT-X UDP parser
  (`wsjtxUdp.js`: magic `0xADBCCBDA`, message types 0/1/2/3/
  5/6/10/12, field-by-field layout, duplicate suppression,
  messages discarded until loading finishes), the settings
  defaults (`wsjtUdpPort` starting at 0 and resolving to
  2237, forward port 2238, ADIF broadcast port 2333,
  `lookupService: CALLOOK`, `myCall: NOCALL`), and the PSK
  Reporter MQTT publisher (`mqtt.pskreporter.info:1883`).
  Bundled offline map tile sets were inventoried in the asar.
- The first launch (t02): the real binary ran under Xvfb for
  120 seconds and stayed alive; `ss` showed it holding UDP
  2237 from about t+10 s for the rest of the run. Its log
  records the first-run confessions (`Could not load:
  .../Ginternal/app-settings.json`, `Defaults will be
  applied`), a scan for other programs' log folders, and a
  version check that failed in the sandbox with
  `ERR_CERT_AUTHORITY_INVALID`. A screenshot at t+60 s shows
  the first-run window: world map, `waiting for message`,
  `...no data yet...`, counters all zero, Map View Filters
  at their defaults, and the window's own version line
  `GridTracker2 v2.261019.5`.
- A clean exit (t03): a second fresh-home run, ended with
  SIGTERM, wrote the real `Ginternal/app-settings.json`
  (25,366 bytes): 37 top-level sections, `app.wsjtUdpPort`
  saved as 2237, `currentVersion` 22610195, `spots.json`
  reading `{"spots":{}}`. Its `Ginternal` also held five
  callsign database files the program downloaded itself
  during the run (dxcc-info.json, lotw-ts-callsigns.json,
  eqsl-callsigns.json, canada-callsigns.txt,
  uls-fz-callsigns.txt; about 20 MB in total).

Documented only — described from the project's documentation
and the program's own code, not run, and the text does not
claim otherwise:

- Installing the .deb system-wide (apt/dpkg install, the
  post-install alternatives link, desktop database updates,
  and the AppArmor profile), the ARM build, and the Windows
  and macOS installers.
- The map populated with live traffic, pins and paths drawn,
  grid shading and decay in action, and all clicking,
  hovering, and zooming — these need received datagrams.
- The Call Roster populated, its sorting, hunting colours,
  exception lists, and click-to-call back to WSJT-X.
- Loading the lab's ADIF fixture (or any log) through the
  window's file picker, the Logbook view's counters against
  a real log, and Logbook of the World downloads, which need
  an account.
- Every onward-logging route of chapter 9 (QRZ, LoTW, eQSL,
  Club Log, N3FJP, Log4OM, HRD, DXKeeper, N1MM, ADIF
  broadcast). No accounts exist in the lab and nothing was
  uploaded.
- Online lookups against Callook, QRZ, HamQTH, or QRZCQ, and
  lookup-driven grid filling.
- Alerts firing — speech, sounds, custom alerts, and feed
  alerts all trigger on traffic the lab could not deliver.
- Spotting in either direction (PSK Reporter MQTT, the
  program's own online service), DX feeds, and the POTA and
  SOTA layers, which need live services; the lab's sandbox
  also broke the program's TLS connections.
- The WSJT-X probe reaction: `send_wsjtx.py` implements the
  Network Message format from the app's own parser and was
  run against the live, listening program, but the sandbox
  rejects every outbound UDP send (`Errno 1, Operation not
  permitted`), loopback included — proven against a Python
  listener on 127.0.0.1:18099 that received nothing (t04).
  The listener and the parser are verified; the reaction is
  not.
- Multicast reception, UDP forwarding in use, multiple
  WSJT-X instances, and everything involving a real radio,
  a real contact, or a real logbook.

One accident is kept in the record: the second launch attempt
was killed by the same UDP block before its probes were even
written, which is how the lab learned to test the sandbox's
UDP policy on its own first (t04's control test) rather than
blame the program.
