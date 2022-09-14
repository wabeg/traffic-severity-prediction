import pandas as pd
import numpy as np
import re

# regex for splitting weather condition entries
re_wc_split = re.compile('\sand\s|\swith\s|\s\/\s')

# wc_words to search for per category
# these are chosen arbitrarily based on examination of unique values
wc_words = {
    'rain': ['rain', 'drizzle', 'precipitation', 'mist'],
    'snow': ['snow', 'wint'],
    'ice': ['hail', 'freez', 'sleet'],
    'wind': ['wind', 'squall'],
    'clouds': ['cloud', 'overcast'],
    'thunder': ['t-storm', 'thunder'],
    'fog': ['fog', 'haze'],
    'fair': ['fair', 'clear'],
    'tornado': ['tornado', 'funnel'],
    'dust': ['sand', 'dust', 'smoke'],
    'other': []
}

# column order
wc_col_names = sorted(wc_words.keys())

# function to split weather condition series into rows per condition
# pass df['weather_condition'] list to split
def split_weather_condition(wc_series, empty=np.nan):
    # supporting function to get a column for a single wc category
    def get_wc_entries(colname, wc_list):
        global wc_words
        nonlocal empty
        keywords = wc_words[colname]
        entry = ''
        for wc in wc_list:
            for keyword in keywords:
                if keyword in wc:
                    if entry: entry += ' / '
                    entry += wc

        if not entry: return empty

        return entry

    # make all items lowercase
    wc_series = [t.lower() if type(t) == str else t for t in wc_series]

    # NOTE n/a precipitation is a category

    rows = list()
    for wc in wc_series:
        # for each weather condition row...
        # split on delimiting words ('/','and','with')
        if type(wc) != str:
            # is nan
            rows.append([''])
        else:
            rows.append(re.split(re_wc_split, wc))

    wc_dict = {k: list() for k in wc_col_names}

    # get each row and add to wc_dict
    for row in rows:
        for col in wc_dict:
            wc_dict[col].append(get_wc_entries(col, row))

    return wc_dict
