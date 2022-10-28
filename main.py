"""invokes the scrapper"""
from src.scrapper import Scrapper

if __name__ == '__main__':
    scrapper = Scrapper()
    scrapper.validate_driver()
    scrapper.validate_input()
    scrapper.validate_text()
