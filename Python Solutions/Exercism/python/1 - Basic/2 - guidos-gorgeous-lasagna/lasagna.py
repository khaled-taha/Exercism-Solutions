EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - time


def preparation_time_in_minutes(layers):
    """ Return preparation_time_in_minutes

    :param layers: int number of layers
    :return: int - layers * 2

    This function should return the total number of minutes you've been cooking,
    or the sum of your preparation time and the time the lasagna has already spent baking in the oven.
    
    """
    return PREPARATION_TIME * layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return elapsed cooking time.

    :param number_of_layers: int the number of layers.
    :param elapsed_bake_time: int the time already spent baking.
    :return: int - the total elapsed minutes spent cooking the lasagna

    This function takes two numbers representing the number of layers & the time already spent baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time