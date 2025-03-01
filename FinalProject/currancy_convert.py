import tkinter as tk
import json
import requests
import plotly.express as px
import pandas as pd

def get_api_data():
    response = requests.get(f"https://api.currencyfreaks.com/v2.0/rates/latest?apikey=6889cb695a2249c59463e57ec9afa594&base=USD")
    return response.json()

def plot(api_data_in_json):
    rates_dict = api_data_in_json["rates"]
    df = pd.DataFrame(list(rates_dict.items()), columns=["Symbol", "Rate"])
    df["Rate"] = pd.to_numeric(df["Rate"], errors="coerce")
    df = df.sort_values("Rate", ascending=True)
    fig = px.line(x=df["Symbol"], y=df["Rate"], labels={"x": "Symbol", "y": "Rate"})
    fig.show()


def organize_api_data_points(api_data_in_json):
    """
    There are three dicts in the api response, date, base, rates
    We will organize this data into a more readable format
    """
    date_dict_value = api_data_in_json["date"]
    base_dict_value = api_data_in_json["base"]
    dict_of_rates_values = api_data_in_json["rates"]
    return date_dict_value, base_dict_value, dict_of_rates_values

def calculte_converted_amount(current_curancy_amount, wanted_conversion_base_symbol):
    data_points = organize_api_data_points(get_api_data())
    if wanted_conversion_base_symbol in data_points[2]:
        exchange_rate_for_given_curency = data_points[2][wanted_conversion_base_symbol]
        wanted_currancy_cash = float(current_curancy_amount) * float(exchange_rate_for_given_curency)
        return  wanted_currancy_cash
    return None

def change_output(label, current_currency_entry, wanted_base_entry):
    current_currency = current_currency_entry.get().strip()
    wanted_base = wanted_base_entry.get().upper().strip()

    try:
        current_currency_amount = float(current_currency)
    except ValueError:
        label.config(text="Invalid amount")
        return

    converted_amount = calculte_converted_amount(current_currency, wanted_base)

    if converted_amount is not None:
        label.config(text=f"{converted_amount:.2f}")
    else:
        label.config(text="Invalid currency code")


def change_output_calculate_units_away_on_gui(units_away_label, current_currency_entry, wanted_base_entry, guess_units_away):
    current_currency = current_currency_entry.get().strip()
    wanted_base = wanted_base_entry.get().upper().strip()
    guess_units_away = guess_units_away.get().strip()


    converted_amount = calculte_converted_amount(current_currency, wanted_base)

    units_away = abs(converted_amount - float(guess_units_away))


    if converted_amount is not None:
        units_away_label.config(text=f"{units_away:.2f}")
    else:
        units_away_label.config(text="Invalid currency code")



def main():
    # Create main window
    root = tk.Tk()
    root.title("Currency Converter")
    root.geometry("750x250")  # Set window size
    root.configure(bg="#d0d0d0")  # Light background

    # Title Label
    title_label = tk.Label(root, text="Currency Converter", font=("Arial", 14, "bold"), bg="#f4f4f4", fg="#333")
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    guess_title = tk.Label(root, text="Guess What The Output Curancy Will Be!", font=("Arial", 14, "bold"), bg="#f4f4f4", fg="#333")
    guess_title.grid(row=0, column=8, columnspan=2, pady=10)

    # Input Fields
    tk.Label(root, text="Amount in USD:", font=("Arial", 10), bg="#f4f4f4").grid(row=1, column=0, sticky="w", padx=10)
    current_currency_entry = tk.Entry(root, font=("Arial", 10))
    current_currency_entry.grid(row=1, column=1, pady=5, padx=10)

    tk.Label(root, text="Target Currency Code:", font=("Arial", 10), bg="#f4f4f4").grid(row=2, column=0, sticky="w", padx=10)
    wanted_base_entry = tk.Entry(root, font=("Arial", 10))
    wanted_base_entry.grid(row=2, column=1, pady=5, padx=10)

    # Output Label
    tk.Label(root, text="Calculated Conversion:", font=("Arial", 10, "bold"), bg="#f4f4f4").grid(row=3, column=0, sticky="w", padx=10)
    calculated = tk.Label(root, text="N/A", font=("Arial", 10), bg="#fff", relief="sunken", width=18)
    calculated.grid(row=3, column=1, pady=5)

    # @@@Guess Input Fields
    tk.Label(root, text="Enter Guess Whole Number:", font=("Arial", 10), bg="#f4f4f4").grid(row=1, column=8, sticky="w", padx=10)
    guess_input = tk.Entry(root, font=("Arial", 10))
    guess_input.grid(row=1, column=9, pady=5, padx=10)

    tk.Label(root, text="Amount in USD:", font=("Arial", 10), bg="#f4f4f4").grid(row=2, column=8, sticky="w", padx=10)
    current_currency_entry2 = tk.Entry(root, font=("Arial", 10))
    current_currency_entry2.grid(row=2, column=9, pady=5, padx=10)

    tk.Label(root, text="Target Currency Code:", font=("Arial", 10), bg="#f4f4f4").grid(row=3, column=8, sticky="w", padx=10)
    wanted_base_entry2 = tk.Entry(root, font=("Arial", 10))
    wanted_base_entry2.grid(row=3, column=9, pady=5, padx=10)

    # @@@Output Box for Guess
    tk.Label(root, text="Units Away From Actual Value:", font=("Arial", 10, "bold"), bg="#f4f4f4").grid(row=4, column=8, sticky="w", padx=10)
    guess_output = tk.Label(root, text="N/A", font=("Arial", 10), bg="#fff", relief="sunken", width=18)
    guess_output.grid(row=4, column=9, pady=5)

    # Buttons with Styling
    convert_button = tk.Button(root, text="Calculate", command=lambda: change_output(calculated, current_currency_entry, wanted_base_entry))
    convert_button.grid(row=4, column=0, columnspan=2, pady=10)

    #guess button@@@
    guess_button = tk.Button(root, text="Guess", command=lambda: change_output_calculate_units_away_on_gui(guess_output, current_currency_entry2, wanted_base_entry2, guess_input))
    guess_button.grid(row=5, column=9, columnspan=2)

    # Run the application
    plot(get_api_data())
    root.mainloop()


if __name__ == "__main__":
    main()
