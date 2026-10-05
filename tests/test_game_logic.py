from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_hints_go_lower():
    # Bug fix: a guess above the secret used to say "Go HIGHER!" instead of "Go LOWER!"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message

def test_too_low_hints_go_higher():
    # Bug fix: a guess below the secret used to say "Go LOWER!" instead of "Go HIGHER!"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message

def test_hint_direction_matches_when_types_mismatch():
    # Same hint-direction bug fix, but through the except TypeError fallback
    # (triggered when guess/secret are different types, e.g. int vs str)
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"
    assert "LOWER" in message

    outcome, message = check_guess(40, "50")
    assert outcome == "Too Low"
    assert "HIGHER" in message
