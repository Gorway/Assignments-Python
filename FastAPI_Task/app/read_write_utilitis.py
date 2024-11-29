import os  
import json
import errors
import dotenv
import asyncio
import aiofiles
from typing import Optional, List, Union, Dict, Any

dotenv.load_dotenv()
USERS_FILE = os.getenv("USERS_FILE", "users.json")
TASKS_FILE = os.getenv("TASKSFILE", "tasks.json")


# Asynchronously reads the JSON file and returns its contents as a list of dictionaries.
# If the file is empty or not found, it returns an empty list. 
# Raises a FileError if JSON decoding fails.
async def read_file(file_path: str) -> List[Dict]:
    try:
        async with aiofiles.open(file_path, mode="r") as file:
            content = await file.read()
            return json.loads(content) if content else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise errors.FileError("JSON file enjured.")
    
# Asynchronously writes data (in JSON format) to the given file path.
# The data is indented for better readability.
async def write_file(file_path: str, data: Any) -> None:
    async with aiofiles.open(file_path, mode="w") as file:
        await file.write(json.dumps(data, indent=4))

# Initializes the USERS_FILE and TASKS_FILE if they do not exist.
# Creates empty JSON arrays in the files if they are missing.
async def init_files() -> None:
    for file in [USERS_FILE, TASKS_FILE]:
        if not os.path.exists(file):
            async with aiofiles.open(file, mode='w') as new_file:
                await new_file.write("[]")