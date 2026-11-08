#!/usr/bin/env python3
"""Send WSJT-X Network Message datagrams to GridTracker2 on 127.0.0.1:2237.
Wire format taken from GridTracker2's own parser (src/renderer/lib/wsjtxUdp.js
inside the official app.asar) and the field comments in that file.
All stations are fictional lab inventions: DE = N0TST in FN42, DX = N0CLL in FN31.
"""
import socket, struct, sys, time, datetime

MAGIC = 0xADBCCBDA
SCHEMA = 3
ID = "WSJT-X"

def u32(v): return struct.pack(">I", v)
def i32(v): return struct.pack(">i", v)
def u64(v): return struct.pack(">Q", v)
def f64(v): return struct.pack(">d", v)
def u8(v): return struct.pack(">B", v)
def utf8(s):
    b = s.encode("utf-8")
    return u32(len(b)) + b
def header(mtype): return u32(MAGIC) + u32(SCHEMA) + u32(mtype) + utf8(ID)

def heartbeat():
    return header(0) + u32(SCHEMA) + utf8("2.7.0-lab") + utf8("lab")

def status():
    m = header(1)
    m += u64(14074000)          # Frequency Hz (20 m FT8 watering hole)
    m += utf8("FT8")            # Mode
    m += utf8("N0CLL")          # DX call
    m += utf8("-07")            # Report
    m += utf8("FT8")            # Tx mode
    m += u8(0)                  # Tx enabled
    m += u8(0)                  # Transmitting
    m += u8(0)                  # Decoding
    m += i32(1500)              # Rx DF
    m += i32(1500)              # Tx DF
    m += utf8("N0TST")          # DE call (fictional)
    m += utf8("FN42")           # DE grid (fictional)
    m += utf8("FN31")           # DX grid (fictional)
    m += u8(0)                  # Tx watchdog
    m += utf8("")               # Submode
    m += u8(0)                  # Fast mode
    return m

def decode(msg, snr, df, ms_since_midnight):
    m = header(2)
    m += u8(1)                  # New
    m += u32(ms_since_midnight) # Time
    m += i32(snr)               # SNR
    m += f64(0.1)               # Delta time
    m += u32(df)                # Delta frequency
    m += utf8("FT8")            # Mode
    m += utf8(msg)              # Message
    m += u8(0)                  # Low confidence
    m += u8(0)                  # Off air
    return m

def qso_logged():
    jd = datetime.date(2026, 11, 7).toordinal() + 1721425  # Julian day
    ms = (22 * 3600 + 40 * 60) * 1000
    m = header(5)
    m += u64(jd) + u32(ms) + u8(1)      # Date/time off (local timespec=1)
    m += utf8("N0CLL") + utf8("FN31")   # DX call / grid
    m += u64(14074000) + utf8("FT8")
    m += utf8("-07") + utf8("-09")      # Reports sent / received
    m += utf8("50")                     # TX power
    m += utf8("lab fixture contact")    # Comments
    m += utf8("Fictional Friend")       # Name
    m += u64(jd) + u32(ms - 60000) + u8(1)  # Date/time on
    m += utf8("N0CLL") + utf8("N0TST") + utf8("FN42")  # Operator, my call, my grid
    m += utf8("") + utf8("")
    return m

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = ("127.0.0.1", 2237)
now_ms = (22 * 3600 + 39 * 60 + 15) * 1000

bad = u32(0xDEADBEEF) + u32(SCHEMA) + u32(0) + utf8(ID) + u32(SCHEMA) + utf8("x") + utf8("y")
steps = [
    ("wrong-magic heartbeat (control)", bad),
    ("heartbeat", heartbeat()),
    ("status", status()),
    ("decode CQ", decode("CQ N0CLL FN31", -7, 1500, now_ms)),
    ("decode exchange", decode("N0TST N0CLL -09", -9, 1500, now_ms + 15000)),
    ("qso logged", qso_logged()),
]
for name, pkt in steps:
    sock.sendto(pkt, dest)
    print(f"sent {name}: {len(pkt)} bytes", flush=True)
    time.sleep(3)
print("all sent")
