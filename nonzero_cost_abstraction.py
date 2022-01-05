#!/usr/bin/env python3

from timeit import timeit
from random import *

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def create_point():
    p = Point(
        random(),
        random(),
        random())

def create_tuple():
    p = (
        random(),
        random(),
        random()
        )

class SequenceRecord:
    def __init__(self, header, sequence):
        self.header = header
        self.sequence = sequence

def create_record_tuple():
    return (">THIS_IS_A_RANDOM_HEADER",
            "ACTGCTTGGCTCGGATTCGATCGGATCGATCG")

def create_record_class():
    return SequenceRecord(
            ">THIS_IS_A_RANDOM_HEADER",
            "ACTGCTTGGCTCGGATTCGATCGGATCGATCG")

n=int(1e6)

print("Small Numerical Class")
print(f"Time to create {n} tuples: ", timeit(create_tuple, number=n))
print(f"Time to create {n} Points: ", timeit(create_point, number=n))

print()
print("Small String Class")
print(f"Time to create {n} tuples: ", timeit(create_record_tuple, number=n))
print(f"Time to create {n} SequenceRecords: ", timeit(create_record_class, number=n))

