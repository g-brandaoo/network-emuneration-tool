main.import socket
import requests
import json
from concurrent.futures import ThreadPoolExecutor

# ================= CONFIG =================
BASE_IP = "192.168.0"
PORTS = [21, 22, 23, 53, 80, 443, 8080, 7547]
TIMEOUT = 1
MAX_THREADS = 100

HTTP_TIMEOUT = 3

results = {}

# ================= PORT SCANNER =================
def scan_port(ip, port):
    s = socket.socket()
    s.settimeout(TIMEOUT)

    try:
        s.connect((ip, port))
        return True
    except:
        return False
    finally:
        s.close()


def scan_ip(ip):
    open_ports = []

    for port in PORTS:
        if scan_port(ip, port):
            open_ports.append(port)

    return open_ports


# ================= HTTP =================
def fetch(url):
    try:
        return requests.get(url, timeout=HTTP_TIMEOUT)
    except:
        return None


def http_scan(ip, port):
    data = []
    for protocol in ["http", "https"]:
        url = f"{protocol}://{ip}:{port}"
        response = fetch(url)

        if response:
            data.append({
                "url": url,
                "status": response.status_code,
                "server": response.headers.get("Server")
            })

    return data


# ================= INTEGRATION =================
def process_target(ip):
    open_ports = scan_ip(ip)

    if open_ports:
        results[ip] = {
            "ports": open_ports,
            "http": []
        }

        print(f"[HOST] {ip} -> {open_ports}")

        for port in open_ports:
            if port in [80, 443, 8080]:
                http_data = http_scan(ip, port)
                results[ip]["http"].extend(http_data)


def scan_network():
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        for i in range(1, 255):
            ip = f"{BASE_IP}.{i}"
            executor.submit(process_target, ip)


# ================= SAVE =================
def save_results():
    with open("results.json", "w") as f:
        json.dump(results, f, indent=4)


# ================= MAIN =================
if __name__ == "__main__":
    print("Scanning...\n")
    scan_network()

    save_results()

    print("\nResultados salvos em results.json")