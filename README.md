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
