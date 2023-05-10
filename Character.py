import requests
import json


class Character:
    def __init__(self, name, realm):
        self.name = name
        self.realm = realm
        self.char_object = None
        self.current_score = None
        self.BH_f = [0,0]
        self.BH_t = [0,0]
        self.HOI_f = [0,0]
        self.HOI_t = [0,0]
        self.NELT_f = [0,0]
        self.NELT_t = [0,0]
        self.ULD_f = [0,0]
        self.ULD_t = [0,0]
        self.FH_f = [0,0]
        self.FH_t = [0,0]
        self.NL_f = [0,0]
        self.NL_t = [0,0]
        self.UNDR_f = [0,0]
        self.UNDR_t = [0,0]
        self.VP_f = [0,0]
        self.VP_t = [0,0]

    def get_char_object(self):
        # score_response = requests.get('http://localhost:3000/test')
        score_response = requests.get(f'https://raider.io/api/v1/characters/profile?region=us&realm={self.realm}&name={self.name}&fields=mythic_plus_scores_by_season%3Acurrent%2Cmythic_plus_best_runs%3Aall%2Cmythic_plus_alternate_runs%3Aall')
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
                    self.BH_f = [best_level, dungeon_score]
                else:
                    self.BH_t = [best_level, dungeon_score]
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "BH":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                alt_level = alt["mythic_level"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.BH_f = [alt_level, alt_dungeon_score]
                else:
                    self.BH_t = [alt_level, alt_dungeon_score]
        return  self.BH_f, self.BH_t
    
    def set_HOI_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "HOI":
                affixes = d["affixes"]
                dungeon_score = d['score']
                best_level=d["mythic_level"]
                if affixes[0]['name'] == "Fortified":
                    self.HOI_f = [best_level, dungeon_score]
                else:
                    self.HOI_t = [best_level,dungeon_score]
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "HOI":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                alt_level = alt["mythic_level"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.HOI_f = [alt_level, alt_dungeon_score]
                else:
                    self.HOI_t = [alt_level, alt_dungeon_score]
        return  self.HOI_f, self.HOI_t
    
    def set_NELT_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "NELT":
                affixes = d["affixes"]
                dungeon_score = d['score']
                best_level=d["mythic_level"]
                if affixes[0]['name'] == "Fortified":
                    self.NELT_f = [best_level, dungeon_score]
                else:
                    self.NELT_t = [best_level,dungeon_score]
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "NELT":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                alt_level = alt["mythic_level"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.NELT_f = [alt_level, alt_dungeon_score]
                else:
                    self.NELT_t = [alt_level, alt_dungeon_score]
        return  self.NELT_f, self.NELT_t
    
    def set_ULD_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "ULD":
                affixes = d["affixes"]
                dungeon_score = d['score']
                best_level=d["mythic_level"]
                if affixes[0]['name'] == "Fortified":
                    self.ULD_f = [best_level, dungeon_score]
                else:
                    self.ULD_t = [best_level,dungeon_score]
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "ULD":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                alt_level = alt["mythic_level"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.ULD_f = [alt_level, alt_dungeon_score]
                else:
                    self.ULD_t = [alt_level, alt_dungeon_score]
        return  self.ULD_f, self.ULD_t
    
    def set_FH_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "FH":
                affixes = d["affixes"]
                dungeon_score = d['score']
                best_level=d["mythic_level"]
                if affixes[0]['name'] == "Fortified":
                    self.FH_f = [best_level, dungeon_score]
                else:
                    self.FH_t = [best_level,dungeon_score]
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "FH":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                alt_level = alt["mythic_level"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.FH_f = [alt_level, alt_dungeon_score]
                else:
                    self.FH_t = [alt_level, alt_dungeon_score]
        return  self.FH_f, self.FH_t
    
    def set_NL_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "NL":
                affixes = d["affixes"]
                dungeon_score = d['score']
                best_level=d["mythic_level"]
                if affixes[0]['name'] == "Fortified":
                    self.NL_f = [best_level, dungeon_score]
                else:
                    self.NL_t = [best_level,dungeon_score]
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "NL":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                alt_level = alt["mythic_level"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.NL_f = [alt_level, alt_dungeon_score]
                else:
                    self.NL_t = [alt_level, alt_dungeon_score]
        return  self.NL_f, self.NL_t
    
    def set_UNDR_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "UNDR":
                affixes = d["affixes"]
                dungeon_score = d['score']
                best_level=d["mythic_level"]
                if affixes[0]['name'] == "Fortified":
                    self.UNDR_f = [best_level, dungeon_score]
                else:
                    self.UNDR_t = [best_level,dungeon_score]
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "UNDR":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                alt_level = alt["mythic_level"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.UNDR_f = [alt_level, alt_dungeon_score]
                else:
                    self.UNDR_t = [alt_level, alt_dungeon_score]
        return  self.UNDR_f, self.UNDR_t
    
    def set_VP_scores(self):
        for d in self.char_object['mythic_plus_best_runs']:
            if d["short_name"] == "VP":
                affixes = d["affixes"]
                dungeon_score = d['score']
                best_level=d["mythic_level"]
                if affixes[0]['name'] == "Fortified":
                    self.VP_f = [best_level, dungeon_score]
                else:
                    self.VP_t = [best_level,dungeon_score]
        for alt in self.char_object['mythic_plus_alternate_runs']:
            if alt["short_name"] == "VP":
                alt_affixes = alt["affixes"]
                alt_dungeon_score = alt["score"]
                alt_level = alt["mythic_level"]
                if alt_affixes[0]['name'] == "Fortified":
                    self.VP_f = [alt_level, alt_dungeon_score]
                else:
                    self.VP_t = [alt_level, alt_dungeon_score]
        return  self.VP_f, self.VP_t
    

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

    print(char.FH_f)