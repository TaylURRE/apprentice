# SLURP - Computer Architecture

## Objectives
 - Understand how computers work and how that can impact programs
  - Latency vs Throughput
  - Memory Hierarchy
  - Stack and Heap

## Questions

After watching the videos answer these questions:

 1. You are Google and want to serve up results to keyword as quickly as possible.  How do you store the search index?
 1. You are a company that wants to transfer several petabytes of data from your data center to amazon.  What is the fastest way to transfer all the data?
 1. Name examples of things stored on the stack, how about the heap?
 1. Which is faster to allocate memory to, the stack or the heap?

## Coding Exercise

In this exercise we are going to optimize a program, using what you learned about computer architecture.  The objective is to make your program fast enough to catch the white rabbit.

First setup the white rabbit server.

```
pyenv virtualenv computerArchitecture
pyenv activate computerArchitecture
pip install -r requirements.txt
./server.py
```

If you run into encoding issues, affix `# -*- coding: utf-8 -*-` above your imports. 

The server has two endpoints `/start` and `/look/{position}`.  Your program will first make a request to `/start` which will start the white rabbit running.  You will then need
to make a request to `/look/{position}` with the correct position within 1200μs.  

The way to find the correct position is to find the end of the labyrinth returned when you make a request to `/start`.  The `/start` endpoint returns a series of bytes that can be broken up into pairs.  For instance

```
3,1,2,3,0,2
```

Can be thought of as:

```
[3, 1], [2, 3], [0, 2]
```

Each pair represents the start and end position of a segment the labyrinth.  You need to arrange the segments so they start with zero and connect each end to the next start.  Like so:

[0, 2], [2, 3], [3, 1]

The last position is the end of the labyrinth and the location that needs to be sent to `/look/`.  So in the case above you would send `/look/1`

Note: The locations are in the labyrinth are a reordering of an array.  So a labyrinth of length 100 has all positions between 0 and 99 only once.

If testing more than once, you may need to clear the port in use: 
https://stackoverflow.com/questions/19071512/socket-error-errno-48-address-already-in-use
https://unix.stackexchange.com/questions/8916/when-should-i-not-kill-9-a-process
