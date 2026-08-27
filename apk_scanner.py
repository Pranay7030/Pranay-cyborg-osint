# 💀 BHACKSH APK SCANNER V2 - Integrated for Pranay-cyborg-osint
# Bhandara Cyber Squad | SKULL x MATRIX Edition
import zipfile
import re
import os

def apk_scanner_module():
    print("""
  ____ _ _ ____ _ ______ _
 | __ )| | | | / \ / ___| |/ / ___|| |__
 | _ \| |_| | / _ \| | | ' /\___ \| '_ \
 | |_) | _ |/ ___ \ |___|. \ ___) | | | |
 |____/|_| |_/_/ \_\____|_|\_\____/|_| |_|
          APK SCANNER V2 - OSINT EDITION
    """)

    apk_path = input("\n[+] APK ka path daal BHACKSH (ex: test.apk): ").strip().replace('"','')

    if not os.path.exists(apk_path):
        print("[!] File nahi mila! Path sahi daal")
        return

    print(f"\n[+] Scanning: {apk_path}\n")
    try:
        with zipfile.ZipFile(apk_path, 'r') as apk:
            files = apk.namelist()

            print("[*] [1/3] Checking Permissions...")
            if 'AndroidManifest.xml' in files:
                data = apk.read('AndroidManifest.xml')
                perms = re.findall(b'android\.permission\.[A-Z_]+', data)
                found = set(perms)
                if found:
                    for p in found:
                        print(f" [!] DANGEROUS: {p.decode()}")
                else:
                    print(" [-] No clear permissions in binary manifest")

            print("\n[*] [2/3] Searching Secrets & URLs...")
            keywords = [b'api_key', b'password', b'secret', b'token', b'http://', b'https://']
            count = 0
            for file in files:
                if file.endswith('.xml') or file.endswith('.dex'):
                    try:
                        content = apk.read(file)
                        for k in keywords:
                            if k in content.lower():
                                print(f" [?] Found '{k.decode()}' in -> {file}")
                                count+=1
                                break
                    except: pass
            if count == 0:
                print(" [-] No hardcoded secrets found")

            print(f"\n[*] [3/3] Total Files: {len(files)}")
            print("\n[+] Scan Complete - BHACKSH V2")

    except Exception as e:
        print(f"[!] Error: {e}")

# Standalone chalane ke liye
if __name__ == "__main__":
    apk_scanner_module()
