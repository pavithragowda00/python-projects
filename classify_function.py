# Classify indicators using a reusable function

HIGH_THRESHOLD = 80
MEDIUM_THRESHOLD = 50

indicators = [
    {"ip": "1.1.1.1", "score": 10, "source": "Firewall"},
    {"ip": "8.8.8.8", "score": 55, "source": "SIEM"},
    {"ip": "203.0.113.5", "score": 85, "source": "EDR"},
    {"ip": "10.0.0.5", "score": 90, "source": "IDS"},
]

def classify_indicator(indicator):
    """Return risk level for a single indicator dict."""
    score = indicator["score"]

    if score >= HIGH_THRESHOLD:
        return "HIGH"
    elif score >= MEDIUM_THRESHOLD:
        return "MEDIUM"
    else:
        return "LOW"


for item in indicators:
    ip = item["ip"]
    source = item["source"]
    score = item["score"]

    risk = classify_indicator(item)

    print(f"IP {ip} from {source} has score {score} -> {risk} risk")
