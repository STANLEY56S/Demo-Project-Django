"""
common_utility.py
==============
Author: Stanley Parmar
Description: Common Utilities which is used across the project.
See the examples directory to learn about the usage.
"""

# commonUtility.py

# Import the default Libraries
import logging
import os
import json
import sys
import multiprocessing
# Import the custom Libraries
from datetime import datetime
import traceback
import pytz


"""
Function Name: get_sys_args
Inputs: None
Output: Tuple containing environment and config name
Description: Get and validate the command-line arguments.
"""


def get_sys_args():
    if len(sys.argv) != 2:
        debug_print("Usage: python your_script.py <env> <config_name>")
        sys.exit(1)
    config_name = sys.argv[1]
    return config_name


def get_db_config():
    # Get the system arguments to fetch project related Mongo connections only
    filename = get_sys_args()

    print("filename ::: ",filename)


"""
    Function Name: get_django_settings_path
    Inputs: file_location (file location) , filename (file name before _config.json like flask for general_config.json),
    env[ profile file_location prod|dev|qa]
    Output: config_json (List of the configs in the file)
"""


def get_django_settings_path():
    # Read the environment
    DJANGO_ENV = os.getenv('DJANGO_ENV', 'base')

    # open read file of config json
    config = open_read_file('config', '', 'general')

    # Retrieve setting for server config
    setting_config = config['setting']

    return setting_config[DJANGO_ENV]


"""
    Function Name: open_read_file
    Inputs: file_location (file location) , filename (file name before _config.json like flask for general_config.json),
    env[ profile file_location prod|dev|qa]
    Output: config_json (List of the configs in the file)
"""


def open_read_file(file_location, local_env, filename):
    try:
        # Get the directory of the current script
        current_dir = os.path.dirname(__file__)

        # Move up to the backend directory
        backend_dir = os.path.abspath(os.path.join(current_dir, '..'))

        # Construct the full path to the config file
        config_path = os.path.join(backend_dir, file_location, filename + '_config.json')
        # print("config_path: {} : {} : {} ".format(backend_dir, file_location, filename + '_config.json'))

        # Load configuration from the file_location and file
        with open(config_path) as config_file:
            config = json.load(config_file)

        # Get the configuration for the current environment
        if local_env:
            config_json = config.get(local_env)
        else:
            config_json = config

        # Failing if the file is having any issues
        if not config_json:
            raise ValueError("No configuration found for environment:%s", local_env)

        # print(config_json)
        return config_json

    except Exception as e:
        print("ee ----> ", e)
        traceback.print_exc()  # This will print the full traceback, including the line number


"""
    Function Name: multi_proc
    Inputs: tasks
    Output: None
    Description: Multi Pooling Threads.
"""


# Example function to simulate a task
def multi_proc(tasks):
    # Execute each function with its parameters using pool.starmap
    # Create a pool of processes
    with multiprocessing.Pool() as pool:
        # Execute each function with its parameters using pool.starmap
        results = pool.starmap(lambda func, args: func(*args), tasks.values())

    # Print results
    debug_print("Results:")
    for result in results:
        debug_print(result)


"""
    Function Name: debug_print
    Inputs: message to print
    Output:  message on console
    Description: only prints statements if the mode is set to debug
"""


def debug_print(message):
    config = open_read_file('config', '', 'general')
    if config.get("debug", False):
        try:
            print(message)
        except UnicodeEncodeError:
            print(message.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))


"""
Function Name: get_local_time_zone
Inputs:None
Output:local time zone now
Description:
     get local time zone based on the config
"""


def get_local_time_zone(config):
    # getting the local time zone from the config
    time_zone = config['time_zone']
    # converting the local time zone from the config for the current timestamp
    local_tz = pytz.timezone(time_zone)
    # converting the current timestamp to local time zone
    current_time_local = datetime.now(local_tz)
    return current_time_local