
import math
from Character import Character

scores = {
    '+2': 40,
    '+3': 45,
    '+4': 50,
    '+5': 55,
    '+6': 60,
    '+7': 75,
    '+8': 80,
    '+9': 85,
    '+10': 90,
    '+11': 97,
    '+12': 104,
    '+13': 111,
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


#This will give you the closest key for a given score
def one_key(diff_score, usr_score, score_dict):
    new_diff = diff_score + usr_score
    if new_diff > 240:
        return int('+30')
    closest_score = None
    closest_distance = float('inf')
    for key in score_dict:
        distance = score_dict[key] - new_diff
        if distance > 0 and distance < closest_distance:
            closest_score = key
            closest_distance = distance
    return int(closest_score)

#Gives you the difference between your current score and your goal
def score_difference(goal_score, user_score):
    diff = goal_score - user_score
    return diff

#Creates a dictionary of dungeons and thier respective keys and scores for fortified weeks
def assign_f_dict(index, fort_array):
    f_dict = {}
    for i in range(len(index)):
        f_dict[index[i]] = fort_array[i]
    return f_dict

#Creates a dictionary of dungeons and their respective keys and scores for tyrannical weeks
def assign_t_dict(index, tyr_array):
    t_dict = {}
    for i in range(len(index)):
        t_dict[index[i]] = tyr_array[i]
    return t_dict

#Returns the dungeon and key needed to hit a target score
def score_calculator_one(char, dict):
    one_score_dict={}
    if char.current_score < 750:
        diff = score_difference(750, char.current_score)
        index = None
        m_key = 35
        for test_key in dict:
            score_comp = dict[test_key][1]
            new_key = one_key(diff, score_comp, scores)
            if not isinstance(new_key, int) :
                return new_key
            elif new_key < m_key:
                m_key = new_key
                index = test_key
        one_score_dict[index] = m_key
        return one_score_dict

    elif 750 <= char.current_score < 1500:
        diff = score_difference(1500, char.current_score)
        index = None
        m_key = 35
        for test_key in dict:
            score_comp = dict[test_key][1]
            new_key = one_key(diff, score_comp, scores)
            if not isinstance(new_key, int) :
                return new_key
            elif new_key < m_key:
                m_key = new_key
                index = test_key
        one_score_dict[index] = m_key
        return one_score_dict

    elif 1500 <= char.current_score < 2000:
        diff = score_difference(2000, char.current_score)
        index = None
        m_key = 35
        for test_key in dict:
            score_comp = dict[test_key][1]
            new_key = one_key(diff, score_comp, scores)
            if not isinstance(new_key, int) :
                return new_key
            elif new_key < m_key:
                m_key = new_key
                index = test_key
        one_score_dict[index] = m_key
        return one_score_dict

    elif 2000 <= char.current_score < 2500:
        diff = score_difference(2500, char.current_score)
        index = None
        m_key = 35
        for test_key in dict:
            score_comp = dict[test_key][1]
            new_key = one_key(diff, score_comp, scores)
            if not isinstance(new_key, int) :
                return new_key
            elif new_key < m_key:
                m_key = new_key
                index = test_key
        one_score_dict[index] = m_key
        return one_score_dict

    elif 2500 <= char.current_score < 2800:
        diff = score_difference(2800, char.current_score)
        index = None
        m_key = 35
        for test_key in dict:
            score_comp = dict[test_key][1]
            new_key = one_key(diff, score_comp, scores)
            if not isinstance(new_key, int) :
                return new_key
            elif new_key < m_key:
                m_key = new_key
                index = test_key
        one_score_dict[index] = m_key
        return one_score_dict

    else:
        diff = score_difference(3000, char.current_score)
        index = None
        m_key = 35
        for test_key in dict:
            score_comp = dict[test_key][1]
            new_key = one_key(diff, score_comp, scores)
            if not isinstance(new_key, int) :
                return new_key
            elif new_key < m_key:
                m_key = new_key
                index = test_key
        one_score_dict[index] = m_key
        return one_score_dict


#Returns three dungeons that you need to hit a target score
def score_calculator_three(char, dict):
    three_score_dict={}
    used_keys = set()
    if char.current_score < 750:
        diff = math.ceil((score_difference(750, char.current_score)) / 3)
        while len(three_score_dict) < 3:
            index = None
            m_key = float('inf')
            for test_key in dict:
                    if test_key in used_keys:
                        continue
                    score_comp = dict[test_key][1]
                    new_key = one_key(diff, score_comp, scores)
                    if not isinstance(new_key, int) :
                        return new_key
                    elif new_key < m_key:
                        m_key = new_key
                        index = test_key
            three_score_dict[index] = m_key
            used_keys.add(index)
        return three_score_dict

    elif 750 <= char.current_score < 1500:
        diff = math.ceil((score_difference(1500, char.current_score)) / 3)
        while len(three_score_dict) < 3:
            index = None
            m_key = float('inf')
            for test_key in dict:
                    if test_key in used_keys:
                        continue
                    score_comp = dict[test_key][1]
                    new_key = one_key(diff, score_comp, scores)
                    if not isinstance(new_key, int) :
                        return new_key
                    elif new_key < m_key:
                        m_key = new_key
                        index = test_key
            three_score_dict[index] = m_key
            used_keys.add(index)
        return three_score_dict

    elif 1500 <= char.current_score < 2000:
        diff = math.ceil((score_difference(2000, char.current_score)) / 3)
        while len(three_score_dict) < 3:
            index = None
            m_key = float('inf')
            for test_key in dict:
                    if test_key in used_keys:
                        continue
                    score_comp = dict[test_key][1]
                    new_key = one_key(diff, score_comp, scores)
                    if not isinstance(new_key, int) :
                        return new_key
                    elif new_key < m_key:
                        m_key = new_key
                        index = test_key
            three_score_dict[index] = m_key
            used_keys.add(index)
        return three_score_dict
    elif 2000 <= char.current_score < 2500:
        diff = math.ceil((score_difference(2500, char.current_score)) / 3)
        while len(three_score_dict) < 3:
            index = None
            m_key = float('inf')
            for test_key in dict:
                    if test_key in used_keys:
                        continue
                    score_comp = dict[test_key][1]
                    new_key = one_key(diff, score_comp, scores)
                    if not isinstance(new_key, int) :
                        return new_key
                    elif new_key < m_key:
                        m_key = new_key
                        index = test_key
            three_score_dict[index] = m_key
            used_keys.add(index)
        return three_score_dict
    elif 2500 <= char.current_score < 2800:
        diff = math.ceil((score_difference(2800, char.current_score)) / 3)
        while len(three_score_dict) < 3:
            index = None
            m_key = float('inf')
            for test_key in dict:
                    if test_key in used_keys:
                        continue
                    score_comp = dict[test_key][1]
                    new_key = one_key(diff, score_comp, scores)
                    if not isinstance(new_key, int) :
                        return new_key
                    elif new_key < m_key:
                        m_key = new_key
                        index = test_key
            three_score_dict[index] = m_key
            used_keys.add(index)
        return three_score_dict
    
    else:
        diff = math.ceil((score_difference(3000, char.current_score)) / 3)
        while len(three_score_dict) < 3:
            index = None
            m_key = float('inf')
            for test_key in dict:
                    if test_key in used_keys:
                        continue
                    score_comp = dict[test_key][1]
                    new_key = one_key(diff, score_comp, scores)
                    if not isinstance(new_key, int) :
                        return new_key
                    elif new_key < m_key:
                        m_key = new_key
                        index = test_key
            three_score_dict[index] = m_key
            used_keys.add(index)
        return three_score_dict

if __name__ == '__main__':
    char = Character('maddusmaxxus', 'dalaran')

    char.get_char_object()
    char.set_current_score()
    char.set_BH_scores()
    char.set_HOI_scores()
    char.set_NELT_scores()
    char.set_ULD_scores()
    char.set_FH_scores()
    char.set_NL_scores()
    char.set_UNDR_scores()
    char.set_VP_scores()

    fort = [char.BH_f, char.HOI_f, char.NELT_f, char.ULD_f, char.FH_f, char.NL_f, char.UNDR_f, char.VP_f]
    tyr = [char.BH_t, char.HOI_t, char.NELT_t, char.ULD_t, char.FH_t, char.NL_t, char.UNDR_t, char.VP_t]

    index = ['Brackenhide Hold', 'Halls of Infusion', 'Neltharus', 'Uldaman: Legacy of Tyr',
            'Freehold', 'Neltharion\'s Lair', 'The Underrot', 'The Vortex Pinnacle']

    
    f_dict = assign_f_dict(index, fort)
    t_dict = assign_t_dict(index, tyr)
    # print(score_calculator_one_f(char, f_dict))
    print(score_calculator_three(char, t_dict))