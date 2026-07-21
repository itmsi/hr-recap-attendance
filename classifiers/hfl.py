# classifiers/hfl.py
"""
Klasifikasi HFL — Cuti Pernikahan/Duka (Happy/Funeral Leave).

Dipanggil oleh __init__.classify() ketika kolom
"HFL-Happy/Funeral(Day(s))" bernilai 1 atau 0.5.

Return: ["HFL"] atau ["1/2 HFL"]
"""

from .base import parse_day_value


def classify(hfl_count) -> list[str] | None:
    val = parse_day_value(hfl_count)
    if val is None:
        return None
    if abs(val - 0.5) < 0.01:
        return ["1/2 HFL"]
    if val >= 0.99:
        return ["HFL"]
    return None