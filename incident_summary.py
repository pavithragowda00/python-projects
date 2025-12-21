HIGH_THRESHOLD = 80
MEDIUM_THRESHOLD = 50

indicators = [
    {"ip": "1.1.1.1", "score": 10, "source": "Firewall"},
    {"ip": "8.8.8.8", "score": 55, "source": "SIEM"},
    {"ip": "203.0.113.5", "score": 85, "source": "EDR"},
    {"ip": "10.0.0.5", "score": 90, "source": "IDS"},
]

def classify_indicator(indicator):
    score = indicator["score"]

    if score >= HIGH_THRESHOLD:
        return "HIGH"
    elif score >= MEDIUM_THRESHOLD:
        return "MEDIUM"
    else:
        return "LOW"


def summarize_incident(indicators_list):
    """Return highest level and counts (like an incident summary)."""
    high = 0
    medium = 0
    low = 0

    for item in indicators_list:
        level = classify_indicator(item)

        if level == "HIGH":
            high += 1
        elif level == "MEDIUM":
            medium += 1
        else:
            low += 1

    if high > 0:
        final_level = "HIGH"
    elif medium > 0:
        final_level = "MEDIUM"
    else:
        final_level = "LOW"

    return final_level, high, medium, low


final_level, high_count, med_count, low_count = summarize_incident(indicators)

print(f"Incident final level: {final_level}")
print(f"High: {high_count}, Medium: {med_count}, Low: {low_count}")
