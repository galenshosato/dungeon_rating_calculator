import requests
import json


class Character:
    def __init__(self, name, realm):
        self.name = name
        self.realm = realm
        self.char_object = None
        self.current_score = None
        self.BH_f = []
        self.BH_t = []
        self.HOI_f = []
        self.HOI_t = []
        self.NELT_f = []
        self.NELT_t = []
        self.ULD_f = []
        self.ULD_t = []
        self.FH_f = []
        self.FH_t = []
        self.NL_f = []
        self.NL_t = []
        self.UNDR_f = []
        self.UNDR_t = []
        self.VP_f = []
        self.VP_t = []

    def get_char_object(self):
        score_response = requests.get('http://localhost:3000/test')
        # score_response = requests.get(f'https://raider.io/api/v1/characters/profile?region=us&realm={self.realm}&name={self.name}&fields=mythic_plus_scores_by_season%3Aprevious%2Cmythic_plus_best_runs%3Aall%2Cmythic_plus_alternate_runs%3Aall')
        char_object = json.loads(score_response.text)
        self.char_object = char_object
        return self.char_object
    
    def set_current_score(self):
        current_score = self.char_object['mythic_plus_scores_by_season'][0]['scores']['all']
        self.current_score = current_score
        return self.current_score
    
    def set_BH_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "BH":
                affixes = d["affixes"]
                dungeon_score = d['score']
                best_level= d["mythic_level"]
                if affixes[0]['name'] == "Fortified":
                    self.BH_f.append(best_level)
                    self.BH_f.append(dungeon_score)
                else:
                    self.BH_t.append(best_level)
                    self.BH_t.append(dungeon_score)
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "BH":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                alt_level = alt["mythic_level"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.BH_f.append(alt_level)
                    self.BH_f.append(alt_dungeon_score)
                else:
                    self.BH_t.append(alt_level)
                    self.BH_t.append(alt_dungeon_score)
        return  self.BH_f, self.BH_t
    
    def set_HOI_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "HOI":
                affixes = d["affixes"]
                dungeon_score = d['score']
                best_level=d["mythic_level"]
                if affixes[0]['name'] == "Fortified":
                    self.HOI_f.append(best_level)
                    self.HOI_f.append(dungeon_score)
                else:
                    self.HOI_t.append(best_level)
                    self.HOI_t.append(dungeon_score)
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "HOI":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                alt_level = alt["mythic_level"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.HOI_f.append(alt_level)
                    self.HOI_f.append(alt_dungeon_score)
                else:
                    self.HOI_t.append(alt_level)
                    self.HOI_t.append(alt_dungeon_score)
        return  self.HOI_f, self.HOI_t
    
    def set_NELT_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "NELT":
                affixes = d["affixes"]
                dungeon_score = d['score']
                best_level=d["mythic_level"]
                if affixes[0]['name'] == "Fortified":
                    self.NELT_f.append(best_level)
                    self.NELT_f.append(dungeon_score)
                else:
                    self.NELT_t.append(best_level)
                    self.NELT_t.append(dungeon_score)
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "NELT":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                alt_level = alt["mythic_level"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.NELT_f.append(alt_level)
                    self.NELT_f.append(alt_dungeon_score)
                else:
                    self.NELT_t.append(alt_level)
                    self.NELT_t.append(alt_dungeon_score)
        return  self.NELT_f, self.NELT_t
    
    def set_ULD_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "ULD":
                affixes = d["affixes"]
                dungeon_score = d['score']
                best_level=d["mythic_level"]
                if affixes[0]['name'] == "Fortified":
                    self.ULD_f.append(best_level)
                    self.ULD_f.append(dungeon_score)
                else:
                    self.ULD_t.append(best_level)
                    self.ULD_t.append(dungeon_score)
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "ULD":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                alt_level = alt["mythic_level"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.ULD_f.append(alt_level)
                    self.ULD_f.append(alt_dungeon_score)
                else:
                    self.ULD_t.append(alt_level)
                    self.ULD_t.append(alt_dungeon_score)
        return  self.ULD_f, self.ULD_t
    
    def set_FH_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "FH":
                affixes = d["affixes"]
                dungeon_score = d['score']
                best_level=d["mythic_level"]
                if affixes[0]['name'] == "Fortified":
                    self.FH_f.append(best_level)
                    self.FH_f.append(dungeon_score)
                else:
                    self.FH_t.append(best_level)
                    self.FH_t.append(dungeon_score)
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "FH":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                alt_level = alt["mythic_level"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.FH_f.append(alt_level)
                    self.FH_f.append(alt_dungeon_score)
                else:
                    self.FH_t.append(alt_level)
                    self.FH_t.append(alt_dungeon_score)
        return  self.FH_f, self.FH_t
    
    def set_NL_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "NL":
                affixes = d["affixes"]
                dungeon_score = d['score']
                best_level=d["mythic_level"]
                if affixes[0]['name'] == "Fortified":
                    self.NL_f.append(best_level)
                    self.NL_f.append(dungeon_score)
                else:
                    self.NL_t.append(best_level)
                    self.NL_t.append(dungeon_score)
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "NL":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                alt_level = alt["mythic_level"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.NL_f.append(alt_level)
                    self.NL_f.append(alt_dungeon_score)
                else:
                    self.NL_t.append(alt_level)
                    self.NL_t.append(alt_dungeon_score)
        return  self.NL_f, self.NL_t
    
    def set_UNDR_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "UNDR":
                affixes = d["affixes"]
                dungeon_score = d['score']
                best_level=d["mythic_level"]
                if affixes[0]['name'] == "Fortified":
                    self.UNDR_f.append(best_level)
                    self.UNDR_f.append(dungeon_score)
                else:
                    self.UNDR_t.append(best_level)
                    self.UNDR_t.append(dungeon_score)
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "UNDR":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                alt_level = alt["mythic_level"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.UNDR_f.append(alt_level)
                    self.UNDR_f.append(alt_dungeon_score)
                else:
                    self.UNDR_t.append(alt_level)
                    self.UNDR_t.append(alt_dungeon_score)
        return  self.UNDR_f, self.UNDR_t
    
    def set_VP_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "VP":
                affixes = d["affixes"]
                dungeon_score = d['score']
                best_level=d["mythic_level"]
                if affixes[0]['name'] == "Fortified":
                    self.VP_f.append(best_level)
                    self.VP_f.append(dungeon_score)
                else:
                    self.VP_t.append(best_level)
                    self.VP_t.append(dungeon_score)
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "VP":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                alt_level = alt["mythic_level"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.VP_f.append(alt_level)
                    self.VP_f.append(alt_dungeon_score)
                else:
                    self.VP_t.append(alt_level)
                    self.VP_t.append(alt_dungeon_score)
        return  self.VP_f, self.VP_t
    

