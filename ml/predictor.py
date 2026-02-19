from baseline import calculate_baseline_need
from deficit import calculate_deficit
from stress import calculate_heat_stress
from behavior import calculate_behavior_factor
# main function
def predict(input_data:dict)-> dict:
    baseline_ml = calculate_baseline_need(input_data["weight"])
    deficit_info=calculate_deficit(
        baseline_need=baseline_ml,
        daily_intake=input_data["daily_intake"]
        )
    deficit_score = deficit_info["deficit_score"]
    heat_stress_score = calculate_heat_stress(
        temperature=input_data["temperature"],
        humidity=input_data["humidity"],
        mist_usage=input_data["mist_usage"]
        )
    behavior_factor = calculate_behavior_factor(
        last_drink_minutes=input_data["last_drink_minutes"]
        )
    #combined risk - the range is from 0 to 1

    combined_risk = deficit_score * heat_stress_score * behavior_factor
    
    #Mapping combined risk to risk levels

    if combined_risk < 0.1:
        risk_level = "low"
        next_drink_minutes = 50
    elif combined_risk < 0.25:
        risk_level = "moderate"
        next_drink_minutes = 25
    elif combined_risk < 0.5:
        risk_level = "high"
        next_drink_minutes = 12
    else:
        risk_level = "critical"
        next_drink_minutes = 0  # immediate

    recommended_ml = int(deficit_info["deficit_ml"] / 2)

    return {
        "hydration_score": round(1 - deficit_score, 3),  # high score = hydrated
        "heat_stress_score": heat_stress_score,
        "risk_level": risk_level,
        "next_drink_minutes": next_drink_minutes,
        "recommended_ml": recommended_ml
    }
if __name__ == "__main__":
    sample_input = {
        "weight": 70,
        "temperature": 35,
        "humidity": 70,
        "mist_usage": 20,
        "last_drink_minutes": 50,
        "daily_intake": 900,
        "time_of_day_ratio": 0.58
    }

    result = predict(sample_input)
    print(result)


