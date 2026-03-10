def calculate_premium(age, vehicle, claims):
    premium = 500  # base premium

    if age < 25:
        premium *= 1.2

    if vehicle.lower() == "sports":
        premium *= 1.3

    if claims > 1:
        premium *= 1.4

    return round(premium, 2)