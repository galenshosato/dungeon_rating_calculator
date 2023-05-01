import pandas as pd
import numpy as np
from Character import Character

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

col1= [key[0] for key in fort]
col2 = [score[1] for score in fort]
col3 = np.nan
col4 = [key[0] for key in tyr]
col5 = [score[1] for score in tyr]

data = {'Key_f': col1, 'Score_f': col2, ' ': col3, 'Key_t': col4, 'Score_t': col5}

df = pd.DataFrame(data, index=index)

df.to_excel('output.xlsx')


