import math

def format_wls(wls_value):
    if wls_value >= 100:
        dl = int(wls_value // 100)
        wls = wls_value % 100
        return f"{dl} DL and {math.ceil(wls)} WLS" if wls > 0 else f"{dl} DL"
    else:
        return f"{math.ceil(wls_value)} WLS"

def calculate_stitches(start_tools, convert_stitches=False):
    tools = [0]*13
    tools[0] = start_tools

    while True:
        conversions_possible = False
        new_tools = [0]*13
        max_convert_index = 13 if convert_stitches else 12
        for i in range(max_convert_index):
            conv = tools[i] // 20
            if conv > 0:
                conversions_possible = True
                tools[i] -= conv * 20
                for j in range(13):
                    if j != i:
                        new_tools[j] += conv
        for i in range(13):
            tools[i] += new_tools[i]
        if not conversions_possible:
            break

    return tools[12]

def parse_number(input_str):
    input_str = input_str.strip().lower()
    try:
        if input_str.endswith('k'):
            return int(float(input_str[:-1]) * 1_000)
        elif input_str.endswith('m'):
            return int(float(input_str[:-1]) * 1_000_000)
        else:
            return int(float(input_str))
    except ValueError:
        return None

def main():
    while True:
        start = None
        while start is None or start <= 0:
            start_input = input("Enter the number of starting tools (can use 'k' for thousands, 'm' for millions): ")
            start = parse_number(start_input)
            if start is None or start <= 0:
                print("Please enter a valid positive integer number (e.g., 100k, 25000, 2.5m).")

        try:
            tools_per_wls = float(input("Enter how many tools you can buy per 1 WLS (e.g. 20): "))
            if tools_per_wls <= 0:
                print("Please enter a positive number for tools per WLS.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        try:
            wls_per_200_stitches = float(input("Enter how many WLS you earn by selling 200 stitches: "))
            if wls_per_200_stitches <= 0:
                print("Please enter a positive number for WLS per 200 stitches.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        stitches = calculate_stitches(start_tools=start, convert_stitches=False)
        stitches_per_wls = 200 / wls_per_200_stitches
        wls_earned = stitches / stitches_per_wls

        wls_spent = start / tools_per_wls
        profit = wls_earned - wls_spent

        wls_spent_rounded = math.ceil(wls_spent)
        wls_earned_rounded = math.floor(wls_earned)

        print(f"\nStarting with {start} tools, you get {stitches} stitches after conversions.")
        print(f"You spent {format_wls(wls_spent_rounded)} to buy these tools.")
        print(f"At a selling rate of {wls_per_200_stitches:.2f} WLS per 200 stitches, you would earn approximately {format_wls(wls_earned_rounded)}.")
        print(f"Your profit would be approximately {format_wls(profit if profit > 0 else 0)}.")

        again = input("\nWould you like to run the program again? (y/n): ").strip().lower()
        if again not in ('y', 'yes'):
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
