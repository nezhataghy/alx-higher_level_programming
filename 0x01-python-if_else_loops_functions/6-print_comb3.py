#!/usr/bin/python3
for m in range(0, 8):
    for n in range(m + 1, 10):
        print(f"{m:d}{n:d}", end=', ')
print(f"{(m + 1):d}{n:d}")
