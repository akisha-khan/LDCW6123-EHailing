def get_surge_multiplier(is_peak):
    # If it's peak hour, apply a 50% rush-hour surge
    if is_peak:
        return 1.5
    # Otherwise, normal fare
    else:
        return 1.0


def apply_promo_code(current_fare, promo_code):
    # Clean the input: handle None, strip spaces, ignore case
    code = (promo_code or "").strip().upper()

    # Valid code: $5 off
    if code == "WELCOME5":
        discount = 5.00
        message = "Promo applied: $5.00 off!"
    # Blank code: no discount
    elif code == "":
        discount = 0.00
        message = "No promo code entered."
    # Anything else is invalid
    else:
        discount = 0.00
        message = "Invalid promo code. Try WELCOME5."

    # Fare can never go below $0.00
    new_fare = max(current_fare - discount, 0.00)
    return new_fare, message


# ---- Test calls ----
print(get_surge_multiplier(True))    # 1.5
print(get_surge_multiplier(False))   # 1.0

print(apply_promo_code(20.00, "welcome5"))  # (15.0, 'Promo applied...')
print(apply_promo_code(3.00, "WELCOME5"))   # (0.0, ...) floor at 0
print(apply_promo_code(20.00, "FAKE"))      # (20.0, 'Invalid...')
print(apply_promo_code(20.00, ""))          # (20.0, 'No promo...')
