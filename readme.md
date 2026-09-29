# 🏏 CrickSim — 11-a-Side Cricket Match Simulator

## Overview

this project is fully based on 5 over performance of both team,
cricketstimulatoe is fully based on python programme,
11 players-side cricket match between two user-defined teams. every ball is manually entered by users
 (runs, wicket, wide, or no ball), and the
programer takes care of the rest: strike change, wickets out, over
completion, scorecards, and the final result — including victory by how many runs by a team
and a "play again" loop.

It was built as a hands-on project to practice basic python concepts
(functions, classes, loops, conditionals, and input validation) in a fun,
relatable domain.

## Features

-   manually or auto-generated 11-player squads for both teams
-  Toss simulation with bat/bowl decision
-  Ball-by-ball input: runs (0–6), wicket (W), wide (WD), no ball (NB)
-  Automatic strike change on odd runs and at the end of every over
-  next bat man entry after every pervious batsman out
-  display live scorecard after every ball played by batsman
-  display live scorecard after every inning
-  display run needed by the playing team to win the matchoop to star
-  automatic:update team win by wicket,by run or tie
-  "Play a new match?" loop to start a new match after an inning

## Technologies / Tools Used

- *Language:* Python language
- *Libraries:* Standard library of python
- *Interface:* Command-line /console (works in VS Code's integrated
  terminal or any terminal)

## Project Structure


cricksimulator/
├── cricket_match.py   # Main program code
├── README.md          # This file
└── statement.md        # Problem statement, scope, target users, features


## Steps to Install & Run

1. Make sure *Python 3.8+* is installed:
   
   python --version
   
2. Clone or download this repository, then open the folder in VS Code (or
   any terminal).
3. Run the program:
   
   python cricket_match.py
   
4. details of both teams:
   -enter name of both teams
   - Enter the name of all players or choose auto generate 
   - Enter the toss winner and their bat/bowl decision
   -type of output on every ball: 0, 1, 2, 3, 4, 5, 6, W,
     WD, NB
5. after the result of every match,ask for play a new match
   or exit the game

## Instructions for Testing

Manual testing was done by playing full matches and specifically checking:

- *Normal scoring:* entering a mix of 0–6 for every ball and confirm the 
   total and strike change update correctly (strike should swap on
  1, 3, 5 and at the end of every over).
- *Wickets:* entering W repeatedly to confirm out of batsman from match and entery of a new batsman 
  time,every team play 5 over match and that the innings ends automatically once 10 wickets have fallen.
- *Extras:* entering WD and NB to confirm 1 extra run is added and the
  ball is replay by bowler to the batsman
- *Invalid input:* typing something outside the allowed set (e.g. 10,
  xyz) to confirm the program re-prompts instead of crashing.
- *Innings/overs boundary:* playing a full 5 overs (30 legal balls) to
  confirm the innings ends on its own even with wickets in hand.
- *Result logic:* testing all three outcomes — team batting first winning,
  the chasing team winning, and a tie (equal scores) — to confirm the correct
  message and margin are shown.
- *Replay:* confirming the "play a new match?" prompt correctly restarts
  the whole flow (new teams, new toss) on yes and exits cleanly on no
## Screenshots

*(Add terminal screenshots here after running a sample match — e.g. the
toss prompt, a mid-over scoreboard, an end-of-innings scorecard, and the
final result screen.)*