from requests_module import RequestsModule
from bs4 import BeautifulSoup
from datetime import datetime


class MyScraper():
    URL_BASE: str = 'https://www.stf.jus.br/portal/diariojusticaeletronico/'
    URL_PDFS_PER_DATE: str = 'montarDiarioEletronico.asp?tp_pesquisa=0&dataP='

    def __init__(self, request_stf: RequestsModule) -> None:
        self.request_stf = request_stf

    def _get_list_urls_pdf(self, date: str) -> list:
        self._check_date(date)
        list_urls_pdf = self._get_urls_pdf(date)
        return list_urls_pdf

    def _get_urls_pdf(self, date: str) -> list:
        html_page = self._get_html_page(date)
        html_page = BeautifulSoup(html_page, 'html.parser')
        urls_pdf = html_page.select('a[target]')
        list_urls_pdf = [
            (f'{MyScraper.URL_BASE}{links.get("href").strip()}') for links in urls_pdf]
        if not list_urls_pdf:
            print('There are no journal(s) published on this day.')
            exit()
        return list_urls_pdf

    def _get_links_pdf(self, links: str) -> list:
        for i in links:
            if i.attrs.get("target"):
                list_urls_pdf = f'{MyScraper.URL_BASE}{i.get("href").strip()}'
        return list_urls_pdf

    def _get_html_page(self, date: str) -> bytes:
        url = f'{MyScraper.URL_BASE}{MyScraper.URL_PDFS_PER_DATE}{date}'
        html_page = self.request_stf.get_response(url)
        return html_page

    def _check_date(self, date: str) -> None:
        try:
            datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            print('This is the incorrect date string format. It should be DD-MM-YYYY')
