# Define a function named water_state that takes one parameter: temperature
def water_state(temperature):
    # Check if the temperature is less than or equal to 0
    if temperature <= 0:
        return "Solid"  # Return "Solid" if temperature is <= 0
    # Check if the temperature is between 0 and 100 (exclusive)
    elif 0 < temperature < 100:
        return "Liquid"  # Return "Liquid" if temperature is between 0 and 100
    else:
        return "Gas"  # Return "Gas" for all other cases

    # Define constants for freezing point and boiling point of water
    FREEZING_POINT = 0
    BOILING_POINT = 100

    # Define a function named water_state that takes one parameter: temperature
    def water_state(temperature):
        # Check if the temperature is less than or equal to the freezing point
        if temperature <= FREEZING_POINT:
            return "Solid"
            # Check if the temperature is between the freezing point and boiling point
        elif FREEZING_POINT < temperature < BOILING_POINT:
            return "Liquid"
            # Return "Gas" for all other cases
        else:
            return "Gas"



        if temperature <= 15:
            return "Cold"

        elif 15 < temperature < 25:
            return "Warm"

        else:
            return "Hot"