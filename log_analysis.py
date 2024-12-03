import re
import csv
from collections import defaultdict

#Set-Up
FAILED_LOGIN_THRESHOLD = 4
LOG_FILE = "sample.log"
OUTPUT_CSV = "log_analysis_results.csv"

#Parsing the log file
def parse_log_file(log_file):
    ip_requests = defaultdict(int)
    endpoint_requests = defaultdict(int)
    failed_logins = defaultdict(int)

    with open(log_file, 'r') as file:
        for line in file:
            #Extracting IP, endpoint, and status code
            ip_match = re.search(r'^(\d+\.\d+\.\d+\.\d+)', line)
            endpoint_match = re.search(r'\"(?:GET|POST) ([^ ]+)', line)
            status_code_match = re.search(r'\" (\d{3}) ', line)
            failure_msg = "Invalid credentials"

            if ip_match:
                ip = ip_match.group(1)
                ip_requests[ip] += 1

            if endpoint_match:
                endpoint = endpoint_match.group(1)
                endpoint_requests[endpoint] += 1

            if status_code_match:
                status_code = status_code_match.group(1)
                if status_code == '401' or failure_msg in line:
                    if ip_match:
                        failed_logins[ip] += 1

    return ip_requests, endpoint_requests, failed_logins

#Saving results to CSV
def save_to_csv(ip_requests, most_accessed, suspicious_activity):
    with open(OUTPUT_CSV, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Requests per IP"])
        writer.writerow(["IP Address", "Request Count"])
        for ip, count in sorted(ip_requests.items(), key=lambda x: x[1], reverse=True):
            writer.writerow([ip, count])

        writer.writerow([])
        writer.writerow(["Most Accessed Endpoint"])
        writer.writerow(["Endpoint", "Access Count"])
        writer.writerow(most_accessed)

        writer.writerow([])
        writer.writerow(["Suspicious Activity"])
        writer.writerow(["IP Address", "Failed Login Count"])
        for ip, count in suspicious_activity:
            writer.writerow([ip, count])


def main():
    ip_requests, endpoint_requests, failed_logins = parse_log_file(LOG_FILE)

    #Sorting IP requests by count
    sorted_ip_requests = sorted(ip_requests.items(), key=lambda x: x[1], reverse=True)

    #Finding the most accessed endpoint
    most_accessed = max(endpoint_requests.items(), key=lambda x: x[1])

    #Filtering suspicious activity
    suspicious_activity = [(ip, count) for ip, count in failed_logins.items() if count > FAILED_LOGIN_THRESHOLD]

    #Displaying results
    print("\nRequests per IP:")
    for ip, count in sorted_ip_requests:
        print(f"{ip:<20} {count}")

    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_accessed[0]} (Accessed {most_accessed[1]} times)")

    print("\nSuspicious Activity Detected:")
    if suspicious_activity:
        for ip, count in suspicious_activity:
            print(f"{ip:<20} {count}")
    else:
        print("No suspicious activity detected.")

    #Saving results to CSV
    save_to_csv(ip_requests, most_accessed, suspicious_activity)
    print(f"\nResults saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()