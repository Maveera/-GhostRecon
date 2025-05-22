import requests

# === Banner and Author Info ===
print("""
  ____ _               _                 
 / ___| |__   ___  ___| | _____ _ __ ___ 
| |  _| '_ \ / _ \/ __| |/ / _ \ '__/ __|
| |_| | | | |  __/ (__|   <  __/ |  \__ \\
 \____|_| |_|\___|\___|_|\_\___|_|  |___/

             GhostRecon - Passive Recon Tool
""")

print("Author   : Maveera")
print("Created  : May 22, 2025")
print("Maintainer: Mavizz")
print("\n🔗 Connect with me:")
print("Webpage : https://maveera.rf.gd/")
print("Instagram : https://www.instagram.com/_.mavi._27_/")
print("LinkedIn  : https://www.linkedin.com/in/maveera/")
print("GitHub    : https://github.com/Maveera/")

# === Get domain input from user ===
domain = input("🔍 Enter the target domain (e.g. example.com): ")

# === Build Wayback URL ===
wayback_url = f"http://web.archive.org/cdx/search/cdx?url={domain}/*&output=text&fl=original&collapse=urlkey"

# === Request to Wayback Machine ===
response = requests.get(wayback_url)

# === Check response and process ===
if response.status_code == 200:
    urls = response.text.strip().split('\n')
    print(f"\n✅ Found {len(urls)} URLs!")
    filename = f"{domain}_wayback_urls.txt"
    with open(filename, "w") as file:
        for url in urls:
            print(url)
            file.write(url + "\n")
    print(f"\n📁 Saved to: {filename}")
else:
    print(f"\n❌ Failed to fetch URLs. Status code: {response.status_code}")
