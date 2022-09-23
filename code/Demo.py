import pickle
import pandas as pd
import numpy as np
filenamexgb = '../models/xgb.sav'
XGB_mod = pickle.load(open(filenamexgb, 'rb'))
filenamemin = '../models/min_max.sav'
min_max = pickle.load(open(filenamemin, 'rb'))
def live():
    lis = [0]*129
    lis[0] = float(input("Temp(F): "))
    lis[1] = float(input('Humidity(%): '))
    lis[2] = float(input('Pressure(in.): '))
    lis[3] = float(input('Visibility(mi.): '))
    lis[4] = float(input('Wind_Speed(mph): '))
    lis[5] = float(input('Precipitation(in.): '))
    #lis[6] = int(input('Presence of Amenity (0:no, 1:yes): '))
    #lis[7] = int(input('Presence of Bump (0:no, 1:yes): '))
    lis[8] = int(input('Presence of Crossing (0:no, 1:yes): '))
    #lis[9] = int(input('Presence of Give_Way (0:no, 1:yes): '))
    lis[10] = int(input('Presence of Junction (0:no, 1:yes): '))
    #lis[11] = int(input('Presence of No_Exit (0:no, 1:yes): '))
    #lis[12] = int(input('Presence of Railway (0:no, 1:yes): '))
    #lis[13] = int(input('Presence of Roundabout (0:no, 1:yes): '))
    #lis[14] = int(input('Presence of Station (0:no, 1:yes): '))
    lis[15] = int(input('Presence of Stop (0:no, 1:yes): '))
    #lis[16] = int(input('Presence of Traffic_Calming (0:no, 1:yes): '))
    #lis[17] = int(input('Presence of Traffic_Signal (0:no, 1:yes): '))
    lis[18] = int(input('0:Day, 1:Night: '))
    
    wc = int(input('Weather Condition: 1 for cloudy, 2 for dusty, 3 for fair, 4 for fog, 5 for ice, 6 for rain, 7 for snow, 8 for thunder, 9 for wind: '))
    if wc ==1: 
        lis[19] = 1
    elif wc ==2:
        lis[20] = 1
    elif wc==3:
        lis[21] = 1
    elif wc==4:
        lis[22] = 1
    elif wc==5:
        lis[23] = 1
    elif wc==6:
        lis[24] = 1
    elif wc==7:
        lis[25] = 1
    elif wc==8:
        lis[26] = 1
    elif wc==9:
        lis[27] = 1
    else:
        print('Invalid input')
    state = input('State Abbr.: ')
    if state == 'AL':
        lis[32] = 1
    elif state == 'AR':
        lis[33] = 1
    elif state == 'AZ':
        lis[34] = 1
    elif state == 'CA':
        lis[35] = 1
    elif state == 'CO':
        lis[36] = 1
    elif state == 'CT':
        lis[37] = 1
    elif state == 'DC':
        lis[38] = 1
    elif state == 'DE':
        lis[39] = 1
    elif state == 'FL':
        lis[40] = 1
    elif state == 'GA':
        lis[41] = 1
    elif state == 'IA':
        lis[42] = 1
    elif state == 'ID':
        lis[43] = 1
    elif state == 'IL':
        lis[44] = 1
    elif state == 'IN':
        lis[45] = 1
    elif state == 'KS':
        lis[46] = 1
    elif state == 'KY':
        lis[47] = 1
    elif state == 'LA':
        lis[48] = 1
    elif state == 'MA':
        lis[49] = 1
    elif state == 'MD':
        lis[50] = 1
    elif state == 'ME':
        lis[51] = 1
    elif state == 'MI':
        lis[52] = 1
    elif state == 'MN':
        lis[53] = 1
    elif state == 'MO':
        lis[54] = 1
    elif state == 'MS':
        lis[55] = 1
    elif state == 'MT':
        lis[56] = 1
    elif state == 'NC':
        lis[57] = 1
    elif state == 'ND':
        lis[58] = 1
    elif state == 'NE':
        lis[59] = 1
    elif state == 'NH':
        lis[60] = 1
    elif state == 'NJ':
        lis[61] = 1
    elif state == 'NM':
        lis[62] = 1
    elif state == 'NV':
        lis[63] = 1
    elif state == 'NY':
        lis[64] = 1
    elif state == 'OH':
        lis[65] = 1
    elif state == 'OK':
        lis[66] = 1
    elif state == 'OR':
        lis[67] = 1
    elif state == 'PA':
        lis[68] = 1
    elif state == 'RI':
        lis[69] = 1
    elif state == 'SC':
        lis[70] = 1
    elif state == 'SD':
        lis[71] = 1
    elif state == 'TN':
        lis[72] = 1
    elif state == 'TX':
        lis[73] = 1
    elif state == 'UT':
        lis[74] = 1
    elif state == 'VA':
        lis[75] = 1
    elif state == 'VT':
        lis[76] = 1
    elif state == 'WA':
        lis[77] = 1
    elif state == 'WI':
        lis[78] = 1
    elif state == 'WV':
        lis[79] = 1
    elif state == 'WY':
        lis[80] = 1
    side = int(input('Side: 1 for L, 2 for R: '))
    if side == 1:
        lis[81] = 1
    elif side == 2:
        lis[82] = 1
    else:
        print('Invalid input')
    timezone = 4
    if timezone == 1:
        lis[83] = 1
    elif timezone == 2:
        lis[84] = 1
    elif timezone == 3:
        lis[85] = 1
    elif timezone == 4:
        lis[86] = 1
    else:
        print('Invalid input')
    year = 2021
    if year == 2016:
        lis[87] = 1
    elif year == 2017:
        lis[88] = 1
    elif year == 2018:
        lis[89] = 1
    elif year == 2019:
        lis[90] = 1
    elif year == 2020:
        lis[91] = 1
    elif year == 2021:
        lis[92] = 1
    else:
        print('Invalid input')
    month = int(input('Month: '))
    if month == 1:
        lis[93] = 1
    elif month == 2:
        lis[94] = 1
    elif month == 3:
        lis[95] = 1
    elif month == 4:
        lis[96] = 1
    elif month == 5:
        lis[97] = 1
    elif month == 6:
        lis[98] = 1
    elif month == 7:
        lis[99] = 1
    elif month == 8:
        lis[100] = 1
    elif month == 9:
        lis[101] = 1
    elif month == 10:
        lis[102] = 1
    elif month == 11:
        lis[103] = 1
    elif month == 12:
        lis[104] = 1
    else:
        print('Invalid input')
    hour = int(input('Hour: '))
    if hour == 0:
        lis[105] = 1
    elif hour == 1:
        lis[106] = 1
    elif hour == 2:
        lis[107] = 1
    elif hour == 3:
        lis[108] = 1
    elif hour == 4:
        lis[109] = 1
    elif hour == 5:
        lis[110] = 1
    elif hour == 6:
        lis[111] = 1
    elif hour == 7:
        lis[112] = 1
    elif hour == 8:
        lis[113] = 1
    elif hour == 9:
        lis[114] = 1
    elif hour == 10:
        lis[115] = 1
    elif hour == 11:
        lis[116] = 1
    elif hour == 12:
        lis[117] = 1
    elif hour == 13:
        lis[118] = 1
    elif hour == 14:
        lis[119] = 1
    elif hour == 15:
        lis[120] = 1
    elif hour == 16:
        lis[121] = 1
    elif hour == 17:
        lis[122] = 1
    elif hour == 18:
        lis[123] = 1
    elif hour == 19:
        lis[124] = 1
    elif hour == 20:
        lis[125] = 1
    elif hour == 21:
        lis[126] = 1
    elif hour == 22:
        lis[127] = 1
    elif hour == 23:
        lis[128] = 1
    else:
        print('Invalid input')
    lis = min_max.fit_transform(np.array(lis).reshape((1,-1)))
    pred = XGB_mod.predict_proba(lis)[0][1]
    if pred >= .05:
        print('Severe, Send Help!')
    else:
        print('Not Severe')
    
live()
