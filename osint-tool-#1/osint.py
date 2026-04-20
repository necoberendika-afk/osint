import requests

def get_ip_info(ip):
    """
    Get geolocation and other information for an IP address using ipinfo.io API.
    """
    url = f"http://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"IP Address: {ip}")
            print(f"Hostname: {data.get('hostname', 'N/A')}")
            print(f"City: {data.get('city', 'N/A')}")
            print(f"Region: {data.get('region', 'N/A')}")
            print(f"Country: {data.get('country', 'N/A')}")
            print(f"Location: {data.get('loc', 'N/A')}")
            print(f"Organization: {data.get('org', 'N/A')}")
        else:
            print(f"Error retrieving info: HTTP {response.status_code}")
    except requests.RequestException as e:
        print(f"Network error: {e}")

if __name__ == "__main__":
    ip = input("Enter IP address to lookup: ").strip()
    if ip:
        get_ip_info(ip)
    else:
        print("No IP address provided.")