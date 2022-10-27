from src.scrapper import Scrapper
from src.save_text_to_file import FileSaving


if __name__ == "__main__":
    scrapper = Scrapper()
    if scrapper.create_driver():
        if scrapper.input_url():
            if scrapper.scroll_and_get_text():
                FileSaving('URL-text.txt')
            else:
                print('Error while getting url text')
        else:
            print('Error while input URL')
    else:
        print('Cannot create scrapper')
