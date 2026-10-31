from elevator_dispatch import door_action, next_direction, pick_elevator


def test_next_direction_covers_empty_and_unmatched_paths():
    assert next_direction(3, "up", []) == "idle"
    assert next_direction(3, "down", []) == "idle"
    assert next_direction(3, "down", [5]) == "up"
    assert next_direction(3, "other", []) == "idle"
    assert next_direction(3, "other", [1, 3]) == "down"


def test_door_action_covers_threshold_and_priority_paths():
    assert door_action(630, False, False) == "close"
    assert door_action(631, True, False) == "overload"
    assert door_action(631, True, True) == "hold_open"


def test_pick_elevator_covers_comparison_and_idle_paths():
    assert pick_elevator([("moving", 5, False)], 5) == "moving"
    assert pick_elevator(
        [("first", 1, True), ("better", 4, True), ("worse", 9, True)],
        5,
    ) == "better"
    assert pick_elevator(
        [("first", 2, True), ("tie", 8, True)],
        5,
    ) == "first"
