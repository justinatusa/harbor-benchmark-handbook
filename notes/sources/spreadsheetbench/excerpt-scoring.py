# Excerpt. Not a clone.
# Source: https://github.com/RUCKBReasoning/SpreadsheetBench
# Commit: 49b73a94775fb489063f60ca1865e3a650079a79
# File: evaluation/evaluation.py
# Numeric cells are rounded to 2 decimals, then compared with ==.
# Color checks exist but are commented out in cell_level_compare.
# At this commit, evaluation() sets proc_path to the input xlsx;
# the model-output path on the next line is commented out.

def transform_value(v):
    if isinstance(v, (int, float)):
        v = round(float(v), 2)
    elif isinstance(v, datetime.time):
        v = str(v)[:-3]
    elif isinstance(v, datetime.datetime):
        v = round(datetime_to_float(v), 0)
    elif isinstance(v, str):
        try:
            v = round(float(v), 2)
        except ValueError:
            pass
    return v

def compare_cell_value(v1, v2):

    v1 = transform_value(v1)
    v2 = transform_value(v2)
    if (v1 == "" and v2 is None) or (v1 is None and v2 == ""):
        return True
    if (v1 == "" and v2 == "") or (v1 is None and v2 is None):
        return True
    if type(v1) != type(v2):
        # print(type(v1), type(v2))
        return False
    if v1 == v2:
        return True
    else:
        return False

# evaluation() lines 212-222 at this commit:
#   gt_path = .../{test_case_idx + 1}_{id}_answer.xlsx
#   proc_path = .../{test_case_idx + 1}_{id}_input.xlsx
#   # proc_path = .../outputs/{setting}_{model}/{test_case_idx + 1}_{id}_output.xlsx
#   soft_restriction = test_case_results.count(1) / len(test_case_results)
#   hard_restriction = 0 if 0 in test_case_results else 1
