"""
E-Hailing Fare Calculator Core Architecture
Module Assignment: Core Architecture & Base Fare Calculation
"""

# ==========================================
# 1. CORE FARE CALCULATION FUNCTION
# ==========================================

def calculate_base_fare(service_type, distance):
    """
    Calculates the base fare based on chosen service type and trip distance.
    
    Service Options:
    1: JustGrab / Economy   -> Base: $3.00, Rate: $1.20/km
    2: GrabCar Premium      -> Base: $5.00, Rate: $2.00/km
    3: GrabBike / Express   -> Base: $2.00, Rate: $0.80/km
    """
    # --- Input Validation for Distance ---
    # Distance must be a positive number (> 0)
    if not isinstance(distance, (int, float)) or distance <= 0:
        raise ValueError("Distance must be a positive number greater than 0.")

    # Initialize variables for base fare and rate per km
    base_fare = 0.0
    rate_per_km = 0.0

    # --- if/elif/else blocks to assign pricing according to service type ---
    # Convert input to string or int comparison to accept options flexibily (e.g., 1 or "1")
    service_str = str(service_type).strip()

    if service_str == "1":
        # Option 1: JustGrab / Economy
        base_fare = 3.00
        rate_per_km = 1.20
    elif service_str == "2":
        # Option 2: GrabCar Premium
        base_fare = 5.00
        rate_per_km = 2.00
    elif service_str == "3":
        # Option 3: GrabBike / Express
        base_fare = 2.00
        rate_per_km = 0.80
    else:
        # Invalid option selected
        raise ValueError("Invalid service type! Please choose 1, 2, or 3.")

    # Core Calculation: Total Base Fare = Base Fee + (Per-Km Rate * Distance)
    total_base_fare = base_fare + (rate_per_km * distance)
    
    return round(total_base_fare, 2)


# ==========================================
# 2. TEAMMATE PLACEHOLDER FUNCTIONS
# ==========================================

def get_surge_multiplier(is_peak):
    """
    [Teammate Placeholder]
    Calculates surge pricing multiplier depending on peak hours.
    
    Parameters:
        is_peak (bool): True if peak hour, False otherwise.
    
    Returns:
        float: Multiplier (e.g., 1.0 for normal, 1.5 for peak)
    """
    # TODO: Teammate to implement peak hour surge multiplier logic here.
    pass


def apply_promo_code(current_fare, promo_code):
    """
    [Teammate Placeholder]
    Applies discount codes to the calculated fare.
    
    Parameters:
        current_fare (float): Current fare before promo.
        promo_code (str): Discount code entered by user.
        
    Returns:
        float: Final fare after applying discount.
    """
    # TODO: Teammate to implement promo code validation and discount logic here.
    pass


def print_receipt(service_name, distance, base_fare, surge_multiplier=1.0, final_fare=None, promo_code=None):
    """
    [Teammate Placeholder]
    Displays a formatted receipt for the user.
    
    Parameters:
        service_name (str): Name of service selected.
        distance (float): Distance in km.
        base_fare (float): Calculated base fare.
        surge_multiplier (float): Surge multiplier applied.
        final_fare (float): Total final cost after promo.
        promo_code (str): Promo code used (optional).
    """
    # TODO: Teammate to implement formatted receipt printing UI here.
    pass


# ==========================================
# 3. HELPER INPUT VALIDATION & USER INTERFACE
# ==========================================

def get_valid_distance():
    """
    Prompts user for distance input and validates that it is a positive float.
    """
    while True:
        try:
            user_input = float(input("Enter trip distance in kilometers (km): "))
            if user_input > 0:
                return user_input
            else:
                print("Error: Distance must be a positive number greater than 0. Please try again.\n")
        except ValueError:
            print("Error: Invalid input! Please enter a valid numerical value for distance.\n")


def get_valid_service_type():
    """
    Prompts user to select a service type (1, 2, or 3).
    """
    print("Available Service Options:")
    print("  1. JustGrab / Economy  (Base: $3.00, Rate: $1.20/km)")
    print("  2. GrabCar Premium     (Base: $5.00, Rate: $2.00/km)")
    print("  3. GrabBike / Express  (Base: $2.00, Rate: $0.80/km)")
    
    while True:
        choice = input("Select service option (1-3): ").strip()
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Error: Invalid choice! Please select 1, 2, or 3.\n")


# ==========================================
# 4. MAIN PROGRAM EXECUTION
# ==========================================

def main():
    print("=======================================")
    print("      E-HAILING FARE CALCULATOR        ")
    print("=======================================")
    
    # Step 1: Input Validation for Service Selection and Distance
    service_choice = get_valid_service_type()
    print()
    distance = get_valid_distance()
    
    # Step 2: Core Base Fare Calculation
    try:
        calculated_fare = calculate_base_fare(service_choice, distance)
        
        # Display initial results
        service_names = {
            "1": "JustGrab / Economy",
            "2": "GrabCar Premium",
            "3": "GrabBike / Express"
        }
        
        print("\n---------------------------------------")
        print(f"Service Selected : {service_names[service_choice]}")
        print(f"Trip Distance    : {distance:.2f} km")
        print(f"Calculated Fare  : ${calculated_fare:.2f}")
        print("---------------------------------------")
        print("Base calculation successful! Ready for teammate integration.")
        
    except ValueError as err:
        print(f"Calculation Error: {err}")


if __name__ == "__main__":
    main()
