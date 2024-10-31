# Multiprocessing Task – Large-Scale Data Aggregation
# You are working with a large dataset stored in multiple CSV files. Each file contains transaction data from different regions. Your task is to process these files concurrently and aggregate the data into a summary report that includes the total number of transactions and the sum of transaction amounts for each file.
# Use the multiprocessing library to create separate processes for each CSV file.
# Each process should read its assigned file, sum the transaction amounts, and count the number of transactions.
# Aggregate the results from all processes and print the final summary.

import csv
from queue import Queue 
from multiprocessing import Process, Queue

def calculate(csv_file: str, queue: Queue):
    total_amount = 0
    transaction_count = 0

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader) 

        for index, col_name in enumerate(header):
            if col_name.strip() == "Amount":
                amount_index = index
                break
        
        for row in reader:
            amount = float(row[amount_index])  
            total_amount += amount
            transaction_count += 1
        
    queue.put((total_amount, transaction_count))  

def main() -> None:
    queue = Queue()
    
    csv_fil1_path = 'transactions_region1.csv'
    csv_fil2_path = 'transactions_region2.csv'
    csv_fil3_path = 'transactions_region3.csv'

    process1 = Process(target=calculate, args=(csv_fil1_path, queue))
    process2 = Process(target=calculate, args=(csv_fil2_path, queue))  
    process3 = Process(target=calculate, args=(csv_fil3_path, queue))

    procs = [process1, process2, process3]

    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()

    total_results = [queue.get() for _ in procs]

    amount = sum(result[0] for result in total_results)  
    count = sum(result[1] for result in total_results) 

    print(f"Total amount: {amount:.2f}")
    print(f"Total transaction count: {count}")

if __name__ == '__main__':
    main()
