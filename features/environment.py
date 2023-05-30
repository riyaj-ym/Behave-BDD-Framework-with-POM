import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utilities import ConfigReader


def before_scenario(context, driver):
    browser = ConfigReader.readConfiguration("basic info", "browser")

    if browser.__eq__("chrome"):
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager

        ser_obj = Service(ChromeDriverManager().install())
        ops = webdriver.ChromeOptions()
        # ops.add_argument("--headless")
        ops.add_experimental_option("detach", True)
        context.driver = webdriver.Chrome(service=ser_obj, options=ops)

    elif browser.__eq__("edge"):
        from selenium.webdriver.edge.service import Service
        from webdriver_manager.microsoft import EdgeChromiumDriverManager

        ser_obj = Service(EdgeChromiumDriverManager().install())
        ops = webdriver.EdgeOptions()
        ops.add_experimental_option("detach", True)
        context.driver = webdriver.Edge(service=ser_obj, options=ops)

    elif browser.__eq__("firefox"):
        from selenium.webdriver.firefox.service import Service
        from webdriver_manager.firefox import GeckoDriverManager

        ser_obj = Service(GeckoDriverManager().install())
        ops = webdriver.FirefoxOptions()
        context.driver = webdriver.Firefox(service=ser_obj, options=ops)

    else:
        raise ValueError("Inappropriate browser")

    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    context.driver.get(ConfigReader.readConfiguration("basic info", "url"))


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
