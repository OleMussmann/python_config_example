import pint
unit = pint.UnitRegistry()

speed_of_light = 299e6 * unit.meter / unit.second

large_value = 130 * unit.meter
small_value = 10 * unit.micrometer

def code_as_config():
    print("Executing a function from the config file.")
    print("Make sure to keep this file for configurations _only_,")
    print("so don't abuse it for other things like this function.")
