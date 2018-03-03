#### Minimal MenuBarTestApp (Systray App) for OSX
Minimal code to get a PyQt5 app to run only in the MenuBar, with no icon in the
Dock, and no 'TestApp' application menu in the MenuBar.

The documentation I've found online suggests that this Info.plist entry should
do the trick

```xml
          <key>LSUIElement</key>
          <string>1</string>
```

I found I had to add this to my executable:
```python
import AppKit                                                                   
info = AppKit.NSBundle.mainBundle().infoDictionary()                            
info["LSBackgroundOnly"] = "1"
```
