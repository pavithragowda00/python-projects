# Filter and print only high-risk indicators (IPs)

indicators = [
    {"ip": "1.1.1.1", "score": 10, "source": "Firewall", "type": "dns"},
    {"ip": "8.8.8.8", "score": 55, "source": "SIEM", "type": "dns"},
    {"ip": "203.0.113.5", "score": 85, "source": "EDR", "type": "c2"},
    {"ip": "10.0.0.5", "score": 90, "source": "IDS", "type": "scanner"},
]

HIGH_THRESHOLD = 80

print(f"High-risk indicators (score >= {HIGH_THRESHOLD}):")

for item in indicators:
    ip = item["ip"]
    score = item["score"]
    source = item["source"]
    ioc_type = item["type"]

    if score >= HIGH_THRESHOLD:
        print(f"- IP {ip} (type: {ioc_type}) from {source} with score {score}")

