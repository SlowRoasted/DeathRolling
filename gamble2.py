prev_probs_sum = 1
nums_to_calculate = 500
for n in range(2,nums_to_calculate + 1):
    curr_probs = 1 - float(n - 1) * (1 + prev_probs_sum) / (n * n - 1)
    print(f'For roll num {n}, K = {curr_probs * 100}%')
    prev_probs_sum += curr_probs