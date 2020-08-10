import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
     return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_farenheit):
    celsiustemp = round((temp_in_farenheit - 32) *  5/9, 1)
    return celsiustemp


def calculate_mean(total, num_items):
    mean = round(total / num_items)
    return mean



def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
   

    with open("data/forecast_5days_a.json") as forecast_file:
        forecast_data = json.load(forecast_file)

    daily_forecast = forecast_data["DailyForecasts"]
#Dates
    for date in daily_forecast:
        date_1 = date["Date"]
        print(date_1)

#min temp for all days
    for date in daily_forecast:
        temperature = date["Temperature"]
        minimum_1 = temperature["Minimum"]
        minimum_2 = minimum_1["Value"]

#max temp for all days
    for date in daily_forecast:
        temperature_2 = date["Temperature"]
        maximum_1 = temperature_2["Maximum"]
        maximum_2 = maximum_1["Value"]

#long phrase description for each day
    for date in daily_forecast:
        day_long = date["Day"]
        day_long_phrase = day_long["LongPhrase"]

#long phrase description for each night
    for date in daily_forecast:
        night_long = date["Night"]
        night_long_phrase = night_long["LongPhrase"]
       

#Day % chance of rain
    for date in daily_forecast:
        day_rain = date["Day"]
        chance_day_rain = day_rain["PrecipitationProbability"]
        

#night % chance of rain
    for date in daily_forecast:
        night_rain = date["Night"]
        chance_night_rain = night_rain["PrecipitationProbability"]
       

   

# Retrieve Temperature
    # for item in forecast_data["DailyForecasts"]:
    #     min_temp = (item["Temperature"]["Minimum"]["Value"])
    #     max_temp = (item["Temperature"]["Maximum"]["Value"])
    #     print( f"Minimum: {min_temp}, Maximum: {max_temp}")
# output = " " #this is just a break for formatting
# output += "--------" #{date goes here} "--------\n"
# output += f"Minimum Temperature: "  #Min Temp goes here "{min_temp}\n"
# output += f"Maximum Temperature: "  #max tem goes here {max_temp}\n"
# output += f"Daytime: "  #forecast here\n"
# output += f"    Chance of rain:" #rain outlook goes here  1%\n"
# output += f"Nighttime: "  #forecast here\n"
# output += f"    Chance of rain: "  #rain outlook here  0%\n"
# print(output)
   

# print(output)


if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))
