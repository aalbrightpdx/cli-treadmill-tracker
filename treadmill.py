#!/usr/bin/env python3
import datetime
import os
import sys
import csv
from statistics import mean

def calculate_calories(weight_lbs, distance_miles, duration_minutes, incline_percent=5):
    """
    Calculate calories burned.
    MET approximation for 2.2mph walk at 5-6% incline.
    """
    MET = 4.3  # Fixed for now. Could adjust based on incline in future.
    weight_kg = weight_lbs / 2.20462
    hours = duration_minutes / 60
    calories = MET * weight_kg * hours
    return round(calories, 2)

def log_session(logfile, date, weight, duration, distance, calories, total_rise):
    """Log a treadmill session to the CSV file with formatted numbers."""
    with open(logfile, 'a') as f:
        f.write(f"{date},{weight:.1f} lbs,{duration:.1f} min,{distance:.2f} mi,{calories:.0f} cal,{total_rise:.1f} in raise\n")

def main():
    logfile = "treadmill_log.csv"
    print("\U0001F3C3‍♂️ Treadmill Session Logger")

    # Create file and header if not exists
    if not os.path.exists(logfile):
        with open(logfile, 'w') as f:
            f.write("Date,Weight,Duration,Distance,Calories,Front Raise (in)\n")

    while True:
        print("\n--- New Entry ---")
        date_str = input("Date (DD-MM-YYYY, leave blank for today or 'q' to quit): ")
        if date_str.lower() == 'q':
            print("Quitting gracefully. 💚")
            break
        if not date_str:
            date_str = datetime.date.today().strftime("%d-%m-%Y")

        while True:
            weight_input = input("Your weight in lbs (e.g., 180.0, or 'q' to quit): ").strip()
            if weight_input.lower() == 'q':
                print("Quitting gracefully. 💚")
                return
            try:
                weight = float(weight_input)
                break
            except ValueError:
                print("❗ Invalid weight. Please enter a number.")

        while True:
            duration_str = input("Duration (min:sec, or 'q' to quit): ")
            if duration_str.lower() == 'q':
                print("Quitting gracefully. 💚")
                return
            try:
                minutes, seconds = map(int, duration_str.strip().split(":"))
                duration = minutes + seconds / 60
                break
            except ValueError:
                print("❗ Invalid format. Please enter time as minutes:seconds (e.g., 30:15)")

        while True:
            distance_input = input("Distance in miles (e.g., 1.25, or 'q' to quit): ").strip()
            if distance_input.lower() == 'q':
                print("Quitting gracefully. 💚")
                return
            try:
                distance = float(distance_input)
                break
            except ValueError:
                print("❗ Invalid distance. Please enter a number.")

        while True:
            rise_input = input("Front rise in inches (e.g., 3.0, leave blank for 0): ").strip()
            if rise_input.lower() == 'q':
                print("Quitting gracefully. 💚")
                return
            if not rise_input:
                total_rise = 0.0
                break
            try:
                total_rise = float(rise_input)
                break
            except ValueError:
                print("❗ Invalid number. Please enter a number.")

        incline_percent = (total_rise / 48) * 100

        calories = calculate_calories(weight, distance, duration, incline_percent)
        print(f"Estimated calories burned: {calories} cal")

        log_session(logfile, date_str, weight, duration, distance, calories, total_rise)
        print(f"✅ Logged session on {date_str}.")

        again = input("Add another? (y/n/q to quit) [default n]: ").lower()
        if again != 'y':
            print("Quitting gracefully. Bye for now! 💚")
            break

def show_records():
    logfile = "treadmill_log.csv"
    if not os.path.exists(logfile):
        print("❗ No treadmill_log.csv file found yet. Start logging sessions first!")
        sys.exit(1)

    print("\n📋 Last 20 Sessions:")

    try:
        with open(logfile, "r") as f:
            lines = list(csv.reader(f))[1:][-20:]  # Skip header
            weights, times, miles, cals = [], [], [], []
            for row in lines:
                print(", ".join(row))
                weights.append(float(row[1].split()[0]))
                times.append(float(row[2].split()[0]))
                miles.append(float(row[3].split()[0]))
                cals.append(float(row[4].split()[0]))

            print("\n📊 Summary:")
            print(f"Total Time: {sum(times):.1f} min")
            print(f"Total Distance: {sum(miles):.2f} mi")
            print(f"Total Calories: {sum(cals):.0f} cal")
            print(f"Average Weight: {mean(weights):.1f} lbs")
            print(f"Most Recent: {lines[-1][0]}, {lines[-1][1]}, {lines[-1][2]}, {lines[-1][3]}, {lines[-1][4]}")

            # Trend over last 5 entries
            print("\n📈 Trend (Last 5 Sessions):")
            recent_weights = weights[-5:]
            recent_cals = cals[-5:]
            recent_times = times[-5:]
            recent_miles = miles[-5:]

            def trend_arrow(change):
                return "⬆️" if change > 0 else ("⬇️" if change < 0 else "➡️")

            print(f"Weight change: {recent_weights[-1] - recent_weights[0]:+.1f} lbs {trend_arrow(recent_weights[-1] - recent_weights[0])}")
            print(f"Calorie change: {recent_cals[-1] - recent_cals[0]:+.0f} cal {trend_arrow(recent_cals[-1] - recent_cals[0])}")
            print(f"Treadmill time change: {recent_times[-1] - recent_times[0]:+.1f} min {trend_arrow(recent_times[-1] - recent_times[0])}")
            print(f"Distance change: {recent_miles[-1] - recent_miles[0]:+.2f} mi {trend_arrow(recent_miles[-1] - recent_miles[0])}")
    except Exception as e:
        print(f"⚠️ Error reading records: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "records":
        show_records()
    else:
        main()

