🏋️ Gym Class Auto-Booking Bot (Selenium)

This Python script automates logging into a gym scheduling website and booking specific classes using Selenium.

It scans available classes, filters by day and time, books open spots, joins waitlists if needed, and verifies booking results.

🚀 Features

Automated login with Selenium

Filters classes by:

Days (Tuesday & Thursday)

Time (6:00 PM)

Automatically:

Books available classes

Joins waitlists when full

Skips already booked classes

Booking verification summary

Retry logic for unstable page loads

🧰 Tech Stack

Python 3

Selenium WebDriver

Chrome browser

📦 Requirements

Install dependencies:

pip install selenium


Download ChromeDriver that matches your Chrome version:

https://chromedriver.chromium.org/downloads

Make sure chromedriver is in your PATH or project folder.

▶️ How It Works

Opens Chrome with a persistent user profile

Logs into the gym booking site

Scans all class cards

Filters:

Tuesday & Thursday

6:00 PM classes

Clicks Book or Waitlist automatically

Verifies bookings in "My Bookings"

🧪 Example Output
Booked Yoga Flow on Tue
Joined waitlist for HIIT on Thu
---Booking Summary---
Classes Booked: 1
Waitlists Joined: 1
Already booked/waitlisted: 2
Total Tuesday/Thursday 6pm classes processed: 4
Booking verified

⚠️ Credentials

Credentials are currently hardcoded for testing purposes:

EMAIL = "example@test.com"
PASSWORD = "password"


⚠️ For production or public repos, use environment variables or .env files instead.

📁 Project Structure
GymBooking/
│
├── main.py
├── chrome_profile/
└── .venv/

🛠 Possible Improvements

Use environment variables for secrets

Add headless mode

Add logging instead of print statements

Support dynamic time/day filters

Add scheduling (cron/task scheduler)

📌 Disclaimer

This script is for educational and personal automation purposes only.
