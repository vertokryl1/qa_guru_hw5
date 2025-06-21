import os
import time

from selene import browser, have, be


def test_send_and_fill_form():
    browser.open('/')

    # Заполнение полей формы
    browser.element('#firstName').type('Муми')
    browser.element('#lastName').type('Тролль')
    browser.element('#userEmail').type('vertokryl@gmail.com')
    browser.element('[for="gender-radio-3"]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirth').click()
    browser.element('.react-datepicker__month-container').should(be.visible)
    browser.element('.react-datepicker__month-select').should(be.visible).element('[value="6"]').click()
    browser.element('.react-datepicker__year-select').should(be.visible).element('[value="1980"]').click()
    browser.element('.react-datepicker__day--007').click()
    browser.element('#dateOfBirthInput').should(have.value('07 Jul 1980'))
    time.sleep(1)
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('49cb68.jpg'))  # загрузка файла
    browser.element('#currentAddress').type('jrhg5i u5yiuoiyu4 riouyiruyr')
    browser.element('#react-select-3-input').should(be.visible).type('NCR').press_enter()
    browser.element('#react-select-4-input').should(be.visible).type('Delhi').press_enter()
    browser.element('[type="submit"]').press_enter()
    # Проверка данных в таблице
    browser.element('.table').all('td').even.should(have.exact_texts(
        'Муми Тролль', 'vertokryl@gmail.com', 'Other', '1234567890', '07 July,1980', 'Maths', 'Reading', '49cb68.jpg',
        'jrhg5i u5yiuoiyu4 riouyiruyr', 'NCR Delhi'
    ))
