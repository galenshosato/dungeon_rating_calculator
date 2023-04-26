import requests
import json


class Character:
    def __init__(self, name, realm):
        self.name = name
        self.realm = realm
        self.current_score = None
        self.cos_f = None
        self.cos_t = None
        self.sbg_f = None
        self.sbg_t = None
        self.hov_f = None
        self.hov_t = None
        self.tjs_f = None
        self.tjs_t = None
        self.av_f = None
        self.av_t = None
        self.aa_f = None
        self.aa_t = None
        self.no_f = None
        self.no_t = None
        self.rlp_f = None
        self.rlp_t = None

    def get_current_score(self):
        score_response = requests.get('http://localhost:3000/test')
        char_object = json.loads(score_response.text)
        self.current_score = char_object['mythic_plus_scores_by_season'][0]['scores']['all']
        return self.current_score
    


if __name__ == '__main__':
    max = Character('lilmadman', 'dalaran')
    print(max.get_current_score())