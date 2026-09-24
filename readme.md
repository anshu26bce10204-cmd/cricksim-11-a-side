# 🏏 CrickSim — 11-a-Side Cricket Match Simulator

## Overview

CrickSim is a console-based Python application that simulates a full 5-over,
11-a-side cricket match between two user-defined teams. Every single ball is
entered manually by the user (runs, wicket, wide, or no ball), and the
program takes care of the rest: strike rotation, wickets falling, over
completion, scorecards, and the final result — including margin of victory
and a "play again" loop.

It was built as a hands-on project to practice core Python concepts
(functions, classes, loops, conditionals, and input validation) in a fun,
relatable domain.

## Features

- 👕 Custom or auto-generated 11-player squads for both teams
- 🪙 Toss simulation with bat/bowl decision
- 🎾 Ball-by-ball input: runs (0–6), wicket (W), wide (WD), no ball (NB)
- 🏃 Automatic strike rotation on odd runs and at the end of every over
- 🚶 Automatic next-batsman entry after every wicket
- 📊 Live mini-scoreboard after every ball
- 📋 Full batting scorecard (runs, balls, out/not out) at the end of each
  innings
- 🎯 Live "runs/balls needed" tracker during the second innings run-chase
- 🏆 Automatic result: win by runs, win by wickets, or a tie
- 🔁 "Play a new match?" loop to start over without restarting the program
- 😄 Emoji-based commentary for boundaries, wickets, and milestones

## Technologies / Tools Used

- *Language:* Python 3
- *Libraries:* Standard library only (sys) — no external dependencies
- *Interface:* Command-line / console (works in VS Code's integrated
  terminal or any terminal)

## Project Structure


cricksim/
├── cricket_match.py   # Main program — all game logic
├── README.md          # This file
└── statement.md        # Problem statement, scope, target users, features


## Steps to Install & Run

1. Make sure *Python 3.8+* is installed:
   
   python --version
   
2. Clone or download this repository, then open the folder in VS Code (or
   any terminal).
3. Run the program:
   
   python cricket_match.py
   
4. Follow the on-screen prompts:
   - Enter both team names
   - Enter 11 player names per team (or choose auto-generate)
   - Enter the toss winner and their bat/bowl decision
   - For every ball, type one of: 0, 1, 2, 3, 4, 5, 6, W,
     WD, NB
5. After the result is shown, type yes when asked if you want to play a
   new match, or no to exit.

## Instructions for Testing

Manual testing was done by playing full matches and specifically checking:

- *Normal scoring:* entering a mix of 0–6 for every ball and confirming the
  running total and strike rotation update correctly (strike should swap on
  1, 3, 5 and at the end of every over).
- *Wickets:* entering W repeatedly to confirm a new batsman comes in each
  time, and that the innings ends automatically once 10 wickets have fallen.
- *Extras:* entering WD and NB to confirm 1 extra run is added and the
  ball is correctly replayed (over does not advance).
- *Invalid input:* typing something outside the allowed set (e.g. 9,
  abc) to confirm the program re-prompts instead of crashing.
- *Innings/overs boundary:* playing a full 5 overs (30 legal balls) to
  confirm the innings ends on its own even with wickets in hand.
- *Result logic:* testing all three outcomes — team batting first winning,
  the chasing team winning, and a tie (equal scores) — to confirm the correct
  message and margin are shown.
- *Replay:* confirming the "play a new match?" prompt correctly restarts
  the whole flow (new teams, new toss) on yes and exits cleanly on no.

## Screenshots

*(Add terminal screenshots here after running a sample match — e.g. the
toss prompt, a mid-over scoreboard, an end-of-innings scorecard, and the
final result screen.)*