
# Function:
def play_tennis(outlook, humidity, windy):
    # response string, holding given args:
    response_str = f"outlook={outlook}, humidity={humidity}, windy={windy}, play tennis? "

    # weather dictionary, holding lists of valid weather conditions:
    weather_dict = {
        "outlook": ["sunny", "overcast", "rainy"],
        "humidity": ["high", "normal"],
        "windy": ["true", "false"]
    }

    has_valid_args = True  # holds whether args are valid

    # loop through list of dictionaries holding each args name and value:
    for arg_dict in [{"outlook": outlook}, {"humidity": humidity}, {"windy": windy}]:
        key = list(arg_dict.keys())[0]  # get arg key
        value = arg_dict.get(key)  # get arg value

        if value not in weather_dict[key]:  # if value isn't a valid weather condition:
            has_valid_args = False  # flag args as invalid
            response_str += f"unknown {key} value"  # add error message to response

    if not has_valid_args:  # if args aren't valid:
        return response_str  # return response string, informing user of error(s)
    else:  # args are valid:
        if outlook == "sunny":  # if outlook is sunny:
            if humidity == "high":  # if humidity is high:
                return response_str + "no"  # return response string with 'no'
            else:  # else humidity is normal:
                return response_str + "yes"  # return response string with 'yes'
        elif outlook == "overcast":  # if outlook is overcast:
            return response_str + "yes"  # return response string with 'yes'
        elif outlook == "rainy":  # if outlook is rainy:
            if windy == "false":  # if windy is false:
                return response_str + "yes"  # return response string with 'yes'
            else:  # else windy is true:
                return response_str + "no"  # return response string with 'no'


# Test cases:

# Cases with valid args:
print(play_tennis("sunny", "high", "true"))
print(play_tennis("overcast", "high", "false"))
print(play_tennis("rainy", "high", "false"))

# Cases with invalid args:
print(play_tennis("xyz", "high", "false"))  # invalid outlook
print(play_tennis("sunny", "xyz", "false"))  # invalid humidity
print(play_tennis("sunny", "high", "xyz"))  # invalid windy
