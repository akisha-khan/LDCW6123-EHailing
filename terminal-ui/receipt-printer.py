"""Terminal UI and receipt display module for the E-Hailing Fare Calculator."""

# ---------------------------------------------------------------------------
# Settings you can tweak in one place
# ---------------------------------------------------------------------------
WIDTH = 50          # Total width of every banner / menu / receipt line
CURRENCY = "$"      # Change to "RM", "AED ", etc. if needed

# The three ride options: (name, short description)
SERVICES = [
    ("Economy", "Budget-friendly everyday rides"),
    ("Premium", "Comfortable cars, top-rated drivers"),
    ("Express", "Priority pickup, fastest route"),
]


def money(amount):
    """Turn a number into text like '$12.50'.

    In an f-string, the part after the colon is a "format spec":
      ,    -> adds thousands separators (1,234.50)
      .2f  -> show exactly 2 digits after the decimal point (f = float)
    """
    return f"{CURRENCY}{amount:,.2f}"


def show_welcome_banner():
    """Print the welcome banner at the top of the program."""
    # Multiplying a string repeats it: "=" * 5 gives "=====".
    # This is the easiest way to draw a divider line of any length.
    border = "=" * WIDTH

    # .center(WIDTH) pads a string with spaces on both sides so the text
    # sits in the middle of a line that is WIDTH characters wide.
    print(border)
    print("E-HAILING".center(WIDTH))
    print("FARE & BOOKING ASSISTANT".center(WIDTH))
    print("~ Safe. Fast. Affordable. ~".center(WIDTH))
    print(border)
    print()  # An empty print() outputs a blank line for spacing


def show_service_menu():
    """Display the 3 ride options and ask the user to pick one.

    Returns the chosen service name (e.g. "Economy").
    """
    divider = "-" * WIDTH

    print("SELECT YOUR RIDE".center(WIDTH))
    print(divider)

    # enumerate(SERVICES, start=1) gives us a counter (1, 2, 3) together
    # with each item, so we can number the menu automatically.
    for number, (name, description) in enumerate(SERVICES, start=1):
        # Inside an f-string, {name:<10} means "left-align the text and pad
        # it with spaces until it is 10 characters wide". That keeps the
        # descriptions lined up in a neat column.
        print(f" [{number}] {name:<10} {description}")

    print(divider)

    # Keep asking until the user types a valid number (input validation).
    while True:
        choice = input(f"Enter your choice (1-{len(SERVICES)}): ").strip()

        # .isdigit() checks the text contains only digits, so int() is safe.
        if choice.isdigit() and 1 <= int(choice) <= len(SERVICES):
            # Lists start counting at 0, but the menu starts at 1, so -1.
            service_name = SERVICES[int(choice) - 1][0]
            print(f"You selected: {service_name}\n")
            return service_name

        print("Invalid choice. Please try again.")


def print_receipt(service_name, distance, base_fare, distance_charge,
                  surge_amount, discount_amount, final_fare):
    """Print a formatted receipt.

    Amounts are shown as positive numbers; surge is displayed with a '+'
    and the discount with a '-' so the maths is easy to follow.
    """
    thick = "=" * WIDTH   # Heavy divider for the top, bottom and total
    thin = "-" * WIDTH    # Light divider between sections

    # How it works: every row has a left label and a right value. We give
    # the label a fixed width and right-align the value so all the
    # numbers line up on the right edge, like a real receipt.
    #   {label:<30}  -> left-align label in a 30-character space
    #   {value:>20}  -> right-align value in a 20-character space
    # 30 + 20 = 50, which matches WIDTH. This helper avoids repeating it.
    def row(label, value):
        return f"{label:<{WIDTH - 20}}{value:>20}"

    print(thick)
    print("RIDE RECEIPT".center(WIDTH))
    print(thick)

    print(row("Service:", service_name))
    print(row("Distance:", f"{distance:.1f} km"))   # .1f = 1 decimal place
    print(thin)

    print(row("Base fare", money(base_fare)))
    print(row("Distance charge", money(distance_charge)))
    print(row("Surge", "+" + money(surge_amount)))
    print(row("Discount", "-" + money(discount_amount)))

    print(thin)
    print(row("TOTAL", money(final_fare)))
    print(thick)
    print("Thank you for riding with us!".center(WIDTH))
    print(thick)


# ---------------------------------------------------------------------------
# Quick demo: runs only when you execute this file directly
# (not when another module imports it).
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    show_welcome_banner()
    service = show_service_menu()
    print_receipt(service, 8.5, 3.00, 10.20, 2.50, 1.20, 14.50)