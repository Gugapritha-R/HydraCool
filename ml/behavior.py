# behavior.py

def calculate_behavior_factor(
    last_drink_minutes: float,
    min_interval: float = 20,
    max_interval: float = 180
) -> float:
    """
    Calculates a behavior factor based on the time since the last drink.

    Parameters:
    - last_drink_minutes: minutes since last intake
    - min_interval: minimum expected interval between drinks (default 20 min)
    - max_interval: maximum safe interval (default 180 min / 3 hours)

    Returns:
    - behavior_factor: float between 0 (good behavior) and 1 (high risk)
    """

    # Step 1: Clamp the interval
    if last_drink_minutes <= min_interval:
        return 0.0  # user is drinking frequently, low risk
    elif last_drink_minutes >= max_interval:
        return 1.0  # extremely delayed, high risk

    # Step 2: Normalize between min_interval and max_interval
    normalized = (last_drink_minutes - min_interval) / (max_interval - min_interval)

    # Clamp just in case
    behavior_factor = min(max(normalized, 0.0), 1.0)

    return round(behavior_factor, 3)


# Optional test
if __name__ == "__main__":
    last_drink = 50  # minutes since last sip
    factor = calculate_behavior_factor(last_drink)
    print("Behavior Factor:", factor)
