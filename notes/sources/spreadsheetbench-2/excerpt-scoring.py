# 节选 evaluation/evaluation.py
# https://github.com/RUCKBReasoning/SpreadsheetBench-2
# commit 5c160265aa93c15b38e4034cbf1e09ab498335d9
# 比较函数只保留数值容差分支；错误占位和类型归一化未抄。
# 下面的 reg_ratio / accuracy 四行是原文。

def compare_cell_value(v1, v2, tolerance=0.01):

    # Handle ArrayFormula objects — compare by formula text
    if hasattr(v1, 'text') and hasattr(v2, 'text'):
        return v1.text == v2.text

    # Treat #DIV/0! and #N/A as equivalent to finance "not meaningful" placeholders.
    # E.g. golden=#DIV/0! and AI="N/A" (via IFERROR) should match.

    # For two numeric values, compare on raw values with tolerance only —
    # skip rounding to avoid boundary artifacts (e.g. -0.105 vs -0.10500000000000001)
    if isinstance(v1, (int, float)) and isinstance(v2, (int, float)):
        if v1 == v2:
            return True
        if v1 == 0 or v2 == 0:
            return abs(v1 - v2) <= tolerance
        return abs(v1 - v2) / max(abs(v1), abs(v2)) <= tolerance

# process_single_item:
    reg_ratio = round(regression_stats['correct'] / regression_stats['total'], 4) if regression_stats['total'] else 0.0
    mod_ratio = round(modification_stats['correct'] / modification_stats['total'], 4) if modification_stats['total'] else 0.0
    # If regression ratio >= 99.8%, treat as 1.0
    if reg_ratio >= 0.998:
        reg_ratio = 1.0
    accuracy = 1.0 if reg_ratio == 1.0 and mod_ratio == 1.0 else 0.0
