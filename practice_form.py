from datetime import datetime

from selenium import webdriver
from driver_creation import SeleniumLibraryExt
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

class PracticeForm:

    def __init__(self):
        self.dict = None

    
    @staticmethod
    def date_parse(date_dict):
        month = datetime.strptime(date_dict["Month"], "%B")
        day = datetime.strptime(str(date_dict["Day"]), "%d")
        year = datetime.strptime(str(date_dict["Year"]), "%Y")
        date = month.strftime("%m") + "/" + day.strftime("%d") + "/" + year.strftime("%Y")
        return date

    @staticmethod
    def textbox_parse(textbox, input_string):
        textbox.send_keys(Keys.CONTROL + "a")
        textbox.send_keys(input_string)
        textbox.send_keys(Keys.RETURN)

    def retrieve_text_boxes(self):
        self.driver = SeleniumLibraryExt.create_driver()
        label_dict = dict()
        xpaths = list()
        form_1 = self.driver.find_elements_by_xpath("//input[@type='text'][contains(@class,'-2 form-control')]")
        for elem in form_1:
            placeholder = elem.get_attribute('placeholder')
            if "@" in placeholder:
                placeholder = 'Email'
            element_id = elem.get_attribute('id')
            xpath = f"//input[@type='text'][@id='{element_id}']"
            xpaths.append(xpath)
            label_dict[placeholder] = xpath
        form_2 = self.driver.find_element_by_xpath("//textarea")
        placeholder = form_2.get_attribute('placeholder')
        element_id = form_2.get_attribute('id')
        xpath = f"//textarea[@id='{element_id}']"
        label_dict[placeholder] = xpath
        self.dict = label_dict
        print(label_dict)

    def insert_dob(self, date_of_birth):
        self.driver = SeleniumLibraryExt.create_driver()
        textbox_dob = self.driver.find_element_by_xpath("//input[@type='text'][@id='dateOfBirthInput']")
        date = self.date_parse(date_of_birth)
        self.textbox_parse(textbox_dob, date)

    def retrieve_checkboxes(self, input_hobbies):
        self.driver = SeleniumLibraryExt.create_driver()
        checkboxes = self.driver.find_elements_by_xpath("//div[@class='custom-control custom-checkbox "
                                                        "custom-control-inline']//label")
        all_hobbies = list()
        for elem in checkboxes:
            all_hobbies.append(elem.text)
        for elem in input_hobbies:
            if elem in all_hobbies:
                self.driver.find_element_by_xpath(f"//label[contains(text(),'{elem}')]").click()

    def gender_selection(self, gender):
        self.driver = SeleniumLibraryExt.create_driver()
        radio_buttons = self.driver.find_elements_by_xpath("//div[@class='custom-control custom-radio "
                                                           "custom-control-inline']")
        all_genders = list()
        for elem in radio_buttons:
            all_genders.append(elem.text)
        if gender in all_genders:
            self.driver.find_element_by_xpath(f"//label[contains(text(),'{gender}')]").click()

    def fill_textboxes(self, input_data):
        self.driver = SeleniumLibraryExt.create_driver()
        for key in input_data:
            if key in self.dict:
                text_box = self.driver.find_element_by_xpath(self.dict[key])
                text_box.clear()
                text_box.send_keys(input_data[key])

    def select_state(self, state):
        self.driver = SeleniumLibraryExt.create_driver()
        states = list()
        self.driver.find_element_by_xpath("//div[@id='state']//div[@class=' css-1hwfws3']").click()
        states_objects = self.driver.find_elements_by_xpath("//div[contains(@id,'react-select')]")
        for elem in states_objects:
            states.append(elem.text)
        if state in states:
            self.driver.find_element_by_xpath(
                f"//div[contains(@id,'react-select')][contains(text(),'{state}')]").click()

    def select_city(self, chosen_city):
        self.driver = SeleniumLibraryExt.create_driver()
        cities = list()
        self.driver.find_element_by_xpath("//div[contains(text(),'Select City')]").click()
        cities_objects = self.driver.find_elements_by_xpath("//div[contains(@id,'react-select-')]")
        for elem in cities_objects:
            cities.append(elem.text)
        if chosen_city in cities:
            self.driver.find_element_by_xpath(
                f"//div[contains(@id,'react-select')][contains(text(),'{chosen_city}')]").click()

    def input_subjects(self, selected_subjects):
        self.driver = SeleniumLibraryExt.create_driver()
        self.driver.find_element_by_xpath("//div[contains(@class,'subjects-auto-complete__input')]").click()
        textbox = self.driver.find_element_by_xpath("//*[@id='subjectsInput']")
        for elem in selected_subjects:
            textbox.send_keys(elem)
            textbox.send_keys(Keys.RETURN)

    def submit_close(self):
        self.driver = SeleniumLibraryExt.create_driver()
        self.driver.find_element_by_xpath("//button[@id='submit']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[@id='closeLargeModal']").click()