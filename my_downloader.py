from typing import List
from complementary_tools import (
    create_directory,
    generate_md5_hash,
    save_file
)
from requests_module import RequestsModule


class MyDownloader():
    DIRECTORY = 'diarios/tribunais/superior/stf'

    def __init__(self, request_stf: RequestsModule) -> None:
        self.request_stf = request_stf
        create_directory(MyDownloader.DIRECTORY)
        self.md5_list = []

    def get_md5(self) -> list:
        return self.md5_list

    def get_download(self, list_urls_pdf: List[str]) -> list:
        if not list_urls_pdf:
            print('There are no journal(s) published on this day.')
        for url in list_urls_pdf:
            self._download_pdf(url)

    def _download_pdf(self, url: str) -> None:
        bin_pdf = self.request_stf.get_response(url)
        md5_pdf = generate_md5_hash(bin_pdf)
        save_file(bin_pdf, f'{md5_pdf}.pdf', f'{MyDownloader.DIRECTORY}/')
        self._insert_md5(md5_pdf)

    def _insert_md5(self, md5_item: str) -> None:
        self.md5_list.append(md5_item)
