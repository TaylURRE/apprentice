#!/usr/bin/env python
import http.client
import urllib.request

client = http.client.HTTPConnection('127.0.0.1', 8080)


def run():

    # Try to optimize this function so that the time between start and look is
    # faster.

    print("Calling Start")
    file_name = download_labyrinth()
    paths = chunk(decode(read_file(file_name)))
    print(paths)
    end_location = traverse_array(paths)
    look(end_location)


def download_labyrinth():
    """calls /start and download labyrinth to a file.
        The file name is returned"""
    client.request('GET', '/start')
    start_response = client.getresponse()
    with open("labyrinth", 'wb') as file:
        bytes = start_response.read(200)
        file.write(bytes)
    return "labyrinth"


def look(location):
    """calls look for a particular location and prints the response"""
    client.request('GET', '/look/%d' % location)
    look_response = client.getresponse()
    print(look_response.read(200).decode('UTF8'))


def chunk(arr):
    """Converts an array into an array of 2 element arrays"""
    return [arr[i:i+2] for i in range(0, len(arr), 2)]


def decode(bytes):
    """Converts a byte array to an array of integers"""
    return [int(x) for x in bytes]


def traverse_array(paths):
    """Given an array of arrays, finds the last location by sorting
       through the arrays."""
    labyrinth = [None] * 1000
    for path in paths:
        labyrinth[path[0]] = path[1]
    location = 0
    while True:
        next_location = labyrinth[location]
        if next_location is None:
            return location
        location = next_location


def read_file(file_name):
    """Reads a given file as a series of bytes."""
    bytes = []
    with open(file_name, 'rb') as file:
        bytes = file.read(200)
    return bytes

if __name__ == "__main__":
    run()
