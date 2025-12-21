# Simple risk classification for IP addresses

# 1. Input: a list of IPs with numeric scores (0-100)
ips = [
    {"ip": "1.1.1.1", "score": 10},
    {"ip": "8.8.8.8", "score": 55},
    {"ip": "203.0.113.5", "score": 85},
]

# 2. Loop through each IP and classify based on score
for item in ips:
    ip = item["ip"]
    score = item["score"]

    if score >= 80:
        level = "HIGH"
    elif score >= 50:
        level = "MEDIUM"
    else:
        level = "LOW"

    print(f"IP {ip} has score {score} -> Risk {level}")
