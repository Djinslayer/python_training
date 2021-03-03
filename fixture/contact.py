
from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHepler:

    def __init__(self, app):
        self.app = app

    def add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/addressbook/') and
                len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_value2(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # ввод ФИО
        self.change_field_value('firstname', contact.firstname)
        self.change_field_value('middlename', contact.middlename)
        self.change_field_value('lastname', contact.lastname)
        # ввод никнейма
        self.change_field_value('nickname', contact.nickname)
        # ввод данных о работе и адреса компании
        self.change_field_value('title', contact.tittle)
        self.change_field_value('company', contact.company)
        self.change_field_value('address', contact.address_company)
        # ввод телефонных номеров (все, которые есть)
        self.change_field_value('home', contact.home_phone)
        self.change_field_value('mobile', contact.mobile_phone)
        self.change_field_value('work', contact.work_phone)
        self.change_field_value('fax', contact.fax)
        # ввод всех мэйлов
        self.change_field_value('email', contact.mail1)
        self.change_field_value('email2', contact.mail2)
        self.change_field_value('email3', contact.mail3)
        # ввод сайта
        self.change_field_value('homepage', contact.homepage)
        # ввод даты рождения
        self.change_field_value2("bday", contact.bday)
        self.change_field_value2("bmonth", contact.bmonth)
        self.change_field_value('byear', contact.birthday_year)
        # ввод даты anniversary
        self.change_field_value2("aday", contact.aday)
        self.change_field_value2("amonth", contact.amonth)
        self.change_field_value('ayear', contact.anniversary_year)
        # ввод доп адреса
        self.change_field_value('address2', contact.address2)
        self.change_field_value('phone2', contact.phone2)
        self.change_field_value('notes', contact.notes)

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        self.add_new_contact()
        self.fill_contact_form(contact)
        # нажатие кнопки создания контакта
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # Удалить контакт
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # Подтверждение удаления
        wd.switch_to_alert().accept()
        self.return_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # нажать на изменение контакта
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # нажатие изменения контакта
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name('selected[]'))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts_list = []
        for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
            firstname = element.find_element_by_xpath("./td[3]").text
            lastname = element.find_element_by_xpath("./td[2]").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts_list.append(Contact(firstname=firstname, lastname=lastname, id=id))
            return list(self.contacts_list)