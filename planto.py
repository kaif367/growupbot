import re
import requests
from datetime import datetime, timedelta
from colorama import Fore, Style, init

def display_banner():
    print(Fore.GREEN + """
=============================================================================

  ██████╗ ██████╗  ██████╗ ██╗    ██╗                                
██╔════╝ ██╔══██╗██╔═══██╗██║    ██║                                
██║  ███╗██████╔╝██║   ██║██║ █╗ ██║                                
██║   ██║██╔══██╗██║   ██║██║███╗██║                                
╚██████╔╝██║  ██║╚██████╔╝╚███╔███╔╝                                
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝                                 
██╗   ██╗██████╗     ███╗   ███╗ ██████╗ ██████╗ ██╗██╗     ███████╗
██║   ██║██╔══██╗    ████╗ ████║██╔═══██╗██╔══██╗██║██║     ██╔════╝
██║   ██║██████╔╝    ██╔████╔██║██║   ██║██████╔╝██║██║     █████╗  
██║   ██║██╔═══╝     ██║╚██╔╝██║██║   ██║██╔══██╗██║██║     ██╔══╝  
╚██████╔╝██║         ██║ ╚═╝ ██║╚██████╔╝██████╔╝██║███████╗███████╗
 ╚═════╝ ╚═╝         ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚══════╝╚══════╝
                                                                                                                                                                       

============================================================================
          TELEGRAM : @GROWUPBINARYTRADING

 ⚡ SIGNAL GENERATOR TOOL FOR BINARY TRADING ⚡          
            Powered by GROWUP TRADING 🎯
            ADMIN TELEGRAM : @KaifSaifi001
            Telegram Channel : @GrowupBinaryTrading 
            Bot Telegram Channel : @GrowupBinaryBot
            Support Team : @Team_GrowUp                    
                                                             
          Current Features:                                              
        - Signal Generation with Advance Strategies       
        - Interactive Menu                                  
                                                             
        ⏱ Use Timezone: UTC +5:30  

============================================================================
""")


# Initialize colorama
init(autoreset=True)

# List of currency pairs (OTC)
currency_pairs = [
    ("AUDCAD_otc", "AUD/CAD (OTC)"),
    ("AUDCHF_otc", "AUD/CHF (OTC)"),
    ("AUDJPY_otc", "AUD/JPY (OTC)"),
    ("AUDNZD_otc", "AUD/NZD (OTC)"),
    ("AUDUSD_otc", "AUD/USD (OTC)"),
    ("EURUSD_otc", "EUR/USD (OTC)"),
    ("EURGBP_otc", "EUR/GBP (OTC)"),
    ("EURJPY_otc", "EUR/JPY (OTC)"),
    ("EURNZD_otc", "EUR/NZD (OTC)"),
    ("EURSGD_otc", "EUR/SGD (OTC)"),
    ("EURAUD_otc", "EUR/AUD (OTC)"),
    ("EURCAD_otc", "EUR/CAD (OTC)"),
    ("EURCHF_otc", "EUR/CHF (OTC)"),
    ("GBPUSD_otc", "GBP/USD (OTC)"),
    ("GBPAUD_otc", "GBP/AUD (OTC)"),
    ("GBPCAD_otc", "GBP/CAD (OTC)"),
    ("GBPCHF_otc", "GBP/CHF (OTC)"),
    ("GBPJPY_otc", "GBP/JPY (OTC)"),
    ("GBPNZD_otc", "GBP/NZD (OTC)"),
    ("NZDCAD_otc", "NZD/CAD (OTC)"),
    ("NZDCHF_otc", "NZD/CHF (OTC)"),
    ("NZDJPY_otc", "NZD/JPY (OTC)"),
    ("USDCAD_otc", "USD/CAD (OTC)"),
    ("USDCHF_otc", "USD/CHF (OTC)"),
    ("USDCOP_otc", "USD/COP (OTC)"),
    ("USDDZD_otc", "USD/DZD (OTC)"),
    ("USDEGP_otc", "USD/EGP (OTC)"),
    ("USDIDR_otc", "USD/IDR (OTC)"),
    ("USDINR_otc", "USD/INR (OTC)"),
    ("USDJPY_otc", "USD/JPY (OTC)"),
    ("USDMXN_otc", "USD/MXN (OTC)"),
    ("USDNGN_otc", "USD/NGN (OTC)"),
    ("USDPHP_otc", "USD/PHP (OTC)"),
    ("USDPKR_otc", "USD/PKR (OTC)"),
    ("USDTRY_otc", "USD/TRY (OTC)"),
    ("USDZAR_otc", "USD/ZAR (OTC)"),
]

