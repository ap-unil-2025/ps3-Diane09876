
def celsius_to_fahrenheit(celsius):
  
    try:
        return round((float(celsius) * 9/5) + 32, 2)
    except ValueError:
        print("Invalid input: please enter a number.")
        return None


def fahrenheit_to_celsius(fahrenheit):
   
    try:
        return round((float(fahrenheit) - 32) * 5/9, 2)
    except ValueError:
        print("Invalid input: please enter a number.")
        return None


def temperature_converter():
  
    try:
        temp = float(input("Enter temperature value: "))
        unit = input("Enter current unit (C/F): ").strip().upper()

        if unit == "C":
            converted = celsius_to_fahrenheit(temp)
            print(f"{temp}°C = {converted}°F")
        elif unit == "F":
            converted = fahrenheit_to_celsius(temp)
            print(f"{temp}°F = {converted}°C")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Please enter a valid numeric value for temperature.")



if __name__ == "__main__":
    print("Running tests...")
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"
    print("All tests passed!\n")

    
    temperature_converter()





