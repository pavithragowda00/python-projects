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
    high = medium = low = 0

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

    # Return a tuple (immutable)
    return final_level, high, medium, low

# Get the tuple summary
summary = summarize_incident(indicators)
print("Original summary tuple:", summary)

# Suppose we want to manually increase the high count by 1.
# Convert tuple -> list, modify, then back to tuple.
summary_list = list(summary)
summary_list[1] = summary_list[1] + 1  # index 1 is high count
adjusted_summary = tuple(summary_list)

print("Adjusted summary tuple:", adjusted_summary)
