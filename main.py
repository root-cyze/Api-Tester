import os
import requests
import platform                                                import json
from datetime import datetime
from colorama import Fore, Style, init                         
init(autoreset=True)
                                                               # -------- LOG SİSTEMİ -------- #
def timestamp():                                                   return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_info(message):                                             print(Fore.CYAN + f"[INFO {timestamp()}] " + Style.RESET_ALL + message)

def log_success(message):
    print(Fore.GREEN + f"[SUCCESS {timestamp()}] " + Style.RESET_ALL + message)

def log_error(message):
    print(Fore.RED + f"[ERROR {timestamp()}] " + Style.RESET_ALL + message)

def log_warn(message):
    print(Fore.YELLOW + f"[WARN {timestamp()}] " + Style.RESET_ALL + message)

def log_input(message):                                            return input(Fore.BLUE + f"[INPUT {timestamp()}] " + Style.RESET_ALL + message)
                                                               def log_exit(message):
    print(Fore.MAGENTA + f"[EXIT {timestamp()}] " + Style.RESET_ALL + message)

# -------- GÖRSEL -------- #
def temizle_ekran():
    os_turu = platform.system()
    os.system("cls" if os_turu == "Windows" else "clear")

def baslik_goster():
    print(
        Fore.BLUE + "    ___    ____  ____                      \n" +
        Fore.LIGHTBLUE_EX + "   /   |  / __ \\/  _/                      \n" +
        Fore.CYAN + "  / /| | / /_/ // /                        \n" +
        Fore.LIGHTCYAN_EX + " / ___ |/ ____// /                         \n" +
        Fore.WHITE + "/_/  |_/_/___/___/________________________ \n" +
        Fore.BLUE + "        /_  __/ ____/ ___/_  __/ ____/ ___/\n" +
        Fore.LIGHTBLUE_EX + "         / / / __/  \\__ \\ / / / __/ / /_/ / \n" +
        Fore.CYAN + "        / / / /___ ___/ // / / /___/ _, _/  \n" +
        Fore.LIGHTCYAN_EX + "       /_/ /_____//____//_/ /_____/_/ |_|   \n" +
        Style.RESET_ALL
    )
print("")
print("")
# -------- API İSTEĞİ -------- #
def fetch_api_response(url, headers=None):
    try:
        log_info("Sending request to API...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        log_success("API responded successfully.")
        content_type = response.headers.get("Content-Type", "")

        if "application/json" in content_type:
            return response.json()
        else:
            log_warn("Response is not JSON. Displaying raw text.")
            return response.text
    except requests.exceptions.RequestException as e:
        log_error(f"Request failed: {e}")
        return None

# -------- ANA FONKSİYON -------- #
def main():
    temizle_ekran()
    baslik_goster()

    try:
        api_url = log_input("Enter the API URL: ").strip()
        if not api_url:
            log_error("URL cannot be empty.")
            return

        add_headers = log_input("Would you like to add headers? (y/n): ").lower().strip()
        headers = {}

        if add_headers == "y":
            while True:
                key = log_input("Header key (leave blank to finish): ").strip()
                if not key:
                    break
                value = log_input(f"Value for '{key}': ").strip()
                headers[key] = value

        result = fetch_api_response(api_url, headers)

        if result is not None:
            log_info("Response:")
            if isinstance(result, dict):
                print(Fore.LIGHTWHITE_EX + json.dumps(result, indent=4, ensure_ascii=False) + Style.RESET_ALL)
            else:
                print(Fore.LIGHTWHITE_EX + str(result) + Style.RESET_ALL)

            save = log_input("Do you want to save the response to a file? (y/n): ").lower().strip()
            if save == "y":
                filename = f"api_response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                with open(filename, "w", encoding="utf-8") as f:
                    if isinstance(result, dict):
                        json.dump(result, f, indent=4, ensure_ascii=False)
                    else:
                        f.write(result)
                log_success(f"Response saved to '{filename}'")
        else:
            log_warn("No data was returned from the API.")

    except KeyboardInterrupt:
        log_exit("Program terminated by user.")

if __name__ == "__main__":
    main()
