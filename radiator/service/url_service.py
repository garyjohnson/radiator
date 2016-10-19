import shelve
import logging
try:
    import ConfigParser as config
except:
    import configparser as config


logger = logging.getLogger(__name__)
RADIATOR_DB = 'radiator_db'
URLS_KEY = 'urls'


class UrlService(object):

    def __init__(self):
        self._urls = list()
        self._url_index = 0
        self._load_starting_urls()

    def set(self, urls):
        self._urls.clear()
        self._url_index = 0
        self._urls.extend(urls)
        self._save_urls(self._urls)

    def get(self):
        return list(self._urls)

    def add(self, url):
        self._urls.append(url)
        self._save_urls(self._urls)

    def remove(self, url):
        self._url_index = 0
        self._urls.remove(url)
        self._save_urls(self._urls)

    def current_url(self):
        return self._urls[self._url_index]

    def cycle_url(self):
        self._url_index += 1
        if self._url_index >= len(self._urls):
            self._url_index = 0

    def _get_saved_urls(self):
        saved_urls = None
        with shelve.open(RADIATOR_DB) as db:
            saved_urls = db.get(URLS_KEY, default=None)

        return saved_urls

    def _save_urls(self, urls):
        with shelve.open(RADIATOR_DB) as db:
            db[URLS_KEY] = urls

    def _get_default_urls(self):
        config_parser = config.SafeConfigParser(allow_no_value=False)
        with open('radiator.cfg') as config_file:
            config_parser.readfp(config_file)

        urls_setting = ''
        if 'general' in config_parser.sections():
            general = config_parser['general']
            urls_setting = general.get('default_urls', '')

        return list(map(lambda x: x.strip(), urls_setting.split(',')))

    def _load_starting_urls(self):
        urls = self._get_saved_urls()
        if urls is None:
            urls = self._get_default_urls()
        self.set(urls)
