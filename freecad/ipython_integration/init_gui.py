from PySide import QtGui
from qtconsole.rich_ipython_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager

import FreeCAD as App
import FreeCADGui as Gui
from PySide import QtCore, QtGui
def put_ipy(parent, mw):
    kernel_manager = QtInProcessKernelManager()
    kernel_manager.start_kernel()
    kernel = kernel_manager.kernel
    kernel.gui = 'qt'

    kernel_client = kernel_manager.client()
    kernel_client.start_channels()
    kernel_client.namespace  = parent

    def stop():
        kernel_client.stop_channels()
        kernel_manager.shutdown_kernel()

    widget = RichJupyterWidget(parent=parent)
    widget.kernel_manager = kernel_manager
    widget.kernel_client = kernel_client
    widget.exit_requested.connect(stop)
    parent.setWidget(widget)
    widget.show()
    kernel.shell.push({'widget':widget,'kernel':kernel, 'parent':parent})
    kernel.shell.push({'App':App,'Gui':Gui})
    return widget

mw = Gui.getMainWindow()
dock_widget = QtGui.QDockWidget()
console = put_ipy(dock_widget, mw)
dock_widget.setWindowTitle("Ipython-qt-console")

mw.addDockWidget(QtCore.Qt.BottomDockWidgetArea, dock_widget)

