import time
from os import system
from datetime import datetime

import schedule

def write_logs(path: str):
    with open(path, 'w') as log:    
        log.write(f'Data updated or saved at: {str(datetime.now())}\n')

def job():
    system('python main.py')

def main():
    print("\n*Schedule started. Every 5 minutes google-sheet reader bot works*")
    job()
    schedule.every(5).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
        write_logs('logs/logs.txt')

if __name__ == "__main__":
    main()