import pandas as pd
import numpy as np
from Character import Character
import shutil
from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.utils.dataframe import dataframe_to_rows

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
fort_smallest = df['Score_f'].nsmallest(3)
tyr_smallest = df['Score_t'].nsmallest(3)
fort_need = pd.DataFrame({'Fortified Need': fort_smallest.index, ' ': np.nan, '  ': np.nan, 'Tyrannical Need': tyr_smallest.index})

workbook=Workbook()

worksheet = workbook.active
worksheet.column_dimensions['A'].width = 30
worksheet.column_dimensions['D'].width = 30

worksheet['A4'] = char.name +' '+' '+' '+str(char.current_score)

timezone = 'US/Eastern'  # change this to your local timezone
worksheet['D4'] = pd.Timestamp.now(tz=timezone).strftime('%m/%d/%Y %I:%M %p')


worksheet.append([])
worksheet.append([])

for r in dataframe_to_rows(df, index=True, header=True):
    worksheet.append(r)

worksheet.append([])

for s in dataframe_to_rows(fort_need, index=False, header=True):
    worksheet.append(s)

for cell in worksheet[18]:
    cell.font = Font(bold=True)

workbook.save('dungeon.xlsx')

shutil.copy2('dungeon.xlsx', '/mnt/c/Users/galen/Desktop/dungeon.xlsx')
