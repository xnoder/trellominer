"""
Read configuration data from YAML.
"""

import ruamel.yaml


def read(name):
    """Read a YAML config file into a standard Python dictionary.

    Args:
        name (str): The name of the config file to open.

    Returns:
        dict: A dictionary containing the configuration.

    Raises:
        None
    """
    with open(name, mode='r') as config_file:
        config = ruamel.yaml.load(config_file, ruamel.yaml.RoundTripLoader)

    return config
