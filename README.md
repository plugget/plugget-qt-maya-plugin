# Plugget Qt Maya plugin

A maya plugin to add [plugget-qt](https://github.com/plugget/plugget-qt) to the menu.  
When run, it opens a dockable widget to search & install Maya plugins.   
![image](https://github.com/plugget/plugget-qt-maya-plugin/assets/3758308/36c17c2d-ccbe-4938-960f-9cb02e932695)




## Installation 

### Installer
1. [Download](https://github.com/plugget/plugget-qt-maya-plugin/archive/refs/heads/main.zip) the project 
2. drag & drop the  `installer.mel` in Maya.  <!-- [here](https://raw.githubusercontent.com/plugget/plugget-qt-maya-plugin/main/installer.mel))   -->  
This auto installs plugget qt & it's dependencies on Windows OS.
3. copy the `plugget-qt-maya-plugin.py` to the `user/documents/maya/plug-ins` folder.  

### Manual installation
<details>
<summary>Manual installation </summary>

#### install the Python plugin
- copy the `plugget-qt-maya-plugin.py` to the `maya/plug-ins` folder.  
- or run the below command to do it for you.
```
pip install https://github.com/plugget/plugget-qt-maya-plugin/archive/refs/heads/main.zip --target "C:/Users/%username%/Documents/Maya/plug-ins" --no-dependencies
```
<sup>_1. if the target folder doesn't exist, this command creates a `Maya/plug-ins` folder in your documents , which requires admin access_</sup>  
<sup>_2. When a user has been renamed on Windows, `%username%` will return the current name. But the folder path will use the old name_</sup>  

#### install the Python dependencies
pip install the dependencies to the Maya script folder
```
pip install plugget-qt --target "C:/Users/%username%/Documents/Maya/scripts" --no-dependencies
```
</details>

#### enable plugin
Enable the `plugget_qt_maya_plugin.py` plugin in Maya's plug-in manager:  
`Windows` > `Settings/Preferences` > `Plug-in Manager`  
![image](https://github.com/plugget/plugget-qt-maya-plugin/assets/3758308/2f8f3e0e-660a-47da-ae32-10c865ed9f4d)


Open plugget qt from the Maya menu `Tools/Plugget`

## other
- plugget package https://github.com/plugget/plugget-pkgs/tree/main/maya/plugget-qt-maya-plugin
- Maya discussion https://forums.cgsociety.org/t/plugget-a-free-maya-tool-manager/2074249
