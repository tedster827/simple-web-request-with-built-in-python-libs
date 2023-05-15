import http.client
import sys
import os
from datetime import datetime


def log_compatible_versions(filename):
    """
    Log the current Python version to a specified file
    :param filename: the name of the file to which the version will be logged
    """

    # Get the Python version
    version = sys.version

    # Get the current date and time
    now = datetime.now()

    # Format the date and time string
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # Create the log message
    log_message = f"Timestamp: {timestamp}, Python Version: {version}\n"

    # Append the log message to the file
    with open(filename, 'a') as file:
        file.write(log_message)


def make_sample_request(host: str, endpoint: str):
    """
    Make a GET request to a specific host and endpoint
    :param host: the domain to which the request will be sent
    :param endpoint: the endpoint (path) of the resource
    """

    # Create a connection to the host
    conn = http.client.HTTPSConnection(host)

    # Define headers for the request
    headers = {'User-Agent': 'Python http.client'}

    # Make the request
    conn.request("GET", endpoint, headers=headers)

    # Get the response
    res = conn.getresponse()

    # Read the data from the response
    data = res.read()

    # Decode the data and print it
    print(data.decode("utf-8"))

    pass


def main():
    print(">>> Simple Web Request Without The Requests Library")
    url = "example.com"
    endpoint = "/"

    make_sample_request(url, endpoint)
    log_compatible_versions("compatible_versions.log")
    pass


main()
