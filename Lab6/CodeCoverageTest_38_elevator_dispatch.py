from elevator_dispatch import door_action, next_direction, pick_elevator


def test_next_direction_returns_all_directions():
    assert next_direction(3, "up", [5, 1]) == "up"
    assert next_direction(3, "up", [1]) == "down"
    assert next_direction(3, "down", [1, 5]) == "down"
    assert next_direction(3, "down", [5]) == "up"
    assert next_direction(3, "idle", [5]) == "up"
    assert next_direction(3, "idle", [1]) == "down"
    assert next_direction(3, "idle", []) == "idle"


def test_door_action_returns_all_actions():
    assert door_action(100, False, True) == "hold_open"
    assert door_action(631, False, False) == "overload"
    assert door_action(100, True, False) == "reopen"
    assert door_action(100, False, False) == "close"


def test_pick_elevator_selects_best_car():
    assert pick_elevator([], 5) is None
    assert pick_elevator(
        [("A", 1, False), ("B", 8, True), ("C", 5, True)],
        5,
    ) == "C"
