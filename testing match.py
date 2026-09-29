"""
Tests for cricket_match.py

Run from the same folder as cricket_match.py:

    python test_cricket_match.py          (short output)
    python -m unittest -v                 (detailed, test-by-test output)

No installs needed - uses only Python's built-in unittest.
Every input() call in the game is faked with mock, so nothing needs typing.
"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import cricket_match as cm


def run(func, inputs, *args, **kwargs):
    """Call func with fake keyboard inputs; return (result, printed_output)."""
    buf = io.StringIO()
    with patch("builtins.input", side_effect=inputs), redirect_stdout(buf):
        result = func(*args, **kwargs)
    return result, buf.getvalue()


def make_players(n=cm.TOTAL_PLAYERS):
    return [cm.Player(f"P{i}") for i in range(n)]


# ----------------------------------------------------------------------
class TestPlayer(unittest.TestCase):
    def test_defaults(self):
        p = cm.Player("Rohit")
        self.assertEqual(p.name, "Rohit")
        self.assertEqual((p.runs, p.balls), (0, 0))
        self.assertFalse(p.out)
        self.assertEqual(p.how_out, "not out")


# ----------------------------------------------------------------------
class TestSetup(unittest.TestCase):
    def test_get_players_auto(self):
        players, _ = run(cm.get_players, ["2"], "Team A")
        self.assertEqual(len(players), 11)
        self.assertEqual(players[0].name, "Player 1")
        self.assertEqual(players[10].name, "Player 11")

    def test_get_players_manual_blank_name_falls_back(self):
        names = ["Virat", ""] + [f"X{i}" for i in range(3, 12)]
        players, _ = run(cm.get_players, ["1"] + names, "Team A")
        self.assertEqual(players[0].name, "Virat")
        self.assertEqual(players[1].name, "Player 2")  # blank -> default
        self.assertEqual(len(players), 11)

    def test_get_team_setup_default_names(self):
        (a, a_players, b, b_players), _ = run(
            cm.get_team_setup, ["", "", "2", "2"]
        )
        self.assertEqual((a, b), ("Team A", "Team B"))
        self.assertEqual(len(a_players), 11)
        self.assertEqual(len(b_players), 11)


# ----------------------------------------------------------------------
class TestToss(unittest.TestCase):
    def test_winner_bats(self):
        (bat, bowl), _ = run(cm.do_toss, ["Team A", "BAT"], "Team A", "Team B")
        self.assertEqual((bat, bowl), ("Team A", "Team B"))

    def test_winner_bowls(self):
        (bat, bowl), _ = run(cm.do_toss, ["Team B", "BOWL"], "Team A", "Team B")
        self.assertEqual((bat, bowl), ("Team A", "Team B"))

    def test_case_insensitive_and_retries_on_bad_input(self):
        inputs = ["nobody", "team b", "maybe", "bat"]
        (bat, bowl), out = run(cm.do_toss, inputs, "Team A", "Team B")
        self.assertEqual((bat, bowl), ("Team B", "Team A"))
        self.assertIn("exact team name", out)
        self.assertIn("BAT or BOWL", out)


# ----------------------------------------------------------------------
class TestAskBallOutcome(unittest.TestCase):
    def test_valid_inputs(self):
        for raw, expected in [("4", "4"), ("w", "W"), ("wd", "WD"), (" nb ", "NB")]:
            result, _ = run(cm.ask_ball_outcome, [raw], 1, 1, cm.Player("A"))
            self.assertEqual(result, expected)

    def test_invalid_then_valid(self):
        result, out = run(cm.ask_ball_outcome, ["7", "abc", "", "6"], 1, 1, cm.Player("A"))
        self.assertEqual(result, "6")
        self.assertEqual(out.count("Invalid input"), 3)


# ----------------------------------------------------------------------
class TestMiniScoreboard(unittest.TestCase):
    def test_shows_required_runs_when_chasing(self):
        s, ns = cm.Player("A"), cm.Player("B")
        buf = io.StringIO()
        with redirect_stdout(buf):
            cm.print_mini_scoreboard("X", s, ns, 10, 1, 12, target=20)
        out = buf.getvalue()
        self.assertIn("10/1", out)
        self.assertIn("Overs: 2.0", out)
        self.assertIn("Need 10 run(s) from 18 ball(s)", out)

    def test_no_target_line_in_first_innings(self):
        s, ns = cm.Player("A"), cm.Player("B")
        buf = io.StringIO()
        with redirect_stdout(buf):
            cm.print_mini_scoreboard("X", s, ns, 10, 1, 12)
        self.assertNotIn("Need", buf.getvalue())


# ----------------------------------------------------------------------
class TestInnings(unittest.TestCase):
    def test_all_dots_full_five_overs(self):
        players = make_players()
        (runs, wkts), out = run(cm.play_innings, ["0"] * 30, "A", players, "B")
        self.assertEqual((runs, wkts), (0, 0))
        self.assertIn("5.0 overs", out)
        # strike swaps every over: opener gets overs 1,3,5 (18 balls), partner 12
        self.assertEqual(players[0].balls, 18)
        self.assertEqual(players[1].balls, 12)

    def test_odd_run_rotates_strike(self):
        players = make_players()
        (runs, _), _ = run(cm.play_innings, ["1", "0"] + ["0"] * 28, "A", players, "B")
        self.assertEqual(runs, 1)
        self.assertEqual(players[0].runs, 1)
        # ball 1 -> P0, balls 2-6 -> P1; then P0 (o2), P1 (o3), P0 (o4), P1 (o5)
        self.assertEqual(players[0].balls, 13)
        self.assertEqual(players[1].balls, 17)

    def test_even_run_keeps_strike(self):
        players = make_players()
        (runs, _), _ = run(cm.play_innings, ["4", "6"] + ["0"] * 28, "A", players, "B")
        self.assertEqual(runs, 10)
        self.assertEqual(players[0].runs, 10)  # same batsman faced both balls

    def test_wide_adds_run_but_not_a_ball(self):
        players = make_players()
        (runs, wkts), out = run(cm.play_innings, ["WD"] + ["0"] * 30, "A", players, "B")
        self.assertEqual((runs, wkts), (1, 0))
        self.assertIn("5.0 overs", out)       # still exactly 30 legal balls
        self.assertIn("Extras: 1", out)
        self.assertEqual(players[0].runs, 0)   # extras don't go to batsman

    def test_no_ball_adds_run_but_not_a_ball(self):
        players = make_players()
        (runs, _), out = run(cm.play_innings, ["NB"] + ["0"] * 30, "A", players, "B")
        self.assertEqual(runs, 1)
        self.assertIn("5.0 overs", out)
        self.assertIn("Extras: 1", out)

    def test_wicket_brings_in_next_batsman(self):
        players = make_players()
        (runs, wkts), _ = run(cm.play_innings, ["W"] + ["0"] * 29, "A", players, "B")
        self.assertEqual((runs, wkts), (0, 1))
        self.assertTrue(players[0].out)
        self.assertEqual(players[0].how_out, "out")
        self.assertEqual(players[0].balls, 1)
        self.assertGreater(players[2].balls, 0)  # next man in faced the next ball

    def test_all_out_after_ten_wickets(self):
        players = make_players()
        (runs, wkts), out = run(cm.play_innings, ["W"] * 10, "A", players, "B")
        self.assertEqual(wkts, 10)
        self.assertIn("ALL OUT", out)
        self.assertEqual(sum(p.out for p in players), 10)
        self.assertEqual(sum(not p.out for p in players), 1)  # exactly one left not out

    def test_chase_ends_immediately_when_target_reached(self):
        players = make_players()
        # only ONE input supplied - if the game asked for more it would crash
        (runs, wkts), out = run(cm.play_innings, ["6"], "B", players, "A", target=6)
        self.assertEqual((runs, wkts), (6, 0))
        self.assertIn("reached the target", out)

    def test_chase_falls_short(self):
        players = make_players()
        (runs, wkts), out = run(
            cm.play_innings, ["0"] * 30, "B", players, "A", target=50
        )
        self.assertEqual((runs, wkts), (0, 0))
        self.assertNotIn("reached the target", out)

    def test_scorecard_only_lists_players_who_batted(self):
        players = make_players()
        _, out = run(cm.play_innings, ["0"] * 30, "A", players, "B")
        self.assertIn("P0", out)
        self.assertIn("P1", out)
        self.assertNotIn("P5", out)


# ----------------------------------------------------------------------
class TestResult(unittest.TestCase):
    def _result(self, *args):
        buf = io.StringIO()
        with redirect_stdout(buf):
            cm.declare_result(*args)
        return buf.getvalue()

    def test_first_team_wins_by_runs(self):
        self.assertIn("A WIN by 10 run(s)", self._result("A", 50, 3, "B", 40, 5))

    def test_second_team_wins_by_wickets(self):
        self.assertIn("B WIN by 6 wicket(s)", self._result("A", 40, 3, "B", 41, 4))

    def test_tie(self):
        self.assertIn("TIED", self._result("A", 30, 2, "B", 30, 4))


# ----------------------------------------------------------------------
class TestFullMatch(unittest.TestCase):
    def test_complete_match_chase_won_with_all_wickets_in_hand(self):
        inputs = (
            ["Alpha", "Beta", "2", "2"]      # team names + auto players
            + ["alpha", "BAT"]               # toss
            + ["1"] * 30                     # Alpha: 30 runs
            + ["6"] * 6                      # Beta chases 31: 36 runs in 6 balls
        )
        _, out = run(cm.play_match, inputs)
        self.assertIn("Alpha: 30/0", out)
        self.assertIn("Beta: 36/0", out)
        self.assertIn("Beta WIN by 10 wicket(s)", out)

    def test_main_replays_until_user_says_no(self):
        with patch.object(cm, "play_match") as fake_match:
            buf = io.StringIO()
            with patch("builtins.input", side_effect=["yes", "y", "no"]), \
                    redirect_stdout(buf):
                with self.assertRaises(SystemExit):
                    cm.main()
        self.assertEqual(fake_match.call_count, 3)
        self.assertIn("Thanks for playing", buf.getvalue())


if _name_ == "_main_":
    unittest.main(verbosity=2)