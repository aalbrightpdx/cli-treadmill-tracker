# CLI Treadmill Tracker 🏃‍♂️

A simple and friendly Python command-line app to track your treadmill sessions.

## Log your:

🔹Date
🔹Weight (in pounds, decimal allowed, e.g., 180.0)
🔹Duration (minutes:seconds, e.g., 30:15)
🔹Distance (miles, decimal allowed, e.g., 1.25)
🔹Front incline raise (inches, decimal allowed, e.g., 3.0)

It saves each session to a CSV file and shows helpful summaries and trends!

## How to Clone

To download and start using this project:

```bash
git clone git@github.com:aalbrightpdx/cli-treadmill-tracker.git
cd cli-treadmill-tracker
```

If you prefer HTTPS instead of SSH:

```bash
git clone https://github.com/aalbrightpdx/cli-treadmill-tracker.git
cd cli-treadmill-tracker
```

## Usage

Run it like this:

```bash
chmod +x treamill.py

./treadmill.py

or

python3 treadmill.py
```

## To view past sessions and trends:

```bash
python3 treadmill.py records
```

## Notes

    Treadmill length is assumed to be 48 inches (4 feet) for incline calculations.

    Logs are saved in treadmill_log.csv.

    Quit anytime by typing q.

# TODO

- Add automatic calorie adjustments based on incline
- Allow customizing treadmill length
- Export graphs of distance and calories
- GUI version?

## License

MIT License