# List of stocks and indices (non-OTC)
stocks_and_indices = [
    ("AXJAUD", "S&P/ASX 200"),
    ("AXP_otc", "American Express (OTC)"),
    ("BA_otc", "Boeing Company (OTC)"),
    ("BRLUSD_otc", "USD/BRL (OTC)"),
    ("BTCUSD_otc", "Bitcoin (OTC)"),
    ("CADCHF_otc", "CAD/CHF (OTC)"),
    ("CADJPY_otc", "CAD/JPY (OTC)"),
    ("CHFJPY_otc", "CHF/JPY (OTC)"),
    ("CHIA50", "FTSE China A50 Index"),
    ("DJIUSD", "Dow Jones"),
    ("F40EUR", "CAC 40"),
    ("FB_otc", "FACEBOOK INC (OTC)"),
    ("FTSGBP", "FTSE 100"),
    ("HSIHKD", "Hong Kong 50"),
    ("IBXEUR", "IBEX 35"),
    ("INTC_otc", "Intel (OTC)"),
    ("IT4EUR", "Italy 40"),
    ("JNJ_otc", "Johnson & Johnson (OTC)"),
    ("JPXJPY", "Nikkei 225"),
    ("MCD_otc", "McDonald's (OTC)"),
    ("MSFT_otc", "Microsoft (OTC)"),
    ("NDXUSD", "NASDAQ 100"),
    ("PFE_otc", "Pfizer Inc (OTC)"),
    ("STXEUR", "EURO STOXX 50"),
    ("UKBrent_otc", "UKBrent (OTC)"),
    ("USCrude_otc", "USCrude (OTC)"),
    ("XAGUSD_otc", "Silver (OTC)"),
    ("XAUUSD_otc", "Gold (OTC)"),
]
# Function to display currency pairs and stocks
def display_pairs():
    print(Fore.GREEN + "📈 Available Currency Pairs (OTC):" + Style.RESET_ALL)
    for pair, name in currency_pairs:
        print(f"{Fore.YELLOW}{pair:<15} {Fore.CYAN}--> {name}")
    
    print(Fore.GREEN + "\n📈 Available Stocks and Indices:" + Style.RESET_ALL)
    for stock, name in stocks_and_indices:
        print(f"{Fore.YELLOW}{stock:<15} {Fore.CYAN}--> {name}")

# Function to display currency pairs and stocks
def display_pairs():
    print(Fore.GREEN + "📈 Available Currency Pairs (OTC):" + Style.RESET_ALL)
    for pair, name in currency_pairs:
        print(f"{Fore.YELLOW}{pair:<15} {Fore.CYAN}--> {name}")
    
    print(Fore.GREEN + "\n📈 Available Stocks and Indices:" + Style.RESET_ALL)
    for stock, name in stocks_and_indices:
        print(f"{Fore.YELLOW}{stock:<15} {Fore.CYAN}--> {name}")

# Dummy user database
USERS = {
    "user1": {"password": "password1", "expire_time": None},
    "user2": {"password": "password2", "expire_time": None}
}

API_URL = "https://alltradingapi.com/signal_list_gen/qx_signal.js"

def login():
    print(Fore.CYAN + "\nEnter your login credentials:" + Style.RESET_ALL)
    username = input(Fore.YELLOW + "Enter username: " + Style.RESET_ALL).strip()
    password = input(Fore.YELLOW + "Enter password: " + Style.RESET_ALL).strip()

    if username in USERS and USERS[username]["password"] == password:
        USERS[username]["expire_time"] = datetime.now() + timedelta(minutes=30)
        print(Fore.GREEN + f"Login successful! Session expires at {USERS[username]['expire_time']}" + Style.RESET_ALL)
        return username
    else:
        print(Fore.RED + "Invalid username or password." + Style.RESET_ALL)
        return None

def check_session(username):
    if username in USERS:
        if datetime.now() > USERS[username]["expire_time"]:
            print(Fore.RED + "Session expired. Please log in again." + Style.RESET_ALL)
            return False
        return True
    print(Fore.RED + "User not logged in." + Style.RESET_ALL)
    return False

def convert_to_indian_time(signal_time):
    """Converts UTC +6:00 time to Indian Standard Time (IST) which is UTC +5:30"""
    utc_time = datetime.strptime(signal_time, "%H:%M")
    indian_time = utc_time - timedelta(hours=0, minutes=30)  # Subtract 30 minutes from UTC +6 to convert to IST (UTC +5:30)
    return indian_time.strftime("%H:%M")

