HIGH_THRESHOLD = 80
MEDIUM_THRESHOLD = 50

csv_data = """
1.1.1.1,10,Firewall
8.8.8.8,abc,SIEM
203.0.113.5,85,EDR
badline
10.0.0.5,90,IDS
"""

def parse_csv_to_indicators(csv_text):
    indicators = []
    errors = []

    for line_num, line in enumerate(csv_text.strip().splitlines(), start=1):
        if not line.strip():
            continue

        try:
            parts = line.split(",")
            if len(parts) != 3:
                raise ValueError("Expected 3 fields (ip,score,source)")

            ip_str, score_str, source_str = parts

            indicator = {
                "ip": ip_str.strip(),
                "score": int(score_str.strip()),  # may raise ValueError
                "source": source_str.strip(),
            }
            indicators.append(indicator)

        except Exception as e:
            errors.append(f"Line {line_num} error: {e} | content: {line}")

    return indicators, errors

def classify_indicator(indicator):
    score = indicator["score"]
    if score >= HIGH_THRESHOLD:
        return "HIGH"
    elif score >= MEDIUM_THRESHOLD:
        return "MEDIUM"
    else:
        return "LOW"

indicators, errors = parse_csv_to_indicators(csv_data)

print("Parsed indicators:")
for item in indicators:
    level = classify_indicator(item)
    print(f"- IP {item['ip']} from {item['source']} -> {level} (score {item['score']})")

print("\nErrors:")
for err in errors:
    print(f"- {err}")
