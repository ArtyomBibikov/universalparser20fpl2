"""Saving text to file"""
from src import scrapper

class FileSaving:
    def __init__(self, filename):
        with(open(filename, 'wb')) as output_file:
            output_file.write(self.text)
            output_file.close()


if __name__ == '__main__':
    pass
