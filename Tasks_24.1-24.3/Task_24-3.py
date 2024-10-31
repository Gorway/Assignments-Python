# Asyncio Task – Asynchronous File Reader and Data Processor
# You are building a system to process JSON files that contain user data (such as user profiles or purchase records). Your task is to read multiple JSON files concurrently and extract specific information like user names or purchase totals.
# Use the asyncio library to create coroutines for reading multiple JSON files concurrently.
# Extract specific information from each file (e.g., user names or purchase totals).
# Print the extracted data after all files have been read and processed.
# Use asyncio.gather() to read all files concurrently.

import json
import asyncio

async def reader(json_file: str) -> dict:
    with open(json_file, 'r') as file:
        user_data = json.load(file)
    return user_data

async def collect_user_names(json_file: str) -> list:
     data = await reader(json_file)
     user_names = [user['name'] for user in data]
     return user_names

async def calculate_total_purchase(json_file: str) -> float:
        data = await reader(json_file)
        total_amount = sum(purchase['amount']  for user in data for purchase in user['purchases'])
        return total_amount

async def manage_files(json_files: list) -> tuple:
     user_names = [collect_user_names(file) for file in json_files]
     purchase_totals = [calculate_total_purchase(file) for file in json_files]
     user_id_numbers = [collect_id_numbers(file) for file in json_files]

     user_names_results = await asyncio.gather(*user_names)
     purchase_totals_results = await asyncio.gather(*purchase_totals)
     user_id_numbers = await asyncio.gather(*user_id_numbers)

     return (user_names_results, purchase_totals_results, user_id_numbers)

async def collect_id_numbers(json_file: str) -> list:
     data = await reader(json_file)
     user_id_numbers = [user['user_id'] for user in data]
     return user_id_numbers

def main() -> None:
     json_files = ['user_data.json', 'user_data2.json', 'user_data3.json']

     loop = asyncio.get_event_loop()
     user_names, purchase_totals, user_ids = loop.run_until_complete(manage_files(json_files))

     print("User names:")
     for names in user_names:
        print(names)

     print("\nPurchase Totals:")
     for total in purchase_totals:
        print(f"${total:.2f}")

     print("\n Id numbers:")
     for id in user_ids:
          print(id)
    

if __name__ == "__main__":
    main()

