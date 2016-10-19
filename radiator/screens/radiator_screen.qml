import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3
import QtWebEngine 1.3
import Screens 1.0
import '../widgets'


RadiatorScreen {

    id:root

    WebEngineView {
        anchors.fill: parent
        url: root.url
    }

    Marquee {
        anchors.fill: parent
    }
}
