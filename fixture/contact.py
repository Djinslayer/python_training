from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

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
        # ввод ФИО
        self.change_field_value('firstname', contact.firstname)
        self.change_field_value('middlename', contact.middlename)
        self.change_field_value('lastname', contact.lastname)
        # ввод никнейма
        self.change_field_value('nickname', contact.nickname)
        # ввод данных о работе и адреса компании
        self.change_field_value('title', contact.tittle)
        self.change_field_value('company', contact.company)
        self.change_field_value('address', contact.address)
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
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # Удалить контакт
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # Подтверждение удаления
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        # Удалить контакт
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # Подтверждение удаления
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_id("%s" % id).click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        # нажатие изменения контакта
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_form(new_contact_data)
        # нажатие изменения контакта
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//*[@href='edit.php?id=%s']" % id).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def modify_first_contact(self):
       self.modify_contact_by_index(0)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name('selected[]'))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                part = element.find_elements_by_tag_name('td')
                id = part[0].find_element_by_tag_name('input').get_attribute("value")
                lastname = part[1].text
                firstname = part[2].text
                address = part[3].text
                all_email = part[4].text
                all_phones = part[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones, address=address,
                                                  all_email_from_home_page=all_email))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name('id').get_attribute("value")
        lastname = wd.find_element_by_name('lastname').get_attribute("value")
        firstname = wd.find_element_by_name('firstname').get_attribute("value")
        address = wd.find_element_by_name('address').get_attribute("value")
        mail1 = wd.find_element_by_name('email').get_attribute("value")
        mail2 = wd.find_element_by_name('email2').get_attribute("value")
        mail3 = wd.find_element_by_name('email3').get_attribute("value")
        home_phone = wd.find_element_by_name('home').get_attribute("value")
        mobile_phone = wd.find_element_by_name('mobile').get_attribute("value")
        work_phone = wd.find_element_by_name('work').get_attribute("value")
        phone2 = wd.find_element_by_name('phone2').get_attribute("value")
        return Contact(id=id, lastname=lastname, firstname=firstname, address=address, mail1=mail1, mail2=mail2,
                       mail3=mail3, home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone,
                       phone2=phone2)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search('M: (.*)', text).group(1)
        work_phone = re.search('W: (.*)', text).group(1)
        phone2 = re.search('P: (.*)', text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, phone2=phone2)

    def add_contact_to_group_by_id(self, id, group):
        self.open_home_page()
        self.select_contact_by_id(id)
        self.add_contact_to_group(group)
        self.open_home_page()
        self.contact_cache = None

    def add_contact_to_group(self, group):
        wd = self.app.wd
        if group is not None:
            wd.find_element_by_name("to_group").click()
            wd.find_element_by_css_selector("select[name='to_group'] [value='%s']" % group).click()
            wd.find_element_by_name("add").click()

    def delete_contact_from_group_by_id(self, group, id):
        self.open_home_page()
        self.delete_contact_to_group(group, id)
        self.open_home_page()
        self.contact_cache = None

    def delete_contact_to_group(self, group, group_and_contact_id):
        wd = self.app.wd
        if group is not None:
            wd.find_element_by_name("group").click()
            wd.find_element_by_css_selector("select[name='group'] option[value='%s']" % group_and_contact_id).click()
            wd.find_element_by_css_selector("td[class='center'] input[type='checkbox']").click()
            wd.find_element_by_name("remove").click()
