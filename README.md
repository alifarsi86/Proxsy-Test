Proxy Tester

A simple and lightweight Python tool for testing HTTP and SOCKS5 proxies. It checks whether a proxy is working correctly, verifies the connection, and retrieves the public IP address assigned by the proxy.

Overview

Proxy Tester is a command-line application built with Python and the "requests" library.

It allows users to enter a proxy type and address, establish a connection through the proxy, and check whether the proxy is functional.

If the connection is successful, the application displays the connection status and the proxy's outgoing IP address. Otherwise, it reports that the proxy is unavailable or the connection has failed.

Features

- HTTP Proxy Support: Test HTTP proxies.
- SOCKS5 Proxy Support: Test SOCKS5 proxies.
- Connection Verification: Check whether the proxy connection is successful.
- Public IP Detection: Retrieve the outgoing IP address through the proxy.
- Input Validation: Validate the specified proxy type.
- Error Handling: Handle connection errors and request timeouts.
- Lightweight: Simple, fast, and easy to use.

Requirements

- Python 3.8+
- Requests

Installation

1. Clone the repository:
   
   git clone https://github.com/your-username/proxy-tester.git

2. Navigate to the project directory:
   
   cd proxy-tester

3. Install the required dependency:
   
   pip install requests

Usage

Run the script using Python:

python proxy_test.py

The application will ask you to enter the proxy type and address.

Example

Proxy Type (http / socks5): socks5
Proxy address and port: 127.0.0.1:1080

Status: Connected
Exit IP: 203.0.113.10

Supported Proxy Formats

Proxy Type| Example
HTTP| "192.168.1.10:8080"
SOCKS5| "127.0.0.1:1080"

Note: The proxy address must include both the IP address (or hostname) and port.

How It Works

1. The user selects a proxy type ("http" or "socks5").
2. The user enters the proxy address and port.
3. The application validates the proxy type.
4. A proxy configuration is created.
5. A request is sent to "api.ipify.org" through the specified proxy.
6. If the request succeeds, the application displays the connection status and outgoing IP address.
7. If an error occurs, the application reports the connection failure.

Error Handling

The application handles common request-related errors, including:

- Connection failures.
- Proxy connection errors.
- Request timeouts.
- Invalid or unavailable proxies.

Dependencies

- "Requests" (https://requests.readthedocs.io/)

- "ipify API" (https://www.ipify.org/) – Used to retrieve the public IP address.

Limitations

- Supports HTTP and SOCKS5 proxies.

- Proxy authentication is not currently implemented.

- SOCKS5 support may require installing additional dependencies:
  
  pip install "requests[socks]"

Future Improvements

- Support for authenticated proxies.
- Proxy response time measurement.
- More detailed connection diagnostics.
- Batch testing of multiple proxies.
- Exporting test results to a file.

License

This project is open-source and available for educational and personal use.
Made by Ali farsi
