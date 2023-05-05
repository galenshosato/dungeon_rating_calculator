
scores = {
    '+2': 40,
    '+3': 45,
    '+4': 55,
    '+5': 60,
    '+6': 65,
    '+7': 75,
    '+8': 80,
    '+9': 85,
    '+10': 100,
    '+11': 107,
    '+12': 114,
    '+13': 121,
    '+14': 128,
    '+15': 135,
    '+16': 142,
    '+17': 149,
    '+18': 156,
    '+19': 163,
    '+20': 170,
    '+21': 177,
    '+22': 184,
    '+23': 191,
    '+24': 198,
    '+25': 205,
    '+26': 212,
    '+27': 219,
    '+28': 226,
    '+29': 233,
    '+30': 240 
}

def one_key(core_score, usr_score):
    closest_key = min(scores, key=lambda x: abs(scores[x] - score))
    return closest_key









def score_calculator(score):
    if score < 750:
        pass
    elif 751 <= score < 1500:
        pass
    elif 1501 <= score < 2000:
        pass
    elif 2001 <= score < 2500:
        pass
    else:
        pass



if __name__ == '__main__':
    print(one_key())