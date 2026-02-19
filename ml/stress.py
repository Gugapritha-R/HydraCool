# stress.py

def calculate_heat_stress(
    temperature: float,
    humidity: float,
    mist_usage: float
) -> float:
    """
    Calculates environmental heat stress score (0 to 1).

    Parameters:
    - temperature: current temperature in °C
    - humidity: percentage (0–100)
    - mist_usage: seconds of recent mist usage (helps cool down)

    Returns:
    - heat_stress_score: float between 0 (no stress) and 1 (extreme stress)
    """

    # Step 1: Temperature factor
    # Assume normal comfort = 22°C, extreme heat = 40°C
    temp_min = 22
    temp_max = 40
    temp_factor = (temperature - temp_min) / (temp_max - temp_min)
    temp_factor = min(max(temp_factor, 0.0), 1.0)  # clamp 0–1

    # Step 2: Humidity factor
    # Normal humidity = 30%, extreme = 90%
    hum_min = 30
    hum_max = 90
    hum_factor = (humidity - hum_min) / (hum_max - hum_min)
    hum_factor = min(max(hum_factor, 0.0), 1.0)

    # Step 3: Mist usage factor
    # More mist reduces stress slightly
    # Assuming max effective mist = 60 seconds
    mist_max = 60
    mist_factor = min(max(mist_usage / mist_max, 0.0), 1.0)
    mist_reduction = 0.2 * mist_factor  # reduces stress by up to 20%
    
    # Step 4: Combine factors
    raw_score = (0.6 * temp_factor) + (0.4 * hum_factor)  # weight temperature more
    heat_stress_score = max(min(raw_score - mist_reduction, 1.0), 0.0)

    return round(heat_stress_score, 3)


# Optional test
if __name__ == "__main__":
    temperature = 35
    humidity = 70
    mist_usage = 20  # seconds

    score = calculate_heat_stress(temperature, humidity, mist_usage)
    print("Heat Stress Score:", score)
