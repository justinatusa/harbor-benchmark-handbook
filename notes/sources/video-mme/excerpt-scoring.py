# Verbatim excerpt, not a clone.
# https://github.com/thanku-all/parse_answer/blob/afd52cfe3dde5b3685e0d4f760c10c756860c758/eval_your_results.py
# Linked from MME-Benchmarks/Video-MME README at 06c2315b892f88578f81d73205d07cf576f292b9
# The list below is copied as published, including adjacent string literals with no comma.

def extract_characters_regex(s):
    s = s.strip()
    answer_prefixes = [
        "The best answer is",
        "The correct answer is",
        "The answer is",
        "The answer",
        "The best option is"
        "The correct option is",
        "Best answer:"
        "Best option:",
        "Answer:",
        "Option:",
        "The correct answer",
        "The correct option",
    ]
    for answer_prefix in answer_prefixes:
        s = s.replace(answer_prefix, "")

    if len(s.split()) > 10 and not re.search("[ABCD]", s):
        return ""
    matches = re.search(r'[ABCD]', s)
    if matches is None:
        return ""
    return matches[0]

# same file, lines 167-175:
#   gt_answer = question[gt_answer_key]
#   response = question[your_answer_key]
#   extration = extract_characters_regex(response)
#   q_type_dict[video_type][q_type]["correct"] += extration == gt_answer
