import json
import helpers

def convert_gender_time(
    time_input: str, 
    course: str, 
    event: str, 
    from_gender: str, 
    json_path: str = "base_times.json"
) -> dict:
    """
    Converts a swim time between genders using World Aquatics (FINA) points.
    Accepts string inputs like '1:45.23' or '20.50'.
    """
    time_sec = helpers.time_str_to_seconds(time_input)
    course = course.upper()
    event = event.upper()
    from_gender = from_gender.upper()
    to_gender = "W" if from_gender == "M" else "M"

    with open(json_path, "r") as f:
        base_times = json.load(f)

    try:
        base_from = base_times[course][from_gender][event]
        base_to = base_times[course][to_gender][event]
    except KeyError as e:
        raise ValueError(f"Invalid key in base_times.json: {e}")

    # Calculate World Aquatics Points
    points = int(1000 * (base_from / time_sec) ** 3)

    # Convert Points to Target Gender Time
    converted_sec = base_to * ((1000 / points) ** (1 / 3))

    return {
        "points": points,
        "input_time_str": helpers.seconds_to_time_str(time_sec),
        "converted_time_str": helpers.seconds_to_time_str(converted_sec),
        "target_gender": to_gender
    }

# --- Usage Example ---
if __name__ == "__main__":
    course = input("Enter course (SCM, SCY, LCM): ").strip()
    event = input("Enter event (e.g., 50_FREE, 100_FLY): ").strip()
    gender = input("Is the input time Men's or Women's? (M/W): ").strip()
    raw_time = input("Enter time (e.g., 1:45.23 or 20.50): ").strip()

    res = convert_gender_time(raw_time, course, event, gender)

    print(f"\n--- Result ---")
    print(f"Input Time: {res['input_time_str']}")
    print(f"Points: {res['points']}")
    print(f"Equivalent {res['target_gender']} Time: {res['converted_time_str']}")