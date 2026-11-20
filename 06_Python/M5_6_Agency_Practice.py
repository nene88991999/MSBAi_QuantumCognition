"""Ungraded agency practice using explicitly constructed teaching data.
Run with Python 3. No API access or third-party packages are needed.
"""
from collections import Counter
import csv
from pathlib import Path

def summarize_histories(rows):
    valid = [r for r in rows if r.get("a_first") in {"off", "on"} and r.get("a_return") in {"off", "on"}]
    ids = [r["respondent_id"] for r in valid]
    if len(ids) != len(set(ids)):
        raise ValueError("Each paired history must have a unique respondent ID.")
    if not valid:
        raise ValueError("No valid paired histories.")
    n = len(valid)
    first = sum(r["a_first"] == "off" for r in valid) / n
    last = sum(r["a_return"] == "off" for r in valid) / n
    return {"valid_paired_histories": n, "excluded_histories": len(rows)-n,
            "initial_off": first, "return_off": last,
            "net_change_percentage_points": 100*(last-first),
            "revision_rate": sum(r["a_first"] != r["a_return"] for r in valid)/n,
            "paths": dict(Counter((r["a_first"],r["a_return"]) for r in valid))}

def expected_loss(renewal_probability, decline_value_advantage):
    if not 0 <= renewal_probability <= 1:
        raise ValueError("Use a probability between zero and one.")
    return renewal_probability * decline_value_advantage

if __name__ == "__main__":
    data = Path(__file__).parent / "data" / "M6_Return_Histories.csv"
    with data.open(newline="") as stream:
        result = summarize_histories(list(csv.DictReader(stream)))
    print("Constructed practice histories:", result)
    direct = expected_loss(.20, 10)
    reminder = expected_loss(.35, 10)
    print(f"Expected losses: direct ${direct:.2f}; reminder ${reminder:.2f}; difference ${reminder-direct:.2f}")
    print("Assumptions: same offer, independently specified stable values, equal procedure costs.")
