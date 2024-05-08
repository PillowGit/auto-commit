from rich import print
from dotenv import load_dotenv
from os import getenv

# Constants
ABS_FILEPATH = __file__
ENV_FILEPATH = f"{ABS_FILEPATH[:ABS_FILEPATH.rfind('/')]}/.env"
HOME_DIRECTORY = ""

# Load environment variables
try:
    load_dotenv(dotenv_path=ENV_FILEPATH)
except FileNotFoundError:
    exit(
        f'Error: {ENV_FILEPATH} not found. Please create a file named ".env" in the same place as this script.'
    )
HOME_DIRECTORY = getenv("HOME_DIRECTORY")
if not HOME_DIRECTORY:
    exit("Error: HOME_DIRECTORY not specified in .env file.")
