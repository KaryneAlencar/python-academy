def nota_quizzes(q1, q2, q3, q4, q5):
    if (q1 < 0) or (q1 > 10):
        return 0
    if (q2 < 0) or (q2 > 10):
        return 0
    if (q3 < 0) or (q3 > 10):
        return 0
    if (q4 < 0) or (q4 > 10):
        return 0
    if (q5 < 0) or (q5 > 10):
        return 0
    if (q1 <= q2) and (q1 <= q3) and (q1 <= q4) and (q1 <= q5):
        media = (q2 + q3 + q4 + q5) / 4
        return media
    elif (q2 <= q1) and (q2 <= q3) and (q2 <= q4) and (q2 <= q5):
        media = (q1 + q3 + q4 + q5) / 4
        return media
    elif (q3 <= q1) and (q3 <= q2) and (q3 <= q4) and (q3 <= q5):
        media = (q1 + q2 + q4 + q5) / 4
        return media
    elif (q4 <= q1) and (q4 <= q2) and (q4 <= q3) and (q4 <= q5):
        media = (q1 + q2 + q3 + q5) / 4
        return media
    elif (q5 <= q1) and (q5 <= q2) and (q5 <= q3) and (q5 <= q4):
        media = (q1 + q2 + q3 + q4) / 4
        return media