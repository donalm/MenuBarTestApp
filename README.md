#### Minimal MenuBarTestApp (Systray App) for OSX
Minimal code to get a PyQt5 app to run only in the MenuBar, with no icon in the
Dock, and no 'TestApp' application menu in the MenuBar.

The documentation I've found online suggests that this Info.plist entry should
do the trick

```xml
          <key>LSUIElement</key>
          <string>1</string>
```

That did not work for me - I found I had to add this to my executable:
```python
import AppKit
info = AppKit.NSBundle.mainBundle().infoDictionary()
info["LSBackgroundOnly"] = "1"
```

The code expects to find a working python interpreter at:
/opt/miniconda/miniconda3/envs/pyqt5/bin/python

You'll need to have pyqt5 and pyobjc modules available. See the contents of
conda_list.txt for a full list of the modules in my environment.

By experimentation I found that I had to install some pyobjc modules using both
conda and pip - otherwise I get this error:
```bash
LSOpenURLsWithRole() failed with error -10810 for the file /Applications/Hanshiro.app.
```

I'm running the code with this Python release from Miniconda:
```bash
Python 3.6.3 |Anaconda, Inc.| (default, Dec  5 2017, 17:30:25)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```
