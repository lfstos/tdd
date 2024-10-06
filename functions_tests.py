from selenium import webdriver


def function_test():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get('http://localhost:8000')

    assert 'The install worked successfully! Congratulations!' in driver.title


function_test()
