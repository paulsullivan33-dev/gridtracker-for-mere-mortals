# Alerts

Outcome: you can make GridTracker call
out — in speech, sound, or text — when
a station you care about appears in the
reports, and you understand what an
alert is really claiming.

*Verification note: alerts trigger on
live traffic, which the lab could not
deliver (chapter 5). This chapter is
documented-only, from the manual and
the alert settings inside the package.*

## What an alert watches

An alert is a rule over the incoming
reports: when a Decode names something
that matches, you hear about it. The
manual's classes are the natural ones —
a callsign (theirs, or your own), a
grid square, a country (DXCC), a CQ
zone or ITU zone, a US state — each
judged **against your log**, with the
reference chosen per chapter 7: new
only counts as new compared with the
contacts in the loaded log, on the
bands and modes the reference names.

The output is your choice per alert:
**text-to-speech** by default — the
program speaks the callsign and why it
matters, through the speech dispatcher
the Linux launcher explicitly enables —
or a media sound instead. A separate
Audio settings tab holds the voice,
the device, a lightning alert, and a
sound on logging a contact. The
manual's one firm warning on devices:
do not pick the sound card your radio
uses, or your alerts and your FT8 share
a wire.

Custom alerts go further — your own
lists and patterns, kept in the
settings as `customAlerts` — and the
roster's Feed alerts (chapter 12) speak
for spots as well as decodes, with
their own `feedAudioAlerts` section.

## The honest limits of an alert

The manual states the deepest one
itself: WSJT-X, and therefore
GridTracker, "hears what you tell it to
hear." An alert can only fire on the
band and mode the radio is on, in the
reports that actually decode. There is
no alert for the station that was on
another band, under the noise, or on
while the program was closed — chapter
1's rule, at the moment it costs you a
country. And the judgement inside the
alert inherits the log's gaps: alert
for "new grid" with half your log
unloaded and the voice will announce
old friends as discoveries, confidently,
in speech.

Used with those two caveats in mind,
the classic setup is the manual's own
tip: an alert on your *own* callsign,
so the program pings you when someone
answers your CQ while you are making
coffee.

Check: set one alert you can predict —
your own callsign — and confirm it is
listed under the Alerts settings.
Then, next session, note whether
anything it announced as "new" was
truly new *in your full log*; if not,
chapter 8 is where the fix lives.
