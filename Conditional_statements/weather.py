#  Weather Decision Maker:
is_sunny = input("Is it sunny? (yes/no): ").lower() == "yes"
is_windy = input("Is it windy? (yes/no): ").lower() == "yes"
is_raining = input("Is it raining? (yes/no): ").lower() == "yes"

if is_raining and is_windy:
    print("Stay home! It's raining and windy outside.")
elif is_raining and not is_windy:
    print("Carry an umbrella if you must go out.")
elif is_sunny and is_windy and not is_raining:
    print("Great day to go outside, but it's a bit windy!")
elif is_sunny and not is_windy and not is_raining:
    print("Perfect weather! Go outside and enjoy!")
elif is_windy and not is_raining:
    print("It's windy but dry, a jacket should do!")
else:
    print("Weather is neutral, should be fine to go outside!")