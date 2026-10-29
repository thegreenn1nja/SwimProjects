import json
import helpers

def time_from_points(
        score_input: str,
        course: str,
        event: str,
        gender: str,
        json_path: str = "base_times.json"
) -> dict:
    try:
        score = float(score_input)
    except ValueError:
        raise ValueError(f"Invalid score input: {score_input}")

    course = course.upper()
    event = event.upper()
    gender = gender.upper()

    with open(json_path, "r") as f:
        base_times = json.load(f)

    try:
        base = base_times[course][gender][event]
    except KeyError as e:
        raise ValueError(f"Invalid key in base_times.json: {e}")

    time_sec = base / ((score / 1000) ** (1/3))

    return {
        "gender": gender,
        "event": event,
        "points": score,
        "time_str": helpers.seconds_to_time_str(time_sec)
    }

if __name__ == "__main__":
    course = input("(SCM, SCY, LCM): ").strip()
    event = input("Enter event (e.g. 50_FREE): ").strip()
    gender = input("M/W?: ").strip()
    score = input("Enter desired score: ").strip()

    res = time_from_points(score, course, event, gender)

    print("\n--- Result ---")
    print(f"Gender: {res['gender']}")
    print(f"Event: {res['event']}")
    print(f"Input Score: {res['points']}")
    print(f"Target Time: {res['time_str']}")