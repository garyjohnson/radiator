import QtQuick 2.2
import QtQuick.Window 2.1

Loader {

    id: root
    property int parentHeight
    property int parentWidth

    anchors.centerIn: parent
    parentHeight: parent == null ? 0 : parent.height
    parentWidth: parent == null ? 0 : parent.width
    height: screenRotation % 180 == 0 ? parentHeight : parentWidth
    width: screenRotation % 180 == 0 ? parentWidth : parentHeight

    source: 'radiator/screens/radiator_screen.qml'

    transform: Rotation {
        angle: screenRotation
        origin.x: root.width / 2
        origin.y: root.height / 2
    }
}
