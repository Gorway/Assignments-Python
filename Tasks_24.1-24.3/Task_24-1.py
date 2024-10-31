# #Threading Task – Real-Time Log Analyzer
# Develop a log monitoring system for a web server. The system should read and analyze server logs in real-time. New log entries are appended to a file continuously, and your goal is to monitor the log file for specific error keywords.
# Create a thread that reads new lines added to the log file continuously.
# Create another thread that checks if any new line contains the keyword “ERROR” and prints it to the console.
# Both threads should run concurrently without blocking each other, using shared data structures like queues to communicate.

import time
import random
import threading
from queue import Queue
import sys

log_file = 'server_log.txt'
log_queue = Queue()
exit = False

def main():

    def reader(file_path, queue):
        with open(file_path, 'r') as file:
            file.seek(0,2)
            while not exit:
                line = file.readline()
                if line:
                    queue.put(line)  
                else:
                    time.sleep(0.5)
    
    def checker(queue):
      while not exit:
        try:
          line = queue.get()  
          if "ERROR" in line:
            print(f"Error detected: {line}")
          queue.task_done()
        except Exception:
           continue
           
    
    def writer(file_path):
      messages = [ '[2024-10-29 09:01:23] INFO: Server started successfully.',
                 '[2024-10-29 09:02:45] INFO: New user connected from IP 192.168.1.10.',
                 '[2024-10-29 09:03:12] WARNING: High memory usage detected.',
                 "[2024-10-29 09:04:18] INFO: User 'admin' logged in.",
                 '[2024-10-29 09:05:07] ERROR: Failed to connect to database.' ]
      while not exit:
        message = random.choice(messages)
        with open(file_path, 'a') as file:
            file.write(f"{time.time()}{message}\n")
            print('adding...')
        time.sleep(0.5) 

    def program_end():
       global exit
       exit = True
       print("Log monitoring ended.")
       sys.exit()

    reader = threading.Thread(target=reader, args=(log_file, log_queue))
    checker = threading.Thread(target=checker, args=(log_queue,))
    writer = threading.Thread(target=writer, args=(log_file,))
    end_timer = threading.Timer(10, program_end)
    
    reader.start()
    checker.start()
    writer.start()
    end_timer.start()
    
    end_timer.join()
    reader.join()
    checker.join()
    writer.join()

if __name__ == "__main__":
   main()