import unittest

from scrapper import Scrapper

class ScrapperTest(unittest.TestCase):
    def test_ideal(self):
        """
        ideal case
        """
        url = "https://www.esl-lounge.com/level1b/lev1bgapfillread.php"
        scrapper = Scrapper()
        message = "Error occurred while creating driver"
        self.assertTrue(scrapper.createDriver(), message)
        message = "Error occurred while setting url"
        self.assertTrue(scrapper.set_url(url), message)
        message = "Error occurred while getting text"
        self.assertTrue(scrapper.getText(), message)
        key = "Thank you for your last letter"
        container = str(scrapper.text)
        message = "Error in scrapping the text"
        self.assertIn(key, container, message)

    def test_bad_input(self):
        """
        negative case
        """
        scrapper = Scrapper()
        url = "fkhseoifh;"
        message = "No error while processing invalid url"
        self.assertFalse(scrapper.set_url(url), message)
