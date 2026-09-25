# 摘录自 evaluation/evaluate.py 的 evaluate()，不是整个仓库。
# 来源: https://github.com/mathllm/MATH-V/blob/a1f5cc3add200c0cd080fad463e500f44ef1fb41/evaluation/evaluate.py
# 抓取日: 2026-09-24 Asia/Shanghai
# 同目录 evaluation/utils.py 的 is_equal 在进程内比较字符串和 LaTeX，不调用另一个模型。

def evaluate(answer_file, regen_answer=False):
    lines = load_jsonl(answer_file)
    for line in tqdm(lines, desc='gen_correct'):
        raw_exampe = id_raw[line['id']]

        gt_answer = str(raw_exampe['answer'])
        if len(raw_exampe['options']) > 0:
            gt_answer_value = raw_exampe['options'][ord(gt_answer)-ord('A')]
        else:
            gt_answer_value = ''

        if 'model_answer' not in line or regen_answer:
            model_answer = line['response'].strip()
            for c in 'ABCDE':
                if model_answer.endswith(f" {c}.") or model_answer.endswith(f" ({c}).") or model_answer.startswith(f"{c}\n") or model_answer.startswith(f"({c})\n") or model_answer.startswith(f"({c}) {c}\n"):
                    model_answer = c
            if is_number(model_answer.split('is ')[-1].rstrip('.')):
                model_answer = model_answer.split('is ')[-1].rstrip('.')
            if 'oxed{' not in model_answer:
                for flag in ['the final answer is', 'the answer is', 'the correct answer is', 'the answer should be']:
                    raw_model_answer = model_answer
                    model_answer = model_answer.split(flag)[-1].strip()
                    if flag in raw_model_answer:
                        model_answer = model_answer.split('\n')[0].split('. ')[0]
                    flag = flag.replace('the', 'The')
                    raw_model_answer = model_answer
                    model_answer = model_answer.split(flag)[-1].strip()
                    if flag in raw_model_answer:
                        model_answer = model_answer.split('\n')[0].split('. ')[0]
            elif model_answer.count('oxed{') > 1:
                model_answer = '\\boxed{' + model_answer.split('oxed{')[-1]
                
            model_answer = find_math_answer(model_answer).replace('(a)', 'a').replace('(b)', 'b').replace('(c)', 'c').replace('(d)', 'd').replace('(e)', 'e').replace('{a}', 'a').replace('{b}', 'b').replace('{c}', 'c').replace('{d}', 'd').replace('{e}', 'e').rstrip('.').lstrip(':').strip()
            line['model_answer'] = model_answer
        else:
            model_answer = line['model_answer']
        line['correct'] = is_equal(gt_answer, model_answer) or is_equal(gt_answer_value, model_answer)
    save_jsonl(answer_file, lines, t_stamp=False)
