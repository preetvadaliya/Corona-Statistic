# CoronaStatus
# Module for get data of corona virus by using web scrapping.


# Import all required python modules for use.
from selenium import webdriver


class CoronaStatus:

    def __init__(self, driverPath):
        """
        ### CoronaStatus
        - Get Information about corona virus.
        
        #### Args
          `driverPath` = Selenium chrome driver path.
        """
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        self.driver = webdriver.Chrome(options=op, executable_path=driverPath)
        self.driver.get("https://rb.gy/0oxpsq")

    def getConfirmedInState(self):
        """
        #### getConfirmedInState( )
        return total number of confirmed case in state.
        """
        return self.driver.find_element_by_xpath(
            "//*[@id=\"rhs\"]/div[2]/div/div/div/div/div[2]/div[1]/div/div[1]/table/tbody/tr/td[1]/div[2]/div[1]/span").text

    def getRecoveredInState(self):
        """
        #### getRecoveredInState( )
        return total number of recovered case in state.
        """
        return self.driver.find_element_by_xpath(
            "//*[@id=\"rhs\"]/div[2]/div/div/div/div/div[2]/div[1]/div/div[1]/table/tbody/tr/td[2]/div[2]/div[1]/span").text

    def getDeathsInState(self):
        """
        #### getDeathsInState( )
        return total number of deaths in state.
        """
        return self.driver.find_element_by_xpath(
            "//*[@id=\"rhs\"]/div[2]/div/div/div/div/div[2]/div[1]/div/div[1]/table/tbody/tr/td[3]/div[2]/div[1]/span").text

    def getConfirmedInCountry(self):
        """
        #### getConfirmedInCountry( )
        return total number of confirmed case in country.
        """
        return self.driver.find_element_by_xpath(
            "//*[@id=\"rhs\"]/div[2]/div/div/div/div/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div[2]/div[1]/span").text

    def getRecoveredInCountry(self):
        """
        #### getRecoveredInCountry( )
        return total number of recovered case in country.
        """
        return self.driver.find_element_by_xpath(
            "//*[@id=\"rhs\"]/div[2]/div/div/div/div/div[2]/div[1]/div/div[2]/table/tbody/tr/td[2]/div[2]/div[1]/span").text

    def getDeathsInCountry(self):
        """
        #### getDeathsInCountry( )
        return total number of deaths in country.
        """
        return self.driver.find_element_by_xpath(
            "//*[@id=\"rhs\"]/div[2]/div/div/div/div/div[2]/div[1]/div/div[2]/table/tbody/tr/td[3]/div[2]/div[1]/span").text

    def getConfirmedInWorld(self):
        """
        #### getConfirmedInWorld( )
        return total number of condirmed case in world.
        """
        return self.driver.find_element_by_xpath(
            "//*[@id=\"rhs\"]/div[2]/div/div/div/div/div[2]/div[1]/div/div[3]/table/tbody/tr/td[1]/div[2]/div[1]/span").text

    def getRecoveredInWorld(self):
        """
        #### getRecoveredInWorld( )
        return total number of recovered case in world.
        """
        return self.driver.find_element_by_xpath(
            "//*[@id=\"rhs\"]/div[2]/div/div/div/div/div[2]/div[1]/div/div[3]/table/tbody/tr/td[2]/div[2]/div[1]/span").text

    def getDeathsInWorld(self):
        """
        #### getDeathsInWorld( )
        return total number of deaths in world.
        """
        return self.driver.find_element_by_xpath(
            "//*[@id=\"rhs\"]/div[2]/div/div/div/div/div[2]/div[1]/div/div[3]/table/tbody/tr/td[3]/div[2]/div[1]/span").text

    def getStateName(self):
        """
        #### getStateName( )
        return your state name.
        """
        return self.driver.find_element_by_xpath(
            "//*[@id=\"rhs\"]/div[2]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/span[2]/span").text

    def getCountryName(self):
        """
        #### getCountryName( )
        return your country name.
        """
        return self.driver.find_element_by_xpath(
            "//*[@id=\"rhs\"]/div[2]/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/span[2]/span").text
