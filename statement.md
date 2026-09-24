# Problem Statement

Beginners learning Python and cyber security fundamentals often lack simple,
hands-on projects that combine control flow, state management, and input
validation in an engaging way. There is no lightweight, offline, console-based
tool that lets two full cricket teams play out a limited-overs match ball by
ball, entirely driven by user input, while correctly tracking runs, wickets,
extras, strike rotation, and the final result.

**CrickSim** solves this by simulating a realistic 11-a-side, 5-overs-per-side
cricket match in Python. Every ball's outcome (runs, wicket, wide, no ball) is
entered by the user, and the program handles all the scoring logic, batsman
rotation, wicket-fall handling, scorecards, and the final result — including
letting the user start a brand-new match afterwards.

## Scope of the Project

- Two teams of 11 players each, with names entered by the user or
  auto-generated.
- A coin-toss stage where the winning team chooses to bat or bowl first.
- A ball-by-ball innings engine for two innings of 5 overs each (30 legal
  balls per side), including:
  - Runs (0–6), wickets, wides, and no balls
  - Automatic strike rotation on odd runs and at the end of every over
  - A new batsman coming in after every wicket, until all out or overs end
- Live mini-scoreboard after every ball, and a full batting scorecard at the
  end of each innings.
- Automatic result calculation — win by runs, win by wickets, or a tie — once
  both innings are complete.
- A "play another match?" loop so a new match can be started without
  restarting the program.

**Out of scope:** bowler-wise statistics, run-outs on a specific batsman,
Duckworth-Lewis-style rain rules, a graphical interface, and persistent
storage of match history (these are listed as possible future enhancements).

## Target Users

- First-year Computer Science / Cyber Security students learning Python
  fundamentals (functions, classes, loops, input validation) through a
  practical, self-built project.
- Cricket fans who want a quick, offline, text-based way to simulate a
  friendly match.
- Anyone wanting a simple example of state-machine-style logic (innings,
  overs, wickets, strike rotation) implemented in plain Python.

## High-Level Features

1. **Match Setup & Toss Module** — team and 11-player squad creation, toss
   winner and decision (bat/bowl), and deciding which team bats first.
2. **Ball-by-Ball Innings Engine** — validated input for every ball, run and
   wicket handling, wide/no-ball extras, strike rotation, over-by-over
   progress, and end-of-innings conditions (all out or overs completed).
3. **Scorecard & Result Module** — live scoreboard during play, full batting
   scorecard at the end of each innings, final result computation (by runs,
   by wickets, or tie), and a replay option to start a new match.