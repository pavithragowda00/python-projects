# Calculate incident risk from multiple IPs

ips = [
    {"ip": "1.1.1.1", "score": 10},
    {"ip": "8.8.8.8", "score": 55},
    {"ip": "203.0.113.5", "score": 85},
    {"ip": "10.0.0.5", "score": 40},
]

total_score = 0
high_count = 0
medium_count = 0
low_count = 0

for item in ips:
    score = item["score"]
    total_score += score

    if score >= 80:
        high_count += 1
    elif score >= 50:
        medium_count += 1
    else:
        low_count += 1

# Avoid division by zero
if len(ips) > 0:
    average_score = total_score / len(ips)
else:
    average_score = 0

# Classify overall incident risk based on average
if average_score >= 80:
    incident_risk = "HIGH"
elif average_score >= 50:
    incident_risk = "MEDIUM"
else:
    incident_risk = "LOW"

print(f"Average score: {average_score:.1f}")
print(f"High: {high_count}, Medium: {medium_count}, Low: {low_count}")
print(f"Incident risk level: {incident_risk}")
