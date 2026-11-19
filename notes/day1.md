# Day 1

Started this repo today. My laptop is slow for training, so I am starting with the basics first: reading contracts, writing down the bugs, and building a small dataset by hand.

What I did today:
- set up the repo structure
- wrote two vulnerable contracts and their fixed versions
- wrote a small script to label them, and a simple checker to compare against later

What I got wrong at first:
- I tried to write the reentrancy fix with a guard first, but the simplest fix is just to update the balance before the call. Keeping it simple helped me understand it.

Tomorrow: more examples, and better labels. I want the dataset to be small and correct, not big and noisy.
