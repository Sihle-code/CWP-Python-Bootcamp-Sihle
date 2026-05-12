# traffic

light_color = input("Enter light color (red, yellow, green): ")

if light_color == "red":
    print("Stop! Do not proceed.")
elif light_color == "yellow":
    print("Slow down, prepare to stop.")
elif light_color == "green":
    print("Go! Proceed with caution.")
else:
    print("Invalid light color, please enter red, yellow or green.")