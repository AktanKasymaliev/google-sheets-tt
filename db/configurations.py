from configparser import ConfigParser, NoOptionError, NoSectionError
import os

def load_conf(config: ConfigParser, section: str, name: str, default=None) -> str:
    """
    "If the config file has a section and name, return the value, otherwise return the default."
    
    The function takes three arguments:
    config: The ConfigParser object.
    section: The section of the config file.
    name: The name of the config file.
    default: The default value to return if the section and name don't exist.
    The function returns the value of the config file if it exists, otherwise it returns the default
    value
    
    :param config: The ConfigParser object that we created earlier
    :type config: ConfigParser
    :param section: The section of the config file to look in
    :type section: str
    :param name: The name of the parameter to load
    :type name: str
    :param default: The default value to return if the option is not found
    :return: The value of the option name in the section section.
    """
    try:
        output = config.get(section, name)
    except (NoOptionError, NoSectionError):
        output = default
    return output

def config() -> None:
    """
    It reads the settings.ini file and sets the environment variables
    for the database connection
    """
    config_parse = ConfigParser()
    config_parse.read("settings.ini")
    DATABASE = "DATABASE"

    os.environ.setdefault("DATABASE_NAME", load_conf(config_parse, DATABASE, "NAME", "blog"))
    os.environ.setdefault("DATABASE_USER", load_conf(config_parse, DATABASE, "USER", "user"))
    os.environ.setdefault("DATABASE_PASSW", load_conf(config_parse, DATABASE, "PASSWORD", "root"))
    os.environ.setdefault("DATABASE_HOST", load_conf(config_parse, DATABASE, "HOST", "localhost"))
    os.environ.setdefault("DATABASE_PORT", load_conf(config_parse, DATABASE, "PORT", "5432"))

def get_config_data(key: str) -> str:
    """
    It returns the value of the environment variable with the name `key`
    
    :param key: The key of the configuration data you want to retrieve
    :type key: str
    :return: The value of the key in the environment variable.
    """
    return os.environ.get(key)