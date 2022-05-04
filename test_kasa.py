import time
import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class KasaTests(unittest.TestCase):

    def setUp(self):
        # Assigning selenium to geckodriver so that the test will be performed on firefox
        self.driver = webdriver.Firefox(executable_path="C:\Webdrivers\geckodriver.exe")
        # Calling kasa url
        self.driver.get("https://kasa.com/")
        # Maximizing browser window
        self.driver.maximize_window()
        # waiting for cookie setting to get popup and if they then accept
        if self.driver.find_element(by=By.CSS_SELECTOR, value=".cookies-container__wrapper"):
            self.driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Accept all ')]").click()
        # wait for sign up modal to popup
        time.sleep(10)
        # press esc key globally to browser to dismiss sign up modal
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        # wait to load search widget
        time.sleep(2)

    def test_search_locations(self):
        for i in range(3):
            # listing 3 location choices which also includes Austin
            location_choices = ["Arlington, TX", "Austin, TX", "Chicago, IL"]
            location = self.driver.find_element(by=By.ID, value="full-screen-hero-search-input")
            # assign location choices to search input,
            # we can also use random.choice(location_choices) to randomly choose a location
            # from given list but here preferred it to be sequence as we are testing, just preferred a consistent result
            location.send_keys(location_choices[i], Keys.ENTER)
            # calculating current date
            current_date = datetime.datetime.today()
            print(current_date)
            # calculating next day using timedelta
            nextday_date = datetime.datetime.today() + datetime.timedelta(days=1)
            print(nextday_date)
            # calculating current day + 3 days using timedelta
            current_plusthree_date = datetime.datetime.today() + datetime.timedelta(days=3)
            print(current_plusthree_date)
            # Check in date always would be today + 1
            check_in = self.driver.find_element(by=By.ID, value="full-screen-hero-check-in-input")
            check_in.send_keys(nextday_date.strftime('%m/%d/%Y'))
            # check out date always would be selected check in date + 2
            check_out = self.driver.find_element(by=By.ID, value="full-screen-hero-check-out-input")
            check_out.send_keys(current_plusthree_date.strftime('%m/%d/%Y'))
            # Click on search button
            self.driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Search')]").click()
            self.driver.get("https://kasa.com/")


    def test_single_night_stay(self):
        for i in range(3):
            # listing 3 location choices which also includes Austin
            location_choices = ["Arlington, TX", "Austin, TX", "Chicago, IL"]
            location = self.driver.find_element(by=By.ID, value="full-screen-hero-search-input")
            # assign location choices to search input,
            # we can also use random.choice(location_choices) to randomly choose a location
            # from given list but here preferred it to be sequence as we are testing, just preferred a consistent result
            location.send_keys(location_choices[i], Keys.ENTER)
            # calculating current date
            current_date = datetime.datetime.today()
            print(current_date)
            # calculating next day using timedelta
            nextday_date = datetime.datetime.today() + datetime.timedelta(days=1)
            print(nextday_date)
            # calculating current day + 2 days using timedelta
            current_plustwo_date = datetime.datetime.today() + datetime.timedelta(days=2)
            print(current_plustwo_date)
            # Check in date always would be today + 1
            check_in = self.driver.find_element(by=By.ID, value="full-screen-hero-check-in-input")
            check_in.send_keys(nextday_date.strftime('%m/%d/%Y'))
            # check out date always would be selected check in date + 1
            check_out = self.driver.find_element(by=By.ID, value="full-screen-hero-check-out-input")
            check_out.send_keys(current_plustwo_date.strftime('%m/%d/%Y'))
            # Click on search button
            self.driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Search')]").click()
            # Implicitly wait until you see property_card/s
            self.driver.implicitly_wait(10)
            self.driver.find_element(by=By.CLASS_NAME, value="property-card__content")
            try:
                # try looking for the class that contains text "Minimum 2 nights stay"
                self.driver.find_element(by=By.XPATH, value="//div[@class='property-card__inner-wrapper']/p")
                # Method 1 to match exact_text: Downside here would be there are other texts that aren't
                # Allowing to stay 1 night which includes "This property has no availability from X to Y."
                # So i went to simple solution by just checking in if class exists
                """try:
                    # use assert function to match actual_text with expected_text
                    assert property_card.text == 'Minimum 2-night stays at this property.'
                    print("Minimum 2 nights stay")
                except AssertionError:
                    print("Assertion failed. Actual value is %s" % property_card.text)"""
                # Method 2
                print("Minimum 2 nights stay")
            except:
                # print if class that contains text "Minimum 2 nights stay" not found
                print("Can stay for 1 night")
            self.driver.get("https://kasa.com/")

    def test_future_date_bookings(self):
        # wait to load search widget
        # Taking location choice here as Arlington, TX
        location_choices = ["Arlington, TX"]
        location = self.driver.find_element(by=By.ID, value="full-screen-hero-search-input")
        # assign location choice to search input,
        location.send_keys(location_choices, Keys.ENTER)

        current_date = datetime.datetime.today()
        print(current_date)
        previous_date = datetime.datetime.today() - datetime.timedelta(days=1)
        print(previous_date)
        nextday_date = datetime.datetime.today() + datetime.timedelta(days=1)
        print(nextday_date)
        # calculating current day + 2 days using timedelta
        current_plustwo_date = datetime.datetime.today() + datetime.timedelta(days=2)
        print(current_plustwo_date)
        # set check in date to be previous day
        check_in = self.driver.find_element(by=By.ID, value="full-screen-hero-check-in-input")
        check_in.send_keys(previous_date.strftime('%m/%d/%Y'))
        # set check out date to be today
        check_out = self.driver.find_element(by=By.ID, value="full-screen-hero-check-out-input")
        check_out.send_keys(current_date.strftime('%m/%d/%Y'))
        time.sleep(2)
        # Click on search button
        self.driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Search')]").click()
        self.driver.implicitly_wait(10)
        # should display Enter valid dates error
        self.driver.find_element(by=By.XPATH, value="//p[@id='full-screen-hero-invalid-dates-error']")
        # now set check in date to be current day
        check_in.clear()
        check_in.send_keys(current_date.strftime('%m/%d/%Y'))
        # now set check out date to be next day
        check_out.clear()
        check_out.send_keys(nextday_date.strftime('%m/%d/%Y'))
        time.sleep(2)
        # Click on search button
        self.driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Search')]").click()
        self.driver.implicitly_wait(10)
        # should still display Enter valid dates error
        self.driver.find_element(by=By.XPATH, value="//p[@id='full-screen-hero-invalid-dates-error']")
        # now set check in date to be next day
        check_in.clear()
        check_in.send_keys(nextday_date.strftime('%m/%d/%Y'))
        # now set check out date to be next day + 1
        check_out.clear()
        check_out.send_keys(current_plustwo_date.strftime('%m/%d/%Y'))
        time.sleep(2)
        # Click on search button
        self.driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Search')]").click()
        # check we show up property cards as the check in and check out dates are future
        self.driver.find_element(by=By.CLASS_NAME, value="property-card__content")

    def test_heating_amenity(self):
        for i in range(3):
            # listing 3 location choices which also includes Austin
            location_choices = ["Arlington, TX", "Austin, TX", "Chicago, IL"]
            location = self.driver.find_element(by=By.ID, value="full-screen-hero-search-input")
            # assign location choices to search input,
            # we can also use random.choice(location_choices) to randomly choose a location
            # from given list but here preferred it to be sequence as we are testing, just preferred a consistent result
            location.send_keys(location_choices[i], Keys.ENTER)
            # calculating current date
            current_date = datetime.datetime.today()
            print(current_date)
            # calculating next day using timedelta
            nextday_date = datetime.datetime.today() + datetime.timedelta(days=1)
            print(nextday_date)
            # calculating current day + 2 days using timedelta
            current_plustwo_date = datetime.datetime.today() + datetime.timedelta(days=2)
            print(current_plustwo_date)
            # Check in date always would be today + 1
            check_in = self.driver.find_element(by=By.ID, value="full-screen-hero-check-in-input")
            check_in.send_keys(nextday_date.strftime('%m/%d/%Y'))
            # check out date always would be selected check in date + 1
            check_out = self.driver.find_element(by=By.ID, value="full-screen-hero-check-out-input")
            check_out.send_keys(current_plustwo_date.strftime('%m/%d/%Y'))
            # Click on search button
            self.driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Search')]").click()
            # Implicitly wait until you see property_card/s
            self.driver.implicitly_wait(10)
            self.driver.find_element(by=By.CLASS_NAME, value="property-card__content")
            # try looking for the class that contains text "Minimum 2 nights stay"
            amenities = self.driver.find_elements(by=By.CLASS_NAME, value="priority-amenities__list-item")
            for amenity in amenities:
                if amenity == 'Heating':
                    print("Has Heating")
                else:
                    print("No Heating")
            self.driver.get("https://kasa.com/")

    def tearDown(self):
        self.driver.quit()