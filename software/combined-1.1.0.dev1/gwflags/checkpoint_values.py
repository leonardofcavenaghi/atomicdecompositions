"""Exact checkpoint fractions without decimal integer conversion limits.

Small values retain the legacy decimal spelling. Large values use explicitly
tagged hexadecimal numerator/denominator strings, supported in spawned workers
without changing the interpreter's process-wide conversion policy.
"""
from fractions import Fraction
import json


def dumps_values(values):
    def encode(value):
        value = Fraction(value)
        if max(abs(value.numerator).bit_length(), value.denominator.bit_length()) <= 2000:
            return str(value)
        return {'hex': [format(value.numerator, 'x'), format(value.denominator, 'x')]}
    return json.dumps([encode(value) for value in values])


def loads_values(text):
    def decode(value):
        if isinstance(value, dict):
            numerator, denominator = value['hex']
            return Fraction(int(numerator, 16), int(denominator, 16))
        return Fraction(value)  # Existing decimal checkpoints remain readable.
    return [decode(value) for value in json.loads(text)]

