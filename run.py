import argparse as argp

from requests_module import RequestsModule
from my_downloader import MyDownloader
from my_scraper import MyScraper


def get_args() -> str:
    my_parser = argp.ArgumentParser(
        prog='my-scraping.py', description='Receive a date and return an MD5 hash list of the PDFs of the journals made available on the fetched date.')
    my_parser.add_argument('input_date', type=str,
                           help='Enter a date in type DD-MM-YYYY')
    args = my_parser.parse_args()
    return args.input_date


def __main__():
    input_date = get_args()
    request_stf = RequestsModule()
    scrapping = MyScraper(request_stf)
    list_urls_pdf = scrapping._get_list_urls_pdf(input_date)
    pdf_download = MyDownloader(request_stf)
    pdf_download.get_download(list_urls_pdf)
    md5_list = pdf_download.get_md5()
    cont = 1
    print('\nOn this date ({date}), these journals were made available:\n'.format(
        date=input_date))
    for md5 in md5_list:
        print('[{cont}] '.format(cont = cont), md5)
        cont += 1
    print('\n{cont} File(s) downloaded.\n'.format(cont = cont-1))


if __name__ == "__main__":
    __main__()
