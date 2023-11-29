# Plugget Qt Maya plugin

A maya plugin to add [plugget-qt](https://github.com/plugget/plugget-qt) to the menu




## Installation 

### Installer
Download `installer.mel`, and drag & drop it in Maya.
This auto installs plugget qt & it's dependencies on Windows OS.

### Manual installation
<details>
<summary>Manual installation </summary>

#### install the Python plugin
- copy the `plugget-qt-maya-plugin.py` to the maya scripts folder.  
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
![image](https://github.com/hannesdelbeke/maya-plugin-template/assets/3758308/a7134b7c-e9a0-45a9-8853-3493e191e848)

### Open plugget qt from the Maya menu `Tools/Plugget`

