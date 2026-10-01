# TCP Segment Practice

A Python-based TCP segment practice tool created for my **ITC 2024 Network Fundamentals** class.

The program generates randomized TCP **ACK**, **SEQ**, and **DATA** values and challenges the user to calculate the correct values as communication switches between a sender and receiver.

## Features

- Randomized ACK, SEQ, and DATA values
- Random sender/receiver packet direction
- Interactive ACK and SEQ calculation practice
- Progressive hints after repeated incorrect attempts
- Input validation
- Tracks completed segments
- Option to exit the program during practice

## What It Practices

This project was designed to help practice the relationship between TCP sequence and acknowledgment numbers across multiple segments.

Depending on the direction of communication, the program applies calculations such as:

```text
New SEQ = Previous ACK
New ACK = Previous SEQ + Previous DATA
```

When the same side continues sending:

```text
New SEQ = Previous SEQ + Previous DATA
ACK remains unchanged
```

## Requirements

- Python 3

No external libraries are required.

## Running the Program

Clone the repository or download the Python file, then run:

```bash
python "tcp_segmetation_practice.py"
```

Follow the prompts and enter the expected ACK and SEQ values for each generated TCP segment.

## Purpose

This was created as a learning project for **ITC 2024 Network Fundamentals** to make practicing TCP sequencing and acknowledgments more interactive.
