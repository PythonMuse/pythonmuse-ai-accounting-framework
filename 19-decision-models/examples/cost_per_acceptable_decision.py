# =============================================================================
# cost_per_acceptable_decision.py
# PythonMuse AI Accounting Framework -- Module 19: Decision Models
#
# Compares approaches to one repeated decision (for example, routing an AR
# exception) by cost per acceptable decision:
#
#   (model cost + review time + cost of wrong or missed items)
#                  divided by
#            decisions that came out right
#
# The point: the cheapest model is not always the cheapest process.
#
# DATA NOTICE: The numbers in data/decision_scenarios.csv are synthetic and
# for illustration only. Replace them with figures from your own testing.
# Do not use real company data until you have reviewed your organization's
# data policies.
# See: https://github.com/PythonMuse/ai-ledger/tree/main/articles/06-safe-ai-data-workflows
#
# Requires only the Python standard library. Run from this folder:
#   python cost_per_acceptable_decision.py
# =============================================================================

import csv
from pathlib import Path

# Step 1: Settings you can change.
# Loaded cost of one hour of reviewer time (synthetic).
REVIEWER_COST_PER_HOUR = 60.00
# How many items the process handles in a month (synthetic).
ITEMS_PER_MONTH = 10_000

DATA_FILE = Path(__file__).parent / "data" / "decision_scenarios.csv"


def cost_per_acceptable_decision(row):
    """Return (cost per item, cost per acceptable decision) for one approach."""
    model_cost = float(row["model_cost_per_item"])
    share_to_person = float(row["share_sent_to_person"])
    review_minutes = float(row["review_minutes_per_sent_item"])
    wrong_rate = float(row["wrong_or_missed_rate"])
    cost_per_wrong = float(row["cost_per_wrong_item"])

    # Review time: only the items sent to a person cost reviewer time.
    review_cost = share_to_person * (review_minutes / 60) * REVIEWER_COST_PER_HOUR

    # Cost of errors: wrong routing and missed exceptions.
    error_cost = wrong_rate * cost_per_wrong

    cost_per_item = model_cost + review_cost + error_cost

    # Divide by the share of decisions that came out right.
    return cost_per_item, cost_per_item / (1 - wrong_rate)


def main():
    # Step 2: Read the scenarios.
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    # Step 3: Calculate each approach.
    results = []
    for row in rows:
        per_item, per_good = cost_per_acceptable_decision(row)
        results.append((row["approach"], float(row["model_cost_per_item"]), per_item, per_good))

    # Step 4: Print the comparison, cheapest process first.
    print(f"Items per month: {ITEMS_PER_MONTH:,}   Reviewer cost per hour: ${REVIEWER_COST_PER_HOUR:,.2f}\n")
    print(f"{'Approach':<24}{'Model $/item':>14}{'Cost/item':>12}{'Per acceptable':>16}{'Monthly':>12}")
    for name, model_cost, per_item, per_good in sorted(results, key=lambda r: r[3]):
        monthly = per_good * ITEMS_PER_MONTH
        print(f"{name:<24}{model_cost:>14.4f}{per_item:>12.2f}{per_good:>16.2f}{monthly:>12,.0f}")

    # Step 5: Show the lesson, using the model rows only (model cost above zero).
    models = [r for r in results if r[1] > 0]
    cheapest_model = min(models, key=lambda r: r[1])
    costliest_process = max(results, key=lambda r: r[3])
    print(f"\nCheapest model per call:      {cheapest_model[0]}")
    print(f"Most expensive process:       {costliest_process[0]}")
    if cheapest_model[0] == costliest_process[0]:
        print("The cheapest model produced the most expensive process.")
    print("\nSynthetic numbers. Replace them with results from your own testing.")


if __name__ == "__main__":
    main()
