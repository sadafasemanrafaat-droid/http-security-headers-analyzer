# HTTP Security Headers Analyzer

A Python-based tool for analyzing HTTP security headers on a target HTTP server.

## Description

This project is a simple HTTP security headers analyzer built with Python.

The tool connects to an HTTP server, sends an HTTP GET request, receives the response, and checks for common security headers.

It can identify whether security headers are present and display their values.

This project was developed as a practical cybersecurity learning project to understand HTTP communication, socket programming, response parsing, dictionaries, and security headers.

## Features

- Target host/IP input
- Custom port input
- TCP connection check
- HTTP service detection
- HTTP GET request
- HTTP response inspection
- Security header extraction
- Displays header values
- Detects missing security headers
- Scan time calculation

## Security Headers Checked

The tool checks the following headers:

- `X-Frame-Options`
- `Content-Security-Policy`
- `Strict-Transport-Security`
- `X-Content-Type-Options`

## How to Run

### 1. Start a local HTTP server

For testing in a safe local environment:

```bash
python3 -m http.server 9000 --bind 127.0.0.1
```

### 2. Run the analyzer

Open another terminal:

```bash
python3 security_headers.py
```

### 3. Enter the target

Example:

```text
Enter Host: 127.0.0.1
Enter port: 9000
```

## Example Output

```text
X-Frame-Options: MISSING
Content-Security-Policy: MISSING
Strict-Transport-Security: MISSING
X-Content-Type-Options: MISSING
Open_port:sucess
total time:0.22second
```

A custom local test server can also be used to verify detected header values.

Example:

```text
X-Frame-Options: DENY
Content-Security-Policy: MISSING
Strict-Transport-Security: MISSING
X-Content-Type-Options: MISSING
```

## Technologies Used

- Python 3
- Socket Programming
- TCP
- HTTP
- Dictionaries
- String Parsing
- Linux / WSL
- Git
- GitHub

## Project Purpose

The purpose of this project is to practice:

1. TCP socket connections
2. HTTP requests
3. HTTP response parsing
4. Dictionary-based data processing
5. Security header analysis
6. Basic cybersecurity automation

## Security Note

This tool is intended for educational purposes and authorized security testing only.

Use it only against systems you own or have explicit permission to test.

## Future Improvements

- Improve error handling
- Add command-line arguments
- Add security header recommendations
- Add security scoring
- Improve HTTP response parsing
- Generate cleaner reports
- Support HTTPS
- Add logging

