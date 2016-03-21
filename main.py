#!/usr/bin/env python

import os
import sys
import signal
import logging

import PyQt5.Qt as qt

import radiator.screens.radiator_screen as radiator_screen
import radiator.main_window as main_window


def exit_on_ctrl_c():
    signal.signal(signal.SIGINT, signal.SIG_DFL)


def main():
    exit_on_ctrl_c()

    app = qt.QApplication(sys.argv)

    qt.qmlRegisterType(radiator_screen.RadiatorScreen, 'Screens', 1, 0, 'RadiatorScreen')

    window = main_window.MainWindow()
    window.showFullScreen()

    sys.exit(app.exec_())


if __name__ == '__main__':

    log_levels = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
    }
    log_level_name = os.environ.get('RAD_LOG', 'ERROR')
    logging.basicConfig(level=log_levels[log_level_name])
    logging.getLogger().setLevel(log_levels[log_level_name])
    logger = logging.getLogger(__name__)
    logger.debug('radiator log level is {}'.format(log_level_name))

    main()
