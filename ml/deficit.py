from datetime import datetime


def get_time_ratio(current_time=None, wake_hour=7, sleep_hour=23):
    """
    Returns fraction (0 to 1) of hydration that should be completed
    based on current time within the wake window.
    """

    if current_time is None:
        current_time = datetime.now()

    current_hour = current_time.hour + current_time.minute / 60

    # Before wake time
    if current_hour <= wake_hour:
        return 0.0

    # After sleep time
    if current_hour >= sleep_hour:
        return 1.0

    total_awake_hours = sleep_hour - wake_hour
    hours_passed = current_hour - wake_hour

    return hours_passed / total_awake_hours


def calculate_deficit(
    baseline_need: float,
    daily_intake: float,
    current_time=None,
    wake_hour: int = 7,
    sleep_hour: int = 23
) -> dict:
    """
    Calculates hydration deficit details.

    Parameters:
    - baseline_need: total required intake for the day (ml)
    - daily_intake: how much user has consumed so far (ml)
    - current_time: optional datetime object
    - wake_hour: user wake time (default 7 AM)
    - sleep_hour: user sleep time (default 11 PM)

    Returns:
    Dictionary containing:
    - baseline_need
    - time_ratio
    - expected_intake
    - daily_intake
    - deficit_ml
    - deficit_score (0 to 1)
    """

    # Step 1: Time progression
    time_ratio = get_time_ratio(current_time, wake_hour, sleep_hour)

    # Step 2: Expected intake by now
    expected_intake = baseline_need * time_ratio

    # Step 3: Raw deficit
    deficit_ml = expected_intake - daily_intake

    if deficit_ml < 0:
        deficit_ml = 0.0

    # Step 4: Normalized deficit score
    deficit_score = deficit_ml / baseline_need if baseline_need > 0 else 0.0
    deficit_score = min(max(deficit_score, 0.0), 1.0)

    return {
        "baseline_need_ml": round(baseline_need, 2),
        "time_ratio": round(time_ratio, 3),
        "expected_intake_ml": round(expected_intake, 2),
        "daily_intake_ml": round(daily_intake, 2),
        "deficit_ml": round(deficit_ml, 2),
        "deficit_score": round(deficit_score, 3)
    }


# Optional test block
if __name__ == "__main__":
    baseline = 2450
    intake = 900

    result = calculate_deficit(baseline, intake)
    print(result)
