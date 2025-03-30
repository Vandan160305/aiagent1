from selenium import webdriver

def run_login_tests():
    driver = webdriver.Chrome()
    driver.get("http://example.com/login")
    username_field = driver.find_element_by_id("username")
    password_field = driver.find_element_by_id("password")
    username_field.send_keys("valid_username")
    password_field.send_keys("valid_password")
    login_button = driver.find_element_by_link_text("Login")
    login_button.click()
    # Check if redirected to home page
    assert driver.current_url == "http://example.com/homepage"
    driver.quit()

def run_invalid_login():
    driver = webdriver.Chrome()
    driver.get("http://example.com/login")
    username_field = driver.find_element_by_id("username")
    password_field = driver.find_element_by_id("password")
    username_field.send_keys("invalid_username")
    password_field.send_keys("invalid_password")
    login_button = driver.find_element_by_link_text("Login")
    login_button.click()
    # Check for error message
    error_message = driver.find_element_by_id("error_message")
    assert error_message.text == "Invalid credentials."
    driver.quit()

def main():
    run_login_tests()
    run_invalid_login()

if __name__ == "__main__":
    main()