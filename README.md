Minimal code to get a PyQt5 app to run only in the MenuBar, with no icon in the
Dock, and no 'TestApp' application menu in the MenuBar.

The documentation I've found online suggests that this Info.plist entry should
do the trick:
          <key>LSUIElement</key>
          <string>1</string>

I've also tried:
          <key>LSUIElement</key>
          <true />

Neither seem to have the desired effect, but they do change the behaviour of
the app. When the app starts up, the 'TestApp' menu (which appears in the top
left of the screen, next to the Apple-icon menu) does not respond to clicks.

If I switch focus to another app and then switch back, it starts to respond to
clicks.

If I remove the LSUIElement entry from the Info.plist, the TestApp menu behaves
normally.