def print_table(signals, api_date):
    """Print the signals in a formatted table"""
    print(Fore.GREEN + "="*40 + Style.RESET_ALL)
    print(Fore.CYAN + "╔══════════════✰══════════════╗" + Style.RESET_ALL)
    print(Fore.YELLOW + f"⏱️ TIMEZONE: UTC +5:30" + Style.RESET_ALL)
    print(Fore.CYAN + f" 🇮🇳 @Growupbinarytrading" + Style.RESET_ALL)
    print(Fore.GREEN + f"Date: {api_date}" + Style.RESET_ALL)
    print(Fore.CYAN + "╚══════════════✰══════════════╝" + Style.RESET_ALL)
    print(Fore.GREEN + "="*40 + Style.RESET_ALL)

    # Print the table headers
    print(Fore.GREEN + "+------------+------------------+--------+" + Style.RESET_ALL)
    print(f"| {Fore.YELLOW}Forex Pair{Style.RESET_ALL} | {Fore.YELLOW}Future Time{Style.RESET_ALL} | {Fore.YELLOW}Action{Style.RESET_ALL} |")
    print(Fore.GREEN + "+------------+------------------+--------+" + Style.RESET_ALL)

    # Print the signal data in table format
    for signal in signals:
        pair = signal['pair']
        time = signal['time']
        action = signal['action']
        color = Fore.RED if action == "CALL" else Fore.GREEN

        print(f"| {pair:<12} | {time} | {color}{action}{Style.RESET_ALL} |")
    
    print(Fore.GREEN + "+------------+------------------+--------+" + Style.RESET_ALL)
    print(Fore.GREEN + "="*40 + Style.RESET_ALL)

def fetch_signals():
    print(Fore.CYAN + "\nEnter signal fetching parameters:" + Style.RESET_ALL)
    pairs = input(Fore.YELLOW + "Enter pairs (comma-separated, e.g., BRLUSD_otc,USDPKR_otc): " + Style.RESET_ALL).strip() or "BRLUSD_otc,USDPKR_otc"
    start_time = input(Fore.YELLOW + "Enter start time (HH:MM, e.g., 09:00): " + Style.RESET_ALL).strip() or "09:00"
    end_time = input(Fore.YELLOW + "Enter end time (HH:MM, e.g., 18:00): " + Style.RESET_ALL).strip() or "18:00"
    days = input(Fore.YELLOW + "Enter number of days (default: 3): " + Style.RESET_ALL).strip() or "3"
    mode = input(Fore.YELLOW + "Enter mode (blackout/normal, default: blackout): " + Style.RESET_ALL).strip() or "blackout"
    min_percentage = input(Fore.YELLOW + "Enter minimum percentage (default: 50): " + Style.RESET_ALL).strip() or "50"
    filter_value = input(Fore.YELLOW + "Enter filter value (1 or 2, default: 1): " + Style.RESET_ALL).strip() or "1"
    separate = input(Fore.YELLOW + "Separate results by trend? (1 for yes, default: 1): " + Style.RESET_ALL).strip() or "1"

    params = {
        "pairs": pairs,
        "start_time": start_time,
        "end_time": end_time,
        "days": days,
        "mode": mode,
        "min_percentage": min_percentage,
        "filter": filter_value,
        "separate": separate
    }

    try:
        print(Fore.GREEN + "\nFetching signals..." + Style.RESET_ALL)
        response = requests.get(API_URL, params=params)
        response.raise_for_status()

        # Hide the raw response and only focus on processed signals
        if "Signals:" in response.text:
            signal_lines = response.text.split("\n")
            signals = []

            # Extract the date from the raw response
            date_match = re.search(r"Date: (\d{2}/\d{2}/\d{4})", response.text)
            api_date = date_match.group(1) if date_match else "Unknown Date"

            # Process each line to extract signals
            for line in signal_lines:
                if "PA～" in line:
                    parts = line.strip().split("～")
                    pair = parts[1]
                    time_utc = parts[2]
                    signal_type = parts[3] if len(parts) > 3 else None
                    
                    # Convert to IST (UTC +6 -> UTC +5:30)
                    time_ist = convert_to_indian_time(time_utc)

                    if "blackout" in mode.lower():
                        # Blackout mode (No CALL/PUT action)
                        signals.append({"pair": pair, "time": time_ist, "action": "N/A"})
                    else:
                        # Normal mode with CALL/PUT actions
                        action = signal_type.upper() if signal_type else "N/A"
                        signals.append({"pair": pair, "time": time_ist, "action": action})

            if signals:
                print_table(signals, api_date)
            else:
                print(Fore.RED + "No signals found that meet the criteria." + Style.RESET_ALL)
        else:
            print(Fore.RED + "No signals found in the response." + Style.RESET_ALL)

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error occurred while fetching signals: {e}" + Style.RESET_ALL)

# Add the option to display the pairs in your main menu
def main():
    display_banner()
    username = login()

    if username:
        while True:
            if not check_session(username):
                break

            print(Fore.GREEN + "\n1. Fetch Signals" + Style.RESET_ALL)
            print(Fore.GREEN + "2. Show Available Pairs" + Style.RESET_ALL)  # New option to show pairs
            print(Fore.GREEN + "3. Logout" + Style.RESET_ALL)

            choice = input(Fore.YELLOW + "Enter your choice: " + Style.RESET_ALL).strip()

            if choice == "1":
                fetch_signals()
            elif choice == "2":
                # Show currency pairs and stocks separately
                display_pairs()
            elif choice == "3":
                print(Fore.GREEN + "Logging out..." + Style.RESET_ALL)
                USERS[username]["expire_time"] = None
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
