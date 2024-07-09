seq_longa = 0
num_com_seq_longa = 0
n = 1
while n <= 1000:
    i = n
    seq_at = 0
    while i >= 1:
        if i % 2 == 0:
            i = i//2
            seq_at += 1
            if i == 1:
                break
        if i % 2 != 0:
            i = 3*i +1
            seq_at += 1
            if i == 1:
                break
    if seq_at > seq_longa:
        seq_longa = seq_at
        num_com_seq_longa = n
        seq_at = 0
    else:
        seq_at = 0
    n += 1
print(num_com_seq_longa)