import datetime
import time

def check_wifi_connection():
    return True 
def report_current_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current time:", current_time)

def main():
    while True:
        if check_wifi_connection():
            report_current_time()
            time.sleep(60)  
        else:
            print("WiFi not connected. Waiting to reconnect...")
            time.sleep(10) 

if __name__ == "__main__":
    main()