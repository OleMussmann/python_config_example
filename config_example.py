#!/usr/bin/env python3

def main():
    # We explore two options for config files, TOML and a Python file.
    print("TOML")
    print("====")
    print()

    #First we import the parsing library.
    import tomli

    # We have two options to load a TOML config. The easier one is
    # to directly load and parse a config file.
    print("load TOML file directly")
    print("-----------------------")
    print()
    with open("./config_direct_import.toml", mode="rb") as config_file:
        toml_config_from_file = tomli.load(config_file)

    # toml_config_from_file is a dictionary.
    print(f"The type of `toml_config_from_file` "
          f"is a dict: {type(toml_config_from_file)}")

    # We can retrieve items like from a dictionary. Make sure to also read
    # the config file to see what the structure looks like.
    print()
    print(toml_config_from_file["global_stuff"])
    print()
    print(toml_config_from_file["vars"]["integer"])
    print()
    print(toml_config_from_file["vars"]["offset_date-time_utc"])
    print()
    print(toml_config_from_file["tables"])
    print(toml_config_from_file["tables"]["nested_one_line"])
    print(toml_config_from_file["tables"]["nested_one_line"]["element_1"])
    print()


    # Another option is to load it like a module
    print("load TOML config like a module")
    print("------------------------------")
    print()

    # Imports the TOML files from the `config` directory,
    # see __init__.py within.
    import config

    print(config.path)  # Print the config file location
    print(config.mod_import_1)
    print(config.mod_import_2)
    print(config.mod_import_2["more_info"]["are_these_normal_TOML_files"])

    # We can also import variables from another Python file
    print()
    print("Python")
    print("======")
    print()

    # We can even use other modules within a python config file.
    # We import it like a module.

    import config_python

    print(config_python.speed_of_light)
    print(config_python.large_value + config_python.small_value)

    # Since the config is full python, we can declare variables,
    # functions, classes, etc. But just because we can, does not
    # mean we should.
    config_python.code_as_config()


if __name__ == "__main__":
    main()
