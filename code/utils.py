import pandas as pd
import numpy as np
import re

# words to search for per category
words = {
    'rain': ['rain', 'drizzle', 'precipitation', 'mist'],
    'snow': ['snow', 'wint'],
    'ice': ['hail', 'freez', 'sleet'],
    'wind': ['wind', 'squall'],
    'clouds': ['cloud', 'overcast'],
    'thunder': ['thunderstorm', 't-storm', 'thunder'],
    'fog': ['fog', 'haze'],
    'fair': ['fair', 'clear'],
    'tornado': ['tornado', 'funnel'],
    'dust': ['sand', 'dust', 'smoke']
}

# match 'and', '/', and 'with' as separators
re_wc_split = re.compile('\sand\s|\s/\s|\swith\s')

def split_weather_condition(df, colname='Weather_Condition'):
    global words

    # make all items lowercase
    df[colname] = [t.lower() if type(t) == str else t for t in df[colname]]

    # NOTE n/a precipitation is a category

    rows = list()
    for wc in df[colname]:
        # for each weather condition row in df...
        # split on '/' or 'and' if exists
        if type(wc) != str:
            # is nan
            rows.append(np.nan)
        else:
            rows.append(re.split(re_wc_split, wc))

    # newcols will keep all the data for the new dataframe
    newcols = dict()

    # didcol will keep data on whether we've touched a category already
    didcol = dict()

    # initialize both dicts
    for cat in words:
        newcols[cat] = list()
        didcol[cat] = False

    # quick function to reset didcol
    def reset_didcol():
        nonlocal didcol
        for k in didcol:
            didcol[k] = False

    # go through each row and separate into weather condition entries
    for row in rows:
        # for each row
        reset_didcol()
        for wc in row:
            # for each weather condition in the row
            for cat in words:
                if didcol[cat]:
                    # if we have multiple entries in a single weather condition
                    # then we should ignore all after the first - have to discuss
                    # after examination
                    print(f'did {cat}: {wc}')
                    continue
                # for each category of weather condition
                for word in cat:
                    # test against words of that category
                    if word in wc:
                        # have a word in weather condition
                        # so add weather_condition to newcols dict
                        newcols[cat].append(wc)
                        didcol[cat] = True
                        break
                    else:
                        # word does not exist in weather condition
                        newcols[cat].append('0')
                        break


    return newcols
