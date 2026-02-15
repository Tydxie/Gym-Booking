from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import os


EMAIL = "LeBobbye@test.com"
PASSWORD = "P@ssword123!"
ADMIN_EMAIL = "admin@test.com"
ADMIN_PW = "admin123"

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

def login():
    email_input = wait.until(ec.presence_of_element_located((By.NAME, "email")))
    email_input.clear()
    email_input.send_keys(EMAIL)

    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(PASSWORD)

    submit_button = wait.until(ec.element_to_be_clickable((By.ID, "submit-button")))
    submit_button.click()

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

def book():
    class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

    bookings = 0
    waitlists = 0
    already_booked = 0

    for card in class_cards:
        day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
        day_title = day_group.find_element(By.TAG_NAME, "h2").text

        if "Tue" in day_title or "Thu" in day_title:

            time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
            if "6:00 PM" in time_text:

                class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

                book_btn = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
                status = book_btn.text
                if "Booked" in status:
                    print(f"{class_name} on {day_title} already booked")
                    already_booked += 1
                    pass
                elif "Waitlisted" in status:
                    print(f"Already in the waitlist for {class_name} on {day_title}")
                    already_booked += 1
                    pass
                else:
                    book_btn.click()
                    wait.until(lambda d: book_btn.text == "Booked")

                    if "Class" in status:
                        print(f"Booked {class_name} on {day_title}")
                        bookings += 1
                    else:
                        print(f"Joined waitlist for {class_name} on {day_title}")
                        waitlists += 1

    my_bookings = driver.find_element(By.CSS_SELECTOR, "a[id='my-bookings-link']")
    my_bookings.click()

    booked_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='booking-card-']")
    waitlist_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='waitlist-card-']")
    booked_classes = 0
    waitlisted_classes = 0

    for card in booked_cards:
        booked_classes += 1

    for card in waitlist_cards:
        waitlisted_classes += 1

    total = bookings + waitlists + already_booked

    print(f"---Booking Summary--- \n"
          f"Classes Booked: {bookings} \n"
          f"Waitlists Joined: {waitlists} \n"
          f"Already booked/waitlisted: {already_booked} \n"
          f"Total Tuesday/Thursday 6pm classes processed: {total}")

    if booked_classes > 0 and booked_classes == bookings:
        print("Booking verified")
    if waitlisted_classes > 0 and waitlisted_classes == waitlists:
        print("Waitlist verified")
    if waitlisted_classes + booked_classes == already_booked or waitlisted_classes + booked_classes == total:
        print("Bookings verified")


def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i+1}")

        try:
            return func()
        except TimeoutException:
            if i == retries -1:
                raise
            time.sleep(1)


driver = webdriver.Chrome(options=chrome_options)

driver.get("https://appbrewery.github.io/gym/")

wait = WebDriverWait(driver,2)

login_button = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

retry(login)



retry(book)