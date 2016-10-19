try:
    import ConfigParser as config
except:
    import configparser as config

import PyQt5.Qt as qt
import radiator.services as services
import radiator.service.url_service as url_service


DEFAULT_DELAY = 10


class RadiatorScreen(qt.QQuickItem):

    url_changed = qt.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(RadiatorScreen, self).__init__(*args, **kwargs)
        self._url_service = services.get(url_service.UrlService)
        self._url = qt.QUrl('about:blank')
        self._delay = DEFAULT_DELAY
        self._load_settings()

    def componentComplete(self):
        super(RadiatorScreen, self).componentComplete()
        self._cycle_url()

    @qt.pyqtSlot()
    def _cycle_url(self):
        self._url_service.cycle_url()
        self.url = self._url_service.current_url()

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
        if 'general' in config_parser.sections():
            general = config_parser['general']
            delay = general.getint('delay', DEFAULT_DELAY)

        self._delay = delay
