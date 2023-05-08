from Character import Character


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

def one_key(diff_score, usr_score, score_dict):
    new_diff = diff_score + usr_score
    closest_score = None
    closest_distance = float('inf')
    for key in score_dict:
        distance = score_dict[key] - new_diff
        if distance > 0 and distance < closest_distance:
            closest_score = key
            closest_distance = distance
    return int(closest_score)


def score_difference(goal_score, user_score):
    diff = goal_score - user_score
    return diff

def assign_f_dict(index, fort_array):
    f_dict = {}
    for i in range(len(index)):
        f_dict[index[i]] = fort_array[i]
    return f_dict









def score_calculator_f(char, f_dict):
    one_score_dict={}
    three_score_dict = {}
    if char.current_score < 750:
        diff = score_difference(750, char.current_score)
        pass
    elif 751 <= char.current_score < 1500:
        diff = score_difference(1500, char.current_score)
        pass
    elif 1501 <= char.current_score < 2000:
        diff = score_difference(2000, char.current_score)
        # index = None
        # key = 35
        # for test_key in f_dict:
        #     score_comp = f_dict[key][1]
        #     new_key = one_key(diff, score_comp, scores)
        #     if new_key < key:
        #         key = new_key
        #         index = test_key
        # score_dict[index] = key
        # return score_dict

    elif 2001 <= char.current_score < 2500:
        diff = score_difference(2500, char.current_score)
        pass
    else:
        diff = score_difference(2750, char.current_score)
        index = None
        m_key = 35
        for test_key in f_dict:
            score_comp = f_dict[test_key][1]
            new_key = one_key(diff, score_comp, scores)
            if new_key < m_key:
                m_key = new_key
                index = test_key
        one_score_dict[index] = m_key
        return one_score_dict



if __name__ == '__main__':
    char = Character('lilmadman', 'dalaran')

    char.get_char_object()
    char.set_current_score()
    char.set_COS_scores()
    char.set_HOV_scores()
    char.set_TJS_scores()
    char.set_SBG_scores()
    char.set_RLP_scores()
    char.set_AA_scores()
    char.set_AV_scores()
    char.set_NO_scores()

    fort = [char.COS_f, char.HOV_f, char.TJS_f, char.SBG_f, char.RLP_f, char.AA_f, char.AV_f, char.NO_f]
    tyr = [char.COS_t, char.HOV_t, char.TJS_t, char.SBG_t, char.RLP_t, char.AA_t, char.AV_t, char.NO_t]

    index = ['Court of Stars', 'Halls of Valor', 'Temple of the Jade Serpent', 'Shadowmoon Burial Ground',
            'Ruby Life Pools', 'Alegthar Academy', 'Azure Vault', 'Nokund Offensive']

    f_dict= assign_f_dict(index, fort)
    print(score_calculator_f(char, f_dict))