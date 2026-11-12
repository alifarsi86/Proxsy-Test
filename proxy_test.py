import requests

proxy_type = input("Proxy Type (http / socks5): ").strip().lower()
proxy_address = input("Proxy address and port: ").strip()

if proxy_type not in ["http", "socks5"]:
    print("Invalid proxy type.")
    exit()

proxy = f"{proxy_type}://{proxy_address}"

proxies = {
    "http": proxy,
    "https": proxy
}

try:
    response = requests.get(
        "https://api.ipify.org",
        proxies=proxies,
        timeout=10
    )

    response.raise_for_status()

    ip = response.text.strip()

    print("status: Connected")
    print("Exit Ip", ip)

except requests.exceptions.RequestException:
    print("status: Disonnected")
    print("The proxy is unavailable, or the connection failed.")
    