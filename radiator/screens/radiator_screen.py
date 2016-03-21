try:
    import ConfigParser as config
except:
    import configparser as config

import PyQt5.Qt as qt


DEFAULT_DELAY = 10


class RadiatorScreen(qt.QQuickItem):

    url_changed = qt.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(RadiatorScreen, self).__init__(*args, **kwargs)
        self._url = qt.QUrl('about:blank')
        self._url_index = 0
        self._urls = []
        self._delay = DEFAULT_DELAY
        self._load_settings()

    def componentComplete(self):
        super(RadiatorScreen, self).componentComplete()
        qt.QTimer.singleShot(self._delay * 1000, self._cycle_url)

    @qt.pyqtSlot()
    def _cycle_url(self):
        self._url_index += 1
        if self._url_index >= len(self._urls):
            self._url_index = 0

        self.url = self._urls[self._url_index]

        qt.QTimer.singleShot(self._delay * 1000, self._cycle_url)


    @qt.pyqtProperty(qt.QUrl, notify=url_changed)
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        if value is not None:
            self._url = qt.QUrl(value)
        else:
            self._url = qt.QUrl('about:blank')

        self.url_changed.emit()

    def _load_settings(self):
        config_parser = config.SafeConfigParser(allow_no_value=False)
        with open('radiator.cfg') as config_file:
            config_parser.readfp(config_file)

        delay = DEFAULT_DELAY
        urls_setting = ''
        if 'general' in config_parser.sections():
            general = config_parser['general']
            urls_setting = general.get('urls', '')
            delay = general.getint('delay', DEFAULT_DELAY)

        self._urls = list(map(lambda x: x.strip(), urls_setting.split(',')))
        self._delay = delay
