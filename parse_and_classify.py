HIGH_THRESHOLD = 80
MEDIUM_THRESHOLD = 50

# Simulated "CSV" input: ip,score,source (like a tiny log extract)
csv_data = """
1.1.1.1,10,Firewall
8.8.8.8,55,SIEM
203.0.113.5,85,EDR
10.0.0.5,90,IDS
"""

def parse_csv_to_indicators(csv_text):
    indicators = []

    # Split into lines and loop
    for line in csv_text.strip().splitlines():
        # Skip empty lines
        if not line.strip():
            continue

        ip_str, score_str, source_str = line.split(",")

        indicator = {
            "ip": ip_str.strip(),
            "score": int(score_str.strip()),
            "source": source_str.strip(),
        }
        indicators.append(indicator)

    return indicators

def classify_indicator(indicator):
    score = indicator["score"]
    if score >= HIGH_THRESHOLD:
        return "HIGH"
    elif score >= MEDIUM_THRESHOLD:
        return "MEDIUM"
    else:
        return "LOW"

indicators = parse_csv_to_indicators(csv_data)

for item in indicators:
    level = classify_indicator(item)
    print(f"IP {item['ip']} from {item['source']} -> {level} (score {item['score']})")
