"""
E-Hailing Fare Calculator Core Architecture
Integrated Version with Teammate Modules:
- Core Base Fare Calculation (Akisha)
- Surge Pricing & Promo Codes (Mohammad Ali Jomaa)
- Terminal UI & Receipt Display (Jaafar Jomaa)
"""

# ==========================================
# CONSTANTS & CONFIGURATION
# ==========================================
WIDTH = 50          # Total width of banner/menu/receipt line
CURRENCY = "$"      # Currency symbol

SERVICES = [
    ("1", "JustGrab / Economy", "Budget-friendly everyday rides", 3.00, 1.20),
    ("2", "GrabCar Premium",    "Comfortable cars, top-rated drivers", 5.00, 2.00),
    ("3", "GrabBike / Express",   "Priority pickup, fastest route", 2.00, 0.80),
]


def money(amount):
    """Formats a numeric value as currency (e.g., $12.50)."""
    return f"{CURRENCY}{amount:,.2f}"


# ==========================================
# 1. CORE FARE CALCULATION FUNCTION (Akisha)
# ==========================================

def get_service_rates(service_type):
    """Helper to return (service_name, base_fee, rate_per_km) for given service_type."""
    service_str = str(service_type).strip()
    for s_id, s_name, s_desc, base_fee, rate_per_km in SERVICES:
        if service_str == s_id:
            return s_name, base_fee, rate_per_km
    raise ValueError("Invalid service type! Please choose 1, 2, or 3.")


def calculate_base_fare(service_type, distance):
    """
    Calculates the base fare based on chosen service type and trip distance.
    
    Returns:
        tuple: (service_name, base_fee, distance_charge, total_base_fare)
    """
    if not isinstance(distance, (int, float)) or distance <= 0:
        raise ValueError("Distance must be a positive number greater than 0.")

    s_name, base_fee, rate_per_km = get_service_rates(service_type)
    distance_charge = round(rate_per_km * distance, 2)
    total_base_fare = round(base_fee + distance_charge, 2)

    return s_name, base_fee, distance_charge, total_base_fare


# ==========================================
# 2. SURGE PRICING & PROMO CODES (Mohammad Ali Jomaa)
# ==========================================

def get_surge_multiplier(is_peak):
    """
    Calculates surge pricing multiplier depending on peak hours.
    If it's peak hour, apply a 50% rush-hour surge (1.5x).
    Otherwise, normal fare (1.0x).
    """
    if is_peak:
        return 1.5
    else:
        return 1.0


def apply_promo_code(current_fare, promo_code):
    """
    Applies discount codes to the calculated fare.
    - 'WELCOME5': $5.00 off
    - Blank or invalid codes: $0.00 off with status message
    
    Returns:
        tuple: (new_fare, discount_amount, message)
    """
    code = (promo_code or "").strip().upper()

    if code == "WELCOME5":
        discount = 5.00
        message = "Promo applied: $5.00 off!"
    elif code == "":
        discount = 0.00
        message = "No promo code entered."
    else:
        discount = 0.00
        message = "Invalid promo code. (Try WELCOME5)"

    new_fare = max(current_fare - discount, 0.00)
    actual_discount = min(discount, current_fare)
    return round(new_fare, 2), round(actual_discount, 2), message


# ==========================================
# 3. TERMINAL UI & RECEIPT PRINTER (Jaafar Jomaa)
# ==========================================

def show_welcome_banner():
    """Print the welcome banner at the top of the program."""
    border = "=" * WIDTH
    print(border)
    print("E-HAILING".center(WIDTH))
    print("FARE & BOOKING ASSISTANT".center(WIDTH))
    print("~ Safe. Fast. Affordable. ~".center(WIDTH))
    print(border)
    print()


def show_service_menu():
    """Display the ride options and ask the user to pick one."""
    divider = "-" * WIDTH
    print("SELECT YOUR RIDE".center(WIDTH))
    print(divider)

    for s_id, s_name, s_desc, base_fee, rate_per_km in SERVICES:
        print(f" [{s_id}] {s_name:<20} {s_desc}")

    print(divider)

    while True:
        choice = input(f"Enter your choice (1-{len(SERVICES)}): ").strip()
        if choice in [s[0] for s in SERVICES]:
            return choice
        print("Invalid choice. Please try again.")


def print_receipt(service_name, distance, base_fare, distance_charge,
                  surge_amount, discount_amount, final_fare):
    """Print a formatted itemized receipt."""
    thick = "=" * WIDTH
    thin = "-" * WIDTH

    def row(label, value):
        return f"{label:<{WIDTH - 20}}{value:>20}"

    print("\n" + thick)
    print("RIDE RECEIPT".center(WIDTH))
    print(thick)

    print(row("Service:", service_name))
    print(row("Distance:", f"{distance:.1f} km"))
    print(thin)

    print(row("Base fee", money(base_fare)))
    print(row("Distance charge", money(distance_charge)))

    if surge_amount > 0:
        print(row("Surge Charge (1.5x)", "+" + money(surge_amount)))
    else:
        print(row("Surge Charge (1.0x)", money(0.00)))

    if discount_amount > 0:
        print(row("Promo Discount", "-" + money(discount_amount)))
    else:
        print(row("Promo Discount", money(0.00)))

    print(thin)
    print(row("TOTAL FARE", money(final_fare)))
    print(thick)
    print("Thank you for riding with us!".center(WIDTH))
    print(thick + "\n")


# ==========================================
# 4. HELPER INPUT VALIDATORS
# ==========================================

def get_valid_distance():
    """Prompts user for distance input and validates that it is a positive float."""
    while True:
        try:
            user_input = float(input("Enter trip distance in kilometers (km): "))
            if user_input > 0:
                return user_input
            else:
                print("Error: Distance must be a positive number greater than 0. Please try again.\n")
        except ValueError:
            print("Error: Invalid input! Please enter a numerical value for distance.\n")


def get_peak_hour_choice():
    """Prompts user whether it is peak hour (rush hour)."""
    while True:
        choice = input("Is it peak hour / rush hour? (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        print("Please enter 'y' for yes or 'n' for no.\n")


# ==========================================
# 5. MAIN PROGRAM EXECUTION
# ==========================================

def main():
    show_welcome_banner()

    # Step 1: Select Service Option
    service_choice = show_service_menu()

    # Step 2: Input Distance & Peak Hour
    print()
    distance = get_valid_distance()
    is_peak = get_peak_hour_choice()
    
    # Step 3: Input Promo Code
    promo_code = input("Enter promo code (press Enter to skip): ").strip()

    # Step 4: Calculate Fares
    try:
        service_name, base_fee, distance_charge, total_base = calculate_base_fare(service_choice, distance)
        
        # Surge Calculation
        surge_mult = get_surge_multiplier(is_peak)
        fare_after_surge = total_base * surge_mult
        surge_amount = fare_after_surge - total_base
        
        # Promo Code Calculation
        final_fare, discount_amount, promo_msg = apply_promo_code(fare_after_surge, promo_code)

        if promo_msg:
            print(f"\n[Promo Status]: {promo_msg}")

        # Step 5: Display Receipt
        print_receipt(
            service_name=service_name,
            distance=distance,
            base_fare=base_fee,
            distance_charge=distance_charge,
            surge_amount=surge_amount,
            discount_amount=discount_amount,
            final_fare=final_fare
        )

    except ValueError as err:
        print(f"Calculation Error: {err}")


if __name__ == "__main__":
    main()
