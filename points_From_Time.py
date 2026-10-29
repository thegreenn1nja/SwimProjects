import json
import helpers

def points_from_time(
        time_input: str,
        course: str,
        event: str,
        gender,
        json_path: str = "base_times.json"
) -> dict:
    time_sec = helpers.time_str_to_seconds(time_input)
    course = course.upper()
    event = event.upper()
    gender = gender.upper()

    with open(json_path, "r") as f:
        base_times = json.load(f)

    try:
        base = base_times[course][gender][event]
    except KeyError as e:
        raise ValueError(f"Invalid key in base_times.json: {e}")

    points = int(1000 * (base / time_sec) ** 3)

    return {
        "gender": gender,
        "event": event,
        "points": points,
        "input_time_str": helpers.seconds_to_time_str(time_sec)
    }

if __name__ == "__main__":
    course = input("(SCM, SCY, LCM): ").strip()
    event = input("Enter event (e.g. 50_FREE): ").strip()
    gender = input("M/W?: ").strip()
    raw_time = input("Enter time: ").strip()

    res = points_from_time(raw_time, course, event, gender)

    print("\n--- Result ---")
    print(f"Gender: {res['gender']}")
    print(f"Event: {res['event']}")
    print(f"Input Time: {res['input_time_str']}")
    print(f"Points: {res['points']}")