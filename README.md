# Plugget Qt Maya plugin

A maya plugin to add [plugget-qt](https://github.com/plugget/plugget-qt) to the menu.  
When run, it opens a dockable widget to search & install Maya plugins.   
![image](https://github.com/plugget/plugget-qt-maya-plugin/assets/3758308/cce315dd-b509-4050-be2e-29af1196d992)




## Installation 

### Installer (windows only)
1. [Download](https://github.com/plugget/plugget-qt-maya-plugin/archive/refs/heads/main.zip) & extract the project
2. drag & drop the  `installer.mel` in Maya <!-- [here](https://raw.githubusercontent.com/plugget/plugget-qt-maya-plugin/main/installer.mel))   -->
to install plugget qt & it's dependencies.

### Manual installation
<details>
<summary>Click here to show instructions for the manual installation </summary>

#### 1. install the Python plugin
- copy the `plugget-qt-maya-plugin.py` to the `maya/plug-ins` folder.  
- or run the below command to do it for you.
```
pip install https://github.com/plugget/plugget-qt-maya-plugin/archive/refs/heads/main.zip --target "C:/Users/%username%/Documents/Maya/plug-ins" --no-dependencies
```
<sup>_1. if the target folder doesn't exist, this command creates a `Maya/plug-ins` folder in your documents , which requires admin access_</sup>  
<sup>_2. When a user has been renamed on Windows, `%username%` will return the current name. But the folder path will use the old name, requiring you to manually edit the path_</sup>  

#### 2. install the Python dependencies
pip install the dependencies to the Maya script folder
```
pip install plugget-qt --target "C:/Users/%username%/Documents/Maya/scripts" --no-dependencies
```
#### 3. enable plugin
Enable the `plugget_qt_maya_plugin.py` plugin in Maya's plug-in manager:  
`Windows` > `Settings/Preferences` > `Plug-in Manager`  
![image](https://github.com/plugget/plugget-qt-maya-plugin/assets/3758308/2f8f3e0e-660a-47da-ae32-10c865ed9f4d)

</details>

Open plugget qt from the Maya menu `Tools/Plugget`

## other
- plugget package https://github.com/plugget/plugget-pkgs/tree/main/maya/plugget-qt-maya-plugin
- Maya discussion https://forums.cgsociety.org/t/plugget-a-free-maya-tool-manager/2074249
