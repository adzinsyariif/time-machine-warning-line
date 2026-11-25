#!/usr/bin/env python3
"""Funniest Time Machine Warning Label entry.

Writes one warning label line to /output/entry.txt.
Deterministic, stdlib only, no network.
"""
import os

LINE = "WARNING: Do not shake hands with yourself. He has already claimed he is the original."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
