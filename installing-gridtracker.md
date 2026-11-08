# Installing GridTracker

Outcome: GridTracker2 on your machine,
proved by the version the program
itself shows — and an honest account
of which install route this guide ran
and which it only read about.

## The check

However you install it, the proof is
the same: start the program and read
its own version line. GridTracker2
prints it in the main window, under the
button panel. This guide's lab copy
reads **GridTracker2 v2.261019.5** in
the window itself (screenshot
`gridtracker-lab/first-run-window.png`),
and the package agrees with it three
more ways: the package control file
says `Version: 2.261019.5-991`, the
`package.json` inside the app says
`"version": "2.261019.5"`, and its
`build.env` says `VERSION=2.261019.5`
(transcripts
`gridtracker-lab/transcripts/t00-download-and-package.txt`
and `t01-asar-inventory.txt`). When the
numbers disagree, believe the window:
it is the program describing itself.

## The route the lab used: the official .deb, unpacked

GridTracker2 is not in the ordinary
Debian or Ubuntu repositories. The
project serves its own packages from
its own download server — the same
server its built-in updater uses,
`download2.gridtracker.org`, named in
the `app-update.yml` file inside the
package itself. The lab downloaded the
current x86-64 package:

```
GridTracker2-2.261019.5-amd64.deb   (112,973,364 bytes)
SHA-256: 4b192de09ed78eb78a2191a5e300e24268fe364a4c5f2684f157078c8587a3d7
```

On a real machine you install it the
normal way and let the package manager
pull in what it needs:

```
sudo apt install ./GridTracker2-2.261019.5-amd64.deb
```

The package declares its needs plainly
(the control file, transcript t00):
GTK 3, NSS, XScreenSaver and XTest
libraries, a notifications library,
`xdg-utils`, and a few more — the usual
furniture of a desktop application. It
installs to `/opt/GridTracker2/`,
registers the command `gridtracker2`,
and files itself in the applications
menu under Utility and HamRadio.

One honest difference: the lab did
**not** install the package system-wide.
It unpacked the `.deb` with `dpkg-deb`
and ran the program in place from the
unpacked tree, with the home directory
pointed at a scratch folder so every
file the program wrote could be
inspected afterwards. The program is
the same program either way; the
package's own post-install steps
(desktop database updates, an AppArmor
profile, the `/usr/bin` link) were read
and are described here, not run.

The launcher inside the package is a
two-line shell script worth knowing
about (verbatim in transcript t00): it
runs the real binary, `gridtracker2.bin`,
with `--no-sandbox` — the browser
engine's sandbox is switched off by the
project's own choice — plus a flag that
enables the speech dispatcher its
spoken alerts use.

## Keeping it current

There are no distribution repositories
for version 2 any more; the project
retired them. Instead the program
checks for a new version itself, offers
to download the new package, and on
exit asks permission to install it
through the system package manager. The
lab saw the check happen — the first
launch logged `Checking for update` —
and also saw it fail in the sandbox,
where the network path broke the
certificate check
(`ERR_CERT_AUTHORITY_INVALID`, transcript
t02). On a normal desktop the check
simply works; the lesson for the lab is
only that the program reaches out on
its own, which chapter 12 returns to.

Old versions are genuinely old: the
project keeps only the current release
and sometimes one back on the server —
the lab confirmed the two newest
version numbers answered and older ones
returned "not found" — and warns that
versions before v1.23 can no longer
reach its online services at all.

## The other routes, documented only

- **ARM Linux.** The same server carries
  an `arm64` build of the same version
  for Raspberry Pi-class machines; the
  lab is x86-64 and did not run it.
- **Windows and macOS.** Installers for
  both are offered on the same downloads
  page. Nothing in this guide's lab
  touched them.
- **Version 1.** The original
  GridTracker is end-of-life and its
  repositories are taken down. If you
  have it, version 2 installs beside it
  and offers to pull settings from the
  last two v1 releases; do not uninstall
  v1 until v2 is running.

Check: start the program and read the
version in the window. Then run
`dpkg-deb -f` on your downloaded file
and compare. If the two agree, you are
installed — chapter 4 takes the first
run apart.
