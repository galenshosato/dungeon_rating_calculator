import requests
import json


class Character:
    def __init__(self, name, realm):
        self.name = name
        self.realm = realm
        self.char_object = None
        self.current_score = None
        self.COS_f = None
        self.COS_t = None
        self.SBG_f = None
        self.SBG_t = None
        self.HOV_f = None
        self.HOV_t = None
        self.TJS_f = None
        self.TJS_t = None
        self.AV_f = None
        self.AV_t = None
        self.AA_f = None
        self.AA_t = None
        self.NO_f = None
        self.NO_t = None
        self.RLP_f = None
        self.RLP_t = None

    def get_char_object(self):
        score_response = requests.get('http://localhost:3000/test')
        char_object = json.loads(score_response.text)
        self.char_object = char_object
        return self.char_object
    
    def set_current_score(self):
        current_score = self.char_object['mythic_plus_scores_by_season'][0]['scores']['all']
        self.current_score = current_score
        return self.current_score
    
    def set_COS_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "COS":
                affixes = d["affixes"]
                dungeon_score = d['score']
                if affixes[0]['name'] == "Fortified":
                    self.COS_f = dungeon_score
                else:
                    self.COS_t = dungeon_score
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "COS":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.COS_f = alt_dungeon_score
                else:
                    self.COS_t = alt_dungeon_score
        return  self.COS_f, self.COS_t
    
    def set_SBG_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "SBG":
                affixes = d["affixes"]
                dungeon_score = d['score']
                if affixes[0]['name'] == "Fortified":
                    self.SBG_f = dungeon_score
                else:
                    self.SBG_t = dungeon_score
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "SBG":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.SBG_f = alt_dungeon_score
                else:
                    self.SBG_t = alt_dungeon_score
        return  self.SBG_f, self.SBG_t
    
    def set_HOV_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "HOV":
                affixes = d["affixes"]
                dungeon_score = d['score']
                if affixes[0]['name'] == "Fortified":
                    self.HOV_f = dungeon_score
                else:
                    self.HOV_t = dungeon_score
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "HOV":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.HOV_f = alt_dungeon_score
                else:
                    self.HOV_t = alt_dungeon_score
        return  self.HOV_f, self.HOV_t
    
    def set_TJS_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "TJS":
                affixes = d["affixes"]
                dungeon_score = d['score']
                if affixes[0]['name'] == "Fortified":
                    self.TJS_f = dungeon_score
                else:
                    self.TJS_t = dungeon_score
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "TJS":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.TJS_f = alt_dungeon_score
                else:
                    self.TJS_t = alt_dungeon_score
        return  self.TJS_f, self.TJS_t
    
    def set_AV_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "AV":
                affixes = d["affixes"]
                dungeon_score = d['score']
                if affixes[0]['name'] == "Fortified":
                    self.AV_f = dungeon_score
                else:
                    self.AV_t = dungeon_score
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "AV":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.AV_f = alt_dungeon_score
                else:
                    self.AV_t = alt_dungeon_score
        return  self.AV_f, self.AV_t
    
    def set_AA_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "AA":
                affixes = d["affixes"]
                dungeon_score = d['score']
                if affixes[0]['name'] == "Fortified":
                    self.AA_f = dungeon_score
                else:
                    self.AA_t = dungeon_score
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "AA":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.AA_f = alt_dungeon_score
                else:
                    self.AA_t = alt_dungeon_score
        return  self.AA_f, self.AA_t
    
    def set_NO_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "NO":
                affixes = d["affixes"]
                dungeon_score = d['score']
                if affixes[0]['name'] == "Fortified":
                    self.NO_f = dungeon_score
                else:
                    self.NO_t = dungeon_score
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "NO":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.NO_f = alt_dungeon_score
                else:
                    self.NO_t = alt_dungeon_score
        return  self.NO_f, self.NO_t
    
    def set_RLP_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "RLP":
                affixes = d["affixes"]
                dungeon_score = d['score']
                if affixes[0]['name'] == "Fortified":
                    self.RLP_f = dungeon_score
                else:
                    self.RLP_t = dungeon_score
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "RLP":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.RLP_f = alt_dungeon_score
                else:
                    self.RLP_t = alt_dungeon_score
        return  self.RLP_f, self.RLP_t
    

                    




        
    


if __name__ == '__main__':
    max = Character('lilmadman', 'dalaran')
    max.get_char_object()
    print(max.set_COS_scores())
    print(max.set_SBG_scores())
    print(max.set_HOV_scores())