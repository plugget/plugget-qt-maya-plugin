import sys
import maya.api.OpenMaya as om
import maya.cmds as cmds
import shiboken2
import maya.OpenMayaUI as apiUI
from maya import cmds, OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore


# def get_maya_window():
#     ptr = apiUI.MQtUtil.mainWindow()
#     if ptr is not None:
#         return shiboken2.wrapInstance(int(ptr), QtWidgets.QWidget)


def Dock(Widget:type, width:int=300, show:bool=True):
    """
    Wrap your widget in a native dockable Maya widget
    Widget (QWidget): Class
    show (bool): Whether to show the resulting dock once created
    """

    name = Widget.__name__
    label = getattr(Widget, "label", name)

    try:
        cmds.deleteUI(name)
    except RuntimeError:
        pass

    dockControl = cmds.workspaceControl(
        name,
        tabToControl=["AttributeEditor", -1],
        initialWidth=width,
        minimumWidth=True,
        widthProperty="preferred",
        label=label
    )

    dockPtr = omui.MQtUtil.findControl(dockControl)
    dockWidget = shiboken2.wrapInstance(int(dockPtr), QtWidgets.QWidget)
    dockWidget.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    child = Widget(parent=dockWidget)
    dockWidget.layout().addWidget(child)

    if show:
        cmds.evalDeferred(
            lambda *args: cmds.workspaceControl(
                dockControl,
                edit=True,
                restore=True
            )
        )

    return child




MENU_NAME = "ToolsMenu"  # no spaces in names, use CamelCase
MENU_LABEL = "Tools"  # spaces are fine in labels
MENU_ENTRY_LABEL = "Plugget Qt"

MENU_PARENT = "MayaWindow"  # do not change

def maya_useNewAPI():  # noqa
    pass  # dummy method to tell Maya this plugin uses Maya Python API 2.0


# =============================== Menu ===========================================
def show(*args):
    import plugget_qt
    
    dock_widget = Dock(plugget_qt.PluggetWidget)
    return dock_widget


def loadMenu():
    if not cmds.menu(f"{MENU_PARENT}|{MENU_NAME}", exists=True):
        cmds.menu(MENU_NAME, label=MENU_LABEL, parent=MENU_PARENT)
    cmds.menuItem(label=MENU_ENTRY_LABEL, command=show, parent=MENU_NAME)  


def unloadMenuItem():
    if cmds.menu(f"{MENU_PARENT}|{MENU_NAME}", exists=True):
        menu_long_name = f"{MENU_PARENT}|{MENU_NAME}"
        menu_item_long_name = f"{menu_long_name}|{MENU_ENTRY_LABEL}"
        # Check if the menu item exists; if it does, delete it
        if cmds.menuItem(menu_item_long_name, exists=True):
            cmds.deleteUI(menu_item_long_name, menuItem=True)
        # Check if the menu is now empty; if it is, delete the menu
        if not cmds.menu(menu_long_name, query=True, itemArray=True):
            cmds.deleteUI(menu_long_name, menu=True)


# =============================== Plugin (un)load ===========================================
def initializePlugin(plugin):
    loadMenu()


def uninitializePlugin(plugin):
    unloadMenuItem()
    
