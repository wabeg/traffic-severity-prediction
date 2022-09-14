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
- weather_timestamp (not relevant, assuming weather time is sufficiently close to time of accident)
- wind_direction (to investigate towards possible drop)
- other weather conditions (precipition, etc) (do we want to assume null values are 0)
- wind_speed (to investigate)

Misc:
- Created dataset: test_weather_condition_unique.20220913.01.csv for splitting
    weather conditions. Contains one entry of each unique Weather Condition
    including null. Will upload with repo

- splitting weather condition column by condition (values have sub-conditions
delimited by '/', 'and', and 'with') towards encoding conditions. 

- Weather Condition Split categories as of 2022-09-13:
    - clouds: 1109693
    - dust: 7629
    - fair: 1296212
    - fog: 80962
    - ice: 2105
    - rain: 196740
    - snow: 57673
    - thunder: 32385
    - tornado: 11
    - wind: 42531
    - other: ?

Roadmap:

EDA via:

- Relationships between time/day of the day/week, location (i.e. junction/intersection) and severity of accident
- Relationships between state/county/city and severity of accident
- Relationships between timezone and severity of accident or timezone and locations of accidents or timezone and timing of most frequent accidents
- Relationships between weather features (i.e. temp, wind_chill, humidity, pressure, visibility, wind_direction, wind_speed, precipitation, weather_condition) and severity, location of accidents, timing of most frequent accidents
- Most frequent points of interest (i.e. amenities, bumps, give_ways, junctions, roundabouts, etc.) per severity or per frequency of accidents
- Use k-prototype clustering (best for mix of categorical and numerical data) for transfer learning
- First optimize for silhouette scores (find range of params)
- Then use labels w/ varying params for supervised classifier
- Create a Tableau dashboard with U.S. map and diff stats/filters

Modeling

- Classification models w/ appropriate metrics on severity
