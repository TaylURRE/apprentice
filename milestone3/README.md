Milestone 3 Coding Challenge
============================

Testing, Object Oriented Code, and Algorithms as a stretch.

Copy this folder into your private git repo as a folder named "milestone3".

Testing
-------

To run test cases:

> ./run-tests.sh

Test cases are failing by design, following Test Driven Development.
Your goal is to make changes to the code so the test cases pass.

Linting
-------

To lint your code (test whether it matches pep8 coding style).

Step 1: Install pep8, which was renamed to pycodestyle:
> pip install pycodestyle

Step 2: Run pycodestyle on this directory:
> pycodestyle . --max-line-length=110
