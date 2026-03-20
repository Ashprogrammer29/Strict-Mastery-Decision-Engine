import sys
import statistics
import json
import argparse

class StrictMasteryEngine:
    def __init__(self, threshold=85.0, max_attempts=3):
        self.threshold = threshold
        self.max_attempts = max_attempts

    def evaluate(self, scores):
        # Validation: Ensure scores are numeric and within 0-100
        validated_scores = []
        for s in scores:
            try:
                val = float(s)
                if not (0 <= val <= 100):
                    return {"status": "DATA_ERROR", "reason": f"Score {val} out of range (0-100)."}
                validated_scores.append(val)
            except (ValueError, TypeError):
                return {"status": "DATA_ERROR", "reason": f"Invalid non-numeric input: {s}"}

        attempts = len(validated_scores)
        if attempts == 0:
            return {"status": "DATA_ERROR", "reason": "No scores provided."}

        latest = validated_scores[-1]
        
        # Weighted Score (S_v) calculation
        if attempts == 1:
            sw = latest
        else:
            sw = round((latest * 0.7) + (validated_scores[-2] * 0.3), 2)

        # Volatility Analysis (Standard Deviation)
        std_dev = round(statistics.stdev(validated_scores), 2) if attempts > 1 else 0.0

        # Decision Hierarchy
        if sw >= self.threshold:
            status = "PROGRESS"
            reason = f"Mastery achieved with weighted score of {sw}%."
        elif attempts >= self.max_attempts:
            status = "PIVOT"
            reason = f"Threshold not met within {attempts} attempts. Final S_v: {sw}%."
        else:
            status = "RETRY"
            reason = f"S_v {sw}% is below {self.threshold}%. {self.max_attempts - attempts} attempt(s) remaining."

        return {
            "status": status,
            "weighted_score": sw,
            "volatility": std_dev,
            "attempts": attempts,
            "reason": reason
        }

def main():
    parser = argparse.ArgumentParser(description="Strict Mastery Decision Engine")
    parser.add_argument("scores", nargs="?", help="Comma-separated scores (e.g., '60,75,86')")
    args = parser.parse_args()

    engine = StrictMasteryEngine()

    if args.scores:
        # Runtime execution mode (for Docker/External Systems)
        input_list = args.scores.split(',')
        result = engine.evaluate(input_list)
        # Structured JSON output as requested
        print(json.dumps(result, indent=2))
    else:
        # Internal diagnostic mode (if run without arguments)
        print("Mastery Engine Active. Provide comma-separated scores as an argument.")

if __name__ == "__main__":
    main()