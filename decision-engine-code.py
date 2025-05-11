"""
Bluevine – automatic decision engine WITH summary counts
--------------------------------------------------------
"""

import pandas as pd
from pathlib import Path

FILE  = Path("Bluevine_Analyst_Exam_-_Data.xlsx")
SHEET = "Data"

# ------------ Load & normalise column names ------------
df = pd.read_excel(FILE, sheet_name=SHEET)
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(' ', '_')
      .str.replace(r'[^\w]', '', regex=True)
)

STATUS = "check_final_status"              # Posted / Returned
SCORE  = "fraud_model_score"
AMOUNT = "dollar_amount"
RISK   = "account_risk_level"
PAST   = "count_of_past_deposited_checks"
BAL    = "balance_at_time_of_deposit"

# ------------ Decision logic ------------
def decide(row) -> str:
    score = row[SCORE]
    amt   = row[AMOUNT]
    risk  = row[RISK]
    past  = row[PAST]
    bal   = row[BAL]

    # 1) Reject – highest-risk pockets
    if (score > 0.90) \
       or (score > 0.80 and amt > 3_000) \
       or (risk == 1 and past <= 2):
        return "Reject"

    # 2) Hold 6 days – medium risk / high exposure
    if (0.70 <= score <= 0.90) \
       or (2_000 <= amt <= 10_000) \
       or (bal < 0):
        return "Hold6d"

    # 3) Otherwise – post funds immediately
    return "Post"

# Apply the decision function
df["decision"] = df.apply(decide, axis=1)

# =======================================================
#  A.  Counts in the raw data (final status)
# =======================================================
print("\n=== Raw data – final status counts ===")
print(df[STATUS].value_counts(dropna=False))

# =======================================================
#  B.  Counts *after* applying the new decision engine
# =======================================================
print("\n=== New decision counts ===")
print(df["decision"].value_counts())

# =======================================================
#  C.  Decision × Final-Status matrix  (counts & %)
# =======================================================
cross_counts = pd.crosstab(df["decision"], df[STATUS])
cross_perc   = pd.crosstab(df["decision"], df[STATUS], normalize="index")*100

print("\n=== Decision × Final status – counts ===")
print(cross_counts)

print("\n=== Decision × Final status – row percentages ===")
print(cross_perc.round(2))

# ---------- OPTIONAL: save to file ----------
# df.to_csv("bluevine_with_decision.csv", index=False)
