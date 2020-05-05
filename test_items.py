from selenium.webdriver.common.by import By
from time import sleep

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_contains_add_to_basket_button(browser):
    browser.get(link)
    # A little perversion to satisfy the 4th criterion of the task (see task.txt)
    num_of_buttons = len(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket"))
    assert num_of_buttons > 0, "Oops, can't find 'Add to basket' button!"
    sleep(10)
