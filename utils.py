def validate_budget(budget, price):
    return price <= budget

def display_options(options):
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
