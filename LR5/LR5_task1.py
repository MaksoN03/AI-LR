# Ймовірності для Play = Yes
P_outlook_rain_yes = 3 / 9
P_humidity_high_yes = 3 / 9
P_wind_strong_yes = 3 / 9
P_yes = 9 / 14

# Ймовірності для Play = No
P_outlook_rain_no = 2 / 5
P_humidity_high_no = 4 / 5
P_wind_strong_no = 3 / 5
P_no = 5 / 14

# Байєсівські обчислення (не нормалізовані)
prob_yes = P_outlook_rain_yes * P_humidity_high_yes * P_wind_strong_yes * P_yes
prob_no = P_outlook_rain_no * P_humidity_high_no * P_wind_strong_no * P_no

# Нормалізація
total = prob_yes + prob_no
normalized_yes = prob_yes / total
normalized_no = prob_no / total

print(f"Ймовірність YES: {normalized_yes:.4f} ({normalized_yes*100:.2f}%)")
print(f"Ймовірність NO: {normalized_no:.4f} ({normalized_no*100:.2f}%)")

if normalized_yes > normalized_no:
    print("Висновок: матч ВІДБУДЕТЬСЯ.")
else:
    print("Висновок: матч НЕ ВІДБУДЕТЬСЯ.")

