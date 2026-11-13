def parse_request(text):
    if not isinstance(text, str):
        return None

    parts = text.split("->")
    if len(parts) != 2:
        return None

    try:
        start = int(parts[0].strip())
        end = int(parts[1].strip())
    except (TypeError, ValueError):
        return None

    if start < 0 or end < 0:
        return None

    return start, end


def total_travel(floors_csv):
    if not isinstance(floors_csv, str):
        return None

    if not floors_csv.strip():
        return 0

    try:
        floors = [int(item.strip()) for item in floors_csv.split(",")]
    except (TypeError, ValueError):
        return None

    if any(floor < 0 for floor in floors):
        return None

    return sum(
        abs(floors[index + 1] - floors[index])
        for index in range(len(floors) - 1)
    )


def load_percent(text):
    if not isinstance(text, str):
        return None

    parts = text.split(" of ")
    if len(parts) != 2:
        return None

    try:
        load = int(parts[0].strip())
        capacity = int(parts[1].strip())
    except (TypeError, ValueError):
        return None

    if capacity <= 0 or load < 0 or load > capacity:
        return None

    return load * 100 // capacity


def main():
    print("==== Running parse_request ====")
    user_input = input("Enter a request as FROM->TO (e.g. 5->9): ")
    result = parse_request(user_input)
    if result is None:
        print("Invalid request. Enter two non-negative floors as FROM->TO.")
    else:
        print("From and To:", result)

    print("\n==== Running total_travel ====")
    user_input = input("Enter floors visited as CSV (e.g. 1,5,3,9): ")
    result = total_travel(user_input)
    if result is None:
        print("Invalid floor list. Enter non-negative floor numbers separated by commas.")
    else:
        print("Floors Travelled:", result)

    print("\n==== Running load_percent ====")
    user_input = input("Enter load as 'X of Y' (e.g. 450 of 630): ")
    result = load_percent(user_input)
    if result is None:
        print("Invalid load. Ensure 0 <= load <= capacity and capacity is greater than zero.")
    else:
        print("Load Percent:", result)


if __name__ == "__main__":
    main()
