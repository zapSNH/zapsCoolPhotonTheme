# Zap's Cool Photon Theme
A userChrome designed to be as faithful to Firefox Photon (specifically Firefox 87) as possible.

See Compatibility for version compatibility
![unfaithton](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/a2690e89-774b-4c4d-9f02-ce160b025bbb)

____

#### Compatibility
| | Windows 10/11 | Linux (Ubuntu) | MacOS |
|-|:-:|:-:|:-:|
| **102esr** | Semi-broken | ? | ? |
| **115esr** | ✔️ | Semi-broken | ? |
| **117** | ✔️ | ✔️ | ? |
| **119** | ✔️ | ✔️ | ? | 
## Installation
Open `about:config` and set/create:
* `toolkit.legacyUserProfileCustomizations.stylesheets` to `true`
* `svg.context-properties.content.enabled` to `true`
* `layout.css.has-selector.enabled` to `true`
* `uc.reduced-megabar` to `false`

Switching `uc.reduced-megabar` to `true` reduces the size of the megabar to Proton's size. Yes, the highlighted/open megabar is smaller in Proton.

Create `security.secure_connection_icon_color_gray` as a boolean and set it to `true` if you don't want the green connection icon.

Download the release for your version:
* [Firefox 115esr](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/115esr.zip)
* [Firefox 116 - 118](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/main.zip)
* [Firefox Nightly](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/nightly.zip)

Extract the zip and move `zapsCoolPhotonTheme-*` to your profile which you can find by going to `about:profiles` and opening the root directory's folder.

Rename `zapsCoolPhotonTheme-*` to `chrome`


Make sure the directory is like this:
* `Profiles` > `your profile` > `chrome`

and not like this:
* `Profiles` > `your profile` > `chrome` > `zapsCoolPhotonTheme-main`

Restart Firefox

# Tab separators
Sometimes the tab separators go missing. If you want them to show up always then remove line 277 (https://github.com/zapSNH/zapsCoolPhotonTheme/blob/b9b6adae9a3844568fc394885cdd5334224d4476/resources/tabs-and-urlbar.css#L277) from `tabs-and-urlbar.css`.

This will result in a separator before the selected tab, so if you don't want that look and are fine with separators sometimes going missing, then don't remove it.

# Misc.
Photon Firefox icons are taken from the `omni.ja` file from Firefox 87 
