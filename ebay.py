from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.ebay.com')

srch_box = driver.find_element(By.ID, 'gh-ac')
srch_box.send_keys('books')
srch_btn = driver.find_element(By.ID, 'gh-btn')
srch_btn.click()

time.sleep(3)

driver.get ("https://www.ebay.com/itm/167233560052?_skw=books&itmmeta=01JGYFD1FZ5VMDMN2BZANFS8XN&hash=item26efe59df4:g:3voAAOSw5xBnen6J&itmprp=enc%3AAQAJAAAA4HoV3kP08IDx%2BKZ9MfhVJKmO9r9m7wlJpxtKvpdi5Mb7LmHk2%2FrIwdLvrLRb9p0xOlEx0TweXqP55of62%2By%2BLe2f4F53xedRV%2Fk7Yjpx8DR1ZDm1NnfNo5QuWWDAvzlpiGyrbeAWOl%2FI5qJ5TNUWfz1aDSPWMwrkfot%2B1eakk6TlaIbrD6VTseLqtklDXS1PF5AzmRR3eHd%2BeaaqBQao7yZ8wv0Qsqra2oXu%2B1gIgUmacC6FczpaL1YF44BodACaOa49aqq3hSQKgAEcJMAekKe9G6Zxp8QcujexUpM8veVN%7Ctkp%3ABFBMhpi0z4dl")

time.sleep(3)
add_to_cart_button = driver.find_element(By.LINK_TEXT,"Add to cart")
add_to_cart_button.click()

time.sleep(3)

cart_icon = driver.find_element(By.ID, 'gh-cart-n')
cart_item_count = cart_icon.text

print(f"Items in Cart: {cart_item_count}")

assert cart_item_count == '1', f"Expected 1 item in the cart, but found {cart_item_count}"

driver.quit()