import PyQt5.Qt as qt


class RadiatorScreen(qt.QQuickItem):

    def __init__(self, *args, **kwargs):
        super(RadiatorScreen, self).__init__(*args, **kwargs)

    def componentComplete(self):
        super(RadiatorScreen, self).componentComplete()
