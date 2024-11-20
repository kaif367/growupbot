import re
import requests
from datetime import datetime, timedelta

# Simple banner for Termux
def display_banner():
    print("""
=============================================================================
    ⚡ SIGNAL GENERATOR TOOL FOR BINARY TRADING ⚡          
    Powered by GROWUP TRADING 🎯
    
    TELEGRAM : @GROWUPBINARYTRADING
    ADMIN    : @KaifSaifi001
    SUPPORT  : @Team_GrowUp                    
                                                             
    Use Timezone: UTC +5:30  
=============================================================================
""")

# Currency pairs (OTC)
currency_pairs = [
    ("AUDCAD_otc", "AUD/CAD (OTC)"),
    ("AUDCHF_otc", "AUD/CHF (OTC)"),
    ("EURUSD_otc", "EUR/USD (OTC)"),
    ("GBPUSD_otc", "GBP/USD (OTC)"),
    ("USDJPY_otc", "USD/JPY (OTC)"),
    ("XAUUSD_otc", "Gold (OTC)"),
]

# Dummy user database
USERS = {
    "user1": {"password": "password1", "expire_time": None},
    "user2": {"password": "password2", "expire_time": None},
}

API_URL = "https://alltradingapi.com/signal_list_gen/qx_signal.js"

def login():
    print("\nEnter your login credentials:")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in USERS and USERS[username]["password"] == password:
        USERS[username]["expire_time"] = datetime.now() + timedelta(minutes=30)
        print(f"Login successful! Session expires at {USERS[username]['expire_time']}")
        return username
    else:
        print("Invalid username or password.")
        return None

def check_session(username):
    if username in USERS:
        if datetime.now() > USERS[username]["expire_time"]:
            print("Session expired. Please log in again.")
            return False
        return True
    print("User not logged in.")
    return False

def print_table(signals, api_date):
    """Print the signals in a formatted table"""
    print("="*40)
    print(f"Date: {api_date}")
    print("="*40)
    print(f"| {'Forex Pair':<12} | {'Future Time':<12} | {'Action':<6} |")
    print("-"*40)

    for signal in signals:
        pair = signal['pair']
        time = signal['time']
        action = signal['action']
        print(f"| {pair:<12} | {time:<12} | {action:<6} |")
    print("="*40)

def fetch_signals():
    print("\nEnter signal fetching parameters:")
    pairs = input("Pairs (comma-separated, e.g., EURUSD_otc,USDJPY_otc): ").strip() or "EURUSD_otc,USDJPY_otc"
    start_time = input("Start time (HH:MM, e.g., 09:00): ").strip() or "09:00"
    end_time = input("End time (HH:MM, e.g., 18:00): ").strip() or "18:00"
    days = input("Number of days (default: 3): ").strip() or "3"
    mode = input("Mode (blackout/normal, default: blackout): ").strip() or "blackout"
    min_percentage = input("Minimum percentage (default: 50): ").strip() or "50"
    filter_value = input("Filter value (1 or 2, default: 1): ").strip() or "1"

    params = {
        "pairs": pairs,
        "start_time": start_time,
        "end_time": end_time,
        "days": days,
        "mode": mode,
        "min_percentage": min_percentage,
        "filter": filter_value,
    }

    try:
        print("Fetching signals...")
        response = requests.get(API_URL, params=params)
        response.raise_for_status()

        # Extract signals
        if "Signals:" in response.text:
            signal_lines = response.text.split("\n")
            signals = []

            # Extract the date
            date_match = re.search(r"Date: (\d{2}/\d{2}/\d{4})", response.text)
            api_date = date_match.group(1) if date_match else "Unknown Date"

            # Process signal lines
            for line in signal_lines:
                if "PA～" in line:
                    parts = line.strip().split("～")
                    signals.append({"pair": parts[1], "time": parts[2], "action": parts[3]})

            print_table(signals, api_date)
        else:
            print("No signals found.")

    except Exception as e:
        print(f"Error fetching signals: {e}")

if __name__ == "__main__":
    display_banner()
    username = login()
    if username:
        while check_session(username):
            print("\n1. View Currency Pairs")
            print("2. Fetch Signals")
            print("3. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                print("Available Currency Pairs:")
                for pair, name in currency_pairs:
                    print(f"{pair:<12} --> {name}")
            elif choice == "2":
                fetch_signals()
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")
