def time_str_to_seconds(time_str: str) -> float:
    """Converts a time string ('1:45.23' or '22.50') to total seconds as a float."""
    parts = time_str.strip().split(":")
    if len(parts) == 1:
        return float(parts[0])
    elif len(parts) == 2:
        minutes = float(parts[0])
        seconds = float(parts[1])
        return minutes * 60 + seconds
    else:
        raise ValueError(f"Invalid time format: '{time_str}'. Expected 'MM:SS.ms' or 'SS.ms'.")

def seconds_to_time_str(total_seconds: float) -> str:
    """Formats floating seconds back into a standard swim time string (e.g., '1:45.23' or '22.50')."""
    minutes = int(total_seconds // 60)
    seconds = total_seconds % 60
    if minutes > 0:
        return f"{minutes}:{seconds:05.2f}"
    return f"{seconds:.2f}"

