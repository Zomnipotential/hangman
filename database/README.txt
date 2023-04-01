The words are extracted from the following data base and saved in a separate csv file
Each word is put on a separate line to make easy to pick one without the need for 
reading all of them into a list before choosing one randomly


**********
https://www.kaggle.com/datasets/lucashohmann/wordle-random-simulations

3,334,196 "random" Wordle game simulations

This dataset contains 1,444 "random" simulations for each one of the 2,309 possible solutions of the game, totalling 3,334,196 simulations. This simulations aren't completely random, the strategy work as follows:

Only known valid answers were used in these simulations.
After each attempt, the words are filtered based on the hits and misses of each letter, so, the next attempt is going to be a word randomly selected from the filtered ones.
The first 2 attempts apply a condition to pick only available words that have the maximum number of unique letters, maximizing the chances of getting good results.
It simulates "hard mode" where the current attempt always uses the correct and misplaced letters from the previous attempt.