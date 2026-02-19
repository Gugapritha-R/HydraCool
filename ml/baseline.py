# baseline.py

def calculate_baseline_need(weight: float, temperature: float) -> float:
    """
    Calculate baseline daily hydration requirement (ml).

    Base formula:
        weight × 35 ml

    Environmental adjustment:
        If temperature > 25°C,
        increase need by 1% per degree.
    """

    # Step 1: physiological base
    base_need = weight * 35

    # Step 2: temperature adjustment
    if temperature > 25:
        adjustment_factor = 1 + ((temperature - 25) * 0.01)
    else:
        adjustment_factor = 1.0

    adjusted_need = base_need * adjustment_factor

    return adjusted_need
