import QtQuick 2.2
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.1
import QtWebKit 3.0
import Screens 1.0
import '../widgets'


RadiatorScreen {

    id:root

    WebView {
        anchors.fill: parent
        url: root.url
    }

    Marquee {
        anchors.fill: parent
    }
}
