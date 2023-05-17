import pandas as pd
import numpy as np
import sys
from Character import Character
import shutil
from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.utils.dataframe import dataframe_to_rows
from functions import assign_f_dict, assign_t_dict, score_calculator_one, score_calculator_three

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
char_name = sys.argv[1]
char_realm = sys.argv[2]
char = Character(char_name, char_realm)

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

goal = 0

if char.current_score < 750:
    goal = 750
elif 750 <= char.current_score < 1500:
    goal = 1500
elif 1500 <= char.current_score < 2000:
    goal = 2000
elif 2000 <= char.current_score < 2500:
    goal = 2500
else:
    goal = 2800




col1= [key[0] for key in fort]
col2 = [score[1] for score in fort]
col3 = np.nan
col4 = [key[0] for key in tyr]
col5 = [score[1] for score in tyr]

data = {'Key_f': col1, 'Score_f': col2, ' ': col3, 'Key_t': col4, 'Score_t': col5}

df = pd.DataFrame(data, index=index)
fort_smallest = df['Score_f'].nsmallest(3)
tyr_smallest = df['Score_t'].nsmallest(3)
dung_need = pd.DataFrame({'Fortified Need': fort_smallest.index, ' ': np.nan, '  ': np.nan, 'Tyrannical Need': tyr_smallest.index})
f_dict = assign_f_dict(index, fort)
t_dict = assign_t_dict(index, tyr)

#Getting Data for fort keys
fort_one_dict = score_calculator_one(char, f_dict)
if fort_one_dict == {"Too High Of Key" : "31 or higher"}:
    fort_one_display = ['Too High of a Key, 31 or Higher']
else:
    fort_one_display = [f"{k}({v})" for k,v in fort_one_dict.items()]
fort_three_dict = score_calculator_three(char, f_dict)
if fort_three_dict == {"Too High Of Key" : "31 or higher"}:
    fort_three_display = ['Continuing to gather data...', 'Continuing to gather data...', 'Continuing to gather data...']
else:
    fort_three_display = [f"{k}({v})" for k,v in fort_three_dict.items()]
tyr_one_dict = score_calculator_one(char, t_dict)
if tyr_one_dict == {"Too High Of Key" : "31 or higher"}:
    tyr_one_display = ['Too High of a Key, 31 or Higher']
else:
    tyr_one_display = [f"{k}({v})" for k,v in tyr_one_dict.items()]
tyr_three_dict = score_calculator_three(char, t_dict)
if tyr_three_dict == {"Too High Of Key" : "31 or higher"}:
    tyr_three_display = ['Continuing to gather data...', 'Continuing to gather data...', 'Continuing to gather data...']
else:
    tyr_three_display = [f"{k}({v})" for k,v in tyr_three_dict.items()]


one_need = pd.DataFrame({f'Single Dungeon to reach {goal} -Fort': fort_one_display, ' ': np.nan, '  ': np.nan, f'Single Dungeon to reach {goal} -Tyr': tyr_one_display})
three_need = pd.DataFrame({f'Three Dungeons to reach {goal} -Fort': fort_three_display, ' ': np.nan, '  ': np.nan, f'Three Dungeons to reach {goal} -Tyr': tyr_three_display})







workbook=Workbook()

worksheet = workbook.active
worksheet.column_dimensions['A'].width = 35
worksheet.column_dimensions['D'].width = 35

worksheet['A4'] = char.name +' '+' '+' '+str(char.current_score)

timezone = 'US/Eastern'  # change this to your local timezone
worksheet['D4'] = pd.Timestamp.now(tz=timezone).strftime('%m/%d/%Y %I:%M %p')


worksheet.append([])
worksheet.append([])

for r in dataframe_to_rows(df, index=True, header=True):
    worksheet.append(r)

worksheet.append([])

for s in dataframe_to_rows(dung_need, index=False, header=True):
    worksheet.append(s)

worksheet.append([])

for t in dataframe_to_rows(one_need, index=False, header=True):
    worksheet.append(t)

worksheet.append([])

for u in dataframe_to_rows(three_need, index=False, header=True):
    worksheet.append(u)

for row_num in [18, 23, 26]:
    for cell in worksheet[row_num]:
        cell.font = Font(bold=True)

workbook.save('dungeon.xlsx')

shutil.copy2('dungeon.xlsx', '/mnt/c/Users/galen/Desktop/dungeon.xlsx')
