def nota_final(quiz, ai, af, ep1, ep2, epf):
    if quiz > 10 or quiz < 0:
        return 0
    if ai > 10 or ai < 0:
        return 0
    if af > 10 or af < 0:
        return 0
    if ep1 > 10 or ep1 < 0:
        return 0
    if ep2 > 10 or ep2 < 0:
        return 0
    if epf > 10 or epf < 0:
        return 0
    ni = 0.4*ai + 0.5*af + 0.1*quiz
    ng = 0.1*ep1 + 0.2*ep2 + 0.7*epf
    if ni >= 5 and ng >= 5:
        nf = (ni + ng)/2
    else:
        if ni <= ng:
            nf = ni
        else:
            nf = ng
    return nf