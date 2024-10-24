from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class GoogleSearchTest(unittest.TestCase):
    
    def setUp(self):
        # Ścieżka do chromedrivera, ustaw ją jeśli nie masz chromedrivera w PATH
        self.driver = webdriver.Chrome(executable_path="/path/to/chromedriver")
        self.driver.get("https://www.google.com")

    def test_search_in_google(self):
        driver = self.driver

        # Znalezienie pola wyszukiwania za pomocą nazwy elementu
        search_box = driver.find_element(By.NAME, "q")
        
        # Wprowadzenie zapytania do pola wyszukiwania
        search_box.send_keys("Selenium Python")
        
        # Symulowanie naciśnięcia klawisza Enter
        search_box.send_keys(Keys.RETURN)
        
        # Odczekanie kilku sekund, aby strona mogła się załadować
        time.sleep(3)
        
        # Sprawdzenie, czy na stronie wyników wyszukiwania pojawiła się fraza "Selenium"
        self.assertIn("Selenium", driver.page_source)

    def tearDown(self):
        # Zamknięcie przeglądarki po teście
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
