import csv
from pathlib import Path

HIGH_THRESHOLD = 80
MEDIUM_THRESHOLD = 50

INPUT_FILE = Path("indicators.csv")
OUTPUT_FILE = Path("risk_assessment.csv")

def parse_csv_file(file_path):
    """Parse CSV file with error handling, return indicators + errors"""
    indicators = []
    errors = []
    
    try:
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            for line_num, row in enumerate(reader, start=1):
                if len(row) != 3 or not any(row):  # Skip empty/malformed rows
                    continue
                    
                try:
                    ip, score_str, source = [field.strip() for field in row]
                    score = int(score_str)
                    
                    indicator = {
                        "ip": ip,
                        "score": score,
                        "source": source,
                        "risk": classify_risk(score)
                    }
                    indicators.append(indicator)
                    
                except (ValueError, IndexError) as e:
                    errors.append(f"Line {line_num}: {e} | row: {row}")
                    
    except FileNotFoundError:
        errors.append(f"File {file_path} not found")
        
    return indicators, errors

def classify_risk(score):
    if score >= HIGH_THRESHOLD:
        return "HIGH"
    elif score >= MEDIUM_THRESHOLD:
        return "MEDIUM"
    return "LOW"

def write_results(indicators, errors, output_path):
    """Write results to CSV file"""
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Write valid indicators
        writer.writerow(["IP", "Score", "Source", "Risk"])
        for ind in indicators:
            writer.writerow([ind["ip"], ind["score"], ind["source"], ind["risk"]])
        
        # Write separator and errors
        writer.writerow([])
        writer.writerow(["ERRORS SUMMARY"])
        for error in errors:
            writer.writerow(["ERROR", error])

# MAIN EXECUTION
if __name__ == "__main__":
    print("🔍 Parsing indicators.csv...")
    
    indicators, errors = parse_csv_file(INPUT_FILE)
    
    print(f"✅ Parsed {len(indicators)} valid indicators")
    print(f"❌ Found {len(errors)} errors")
    
    # Show high risks
    high_risks = [i for i in indicators if i["risk"] == "HIGH"]
    if high_risks:
        print("\n🚨 HIGH RISK INDICATORS:")
        for ind in high_risks:
            print(f"  - {ind['ip']} ({ind['source']}) score: {ind['score']}")
    
    # Write results
    write_results(indicators, errors, OUTPUT_FILE)
    print(f"\n💾 Results saved to {OUTPUT_FILE}")
