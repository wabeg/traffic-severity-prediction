# Project 4

This is the Project 4 readme

## Problem Statement

Based on National US Accident Data from 2016-2021, provide recommendations
towards reducing accident severity.

## Cleaning

To Drop:
- number
- zip
- wind_chill (high correlation with temperature and wind speed)
- airport_code (not relevant)
- nautical_twilight, astronomical_twilight (similar to other day/night metrics)
- weather_timestamp (not relevant, assuming weather time is sufficiently close
to time of accident)
- wind_direction (to investigate towards possible drop)
- other weather conditions (precipition, etc) (do we want to assume null values are 0)
- wind_speed (to investigate)

Misc:
- Created dataset: test_weather_condition_unique.20220913.01.csv for splitting
    weather conditions. Contains one entry of each unique Weather Condition
    including null. Will upload with repo

- splitting weather condition column by condition (values have sub-conditions
delimited by '/', 'and', and 'with') towards encoding conditions. Still
programming code to split categories. Seems like there may be instances where
categories are repeated based on keywords, so need to filter to keep row count
same as original dataframe.

- Weather Condition Split categories as of 2022-09-13:
    - rain: 185128+
    - snow: 53748+
    - ice: 318+
    - wind: 42504+
    - clouds: 1024811+
    - thunder: 21599+
    - fog: 44044+
    - fair: 1122389+
    - tornado: 9? 
    - dust: 378+?
    - other: ?
