# Day 3

Added two more bugs today, and I am starting to see a pattern: most of these are about trusting something you should not trust.

What I did today:
- added a game that uses block.timestamp to pick a winner, and a version that does not
- added a contract where anyone can call init and become the owner, and a version that sets the owner in the constructor
- taught the checker to spot block.timestamp and a public init function

What I learned:
- block.timestamp can move a little, and a little is enough when money is on the line
- an init function is only safe if it can run once, and only by the right person

The dataset is now 12 examples. Still hand-written, still small. The next step is to look at public datasets, not to keep writing these one by one.
