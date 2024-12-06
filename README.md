# Log Analysis Script

A Python-based tool to analyze web server log files. This tool processes logs to extract meaningful insights, such as requests per IP address, the most accessed endpoint, and detection of suspicious activities (e.g., brute-force login attempts). The results are displayed in the terminal and saved to a CSV file for further analysis.

---

## Features

- **Requests Per IP Address**: Count and display the number of requests made by each IP address.
- **Most Accessed Endpoint**: Identify and report the endpoint accessed most frequently.
- **Suspicious Activity Detection**: Detect potential brute-force attacks by analyzing failed login attempts.
- **CSV Output**: Save the analysis results in a well-structured CSV file for offline reference.

---

## How the Solution Was Developed

### 1. **Reading and Parsing the Log File**
   - The log file is read line by line to extract key information such as IP addresses, timestamps, HTTP methods, endpoints, and status codes.
   - The parsed data is stored in Python dictionaries and counters for efficient processing.

### 2. **Requests Per IP Address**
   - Used Python's `collections.Counter` to count occurrences of each IP address.
   - Results are sorted by the request count in descending order and displayed in the terminal.

### 3. **Most Accessed Endpoint**
   - Extracted endpoints from log entries and counted their occurrences.
   - Identified the endpoint with the highest access count and displayed it alongside its frequency.

### 4. **Suspicious Activity Detection**
   - Focused on log entries with the `401` status code, which indicates failed login attempts.
   - Introduced a configurable threshold (`FAILED_LOGIN_THRESHOLD`) to flag IP addresses with excessive failed logins.
   - This threshold is set to 4 by default but can be adjusted as needed.

### 5. **Results Formatting and Output**
   - Results are neatly displayed in the terminal in a human-readable format.
   - A CSV file (`log_analysis_results.csv`) is generated, containing three sections: 
      - Requests per IP
      - Most Accessed Endpoint
      - Suspicious Activity

---

## Installation and Usage

### Prerequisites
- Python 3.6 or higher
- Basic understanding of web server log formats

### Steps to Run the Tool
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   
2. Place your log file in the same directory as the script (or specify its path in the code).

3. Run the script:
    ```bash
    python log_analysis.py
   ```
4. View the results in the terminal and check the CSV output (log_analysis_results.csv).

---

### Example Output
```bash
Requests per IP:
203.0.113.5          8
198.51.100.23        8
192.168.1.1          7
10.0.0.2             6
192.168.1.100        5

Most Frequently Accessed Endpoint:
/login (Accessed 13 times)

Suspicious Activity Detected:
203.0.113.5          8
192.168.1.100        5
```

---

### CSV Output
The CSV file contains:

- A table of requests per IP address.
- The most accessed endpoint and its access count.
- A list of suspicious IPs with their failed login counts.

---

### Why This Solution?
I approached the problem with a modular and robust methodology:

- Used efficient data structures (Counter and dictionaries) for fast data processing.
- Ensured configurability with the FAILED_LOGIN_THRESHOLD variable.
- Followed Pythonic coding practices for clarity and maintainability.
- Paid attention to edge cases, such as handling ties in counts and missing data.
