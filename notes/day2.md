# Day 2

Added two more bugs today, because the first two felt too easy on their own.

What I did today:
- added a contract with no access control at all, and its fixed version
- added a contract that ignores the return value of a call, and its fixed version
- taught the simple checker to spot those two as well

What I learned:
- a missing check is easy to miss when you are reading fast, because the code looks normal
- checking the return value feels like a small thing, but ignoring it can lose funds quietly
- my first version of the checker flagged the safe contracts too, because it read comments and treated every withdraw the same. I fixed it to ignore comments and only flag a withdraw that sends the whole balance with no check.

The dataset is now 8 examples. Still small, and that is fine for now. I would rather have 8 I understand than 100 I do not.
