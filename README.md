# Zap's Cool Photon Theme
A userChrome designed to be as faithful to Firefox Photon (specifically Firefox 87) as possible.

See Compatibility for version compatibility
![unfaithton](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/a2690e89-774b-4c4d-9f02-ce160b025bbb)

____

#### Compatibility
| | Windows 10/11 | Linux (Ubuntu) | MacOS |
|-|:-:|:-:|:-:|
| **102esr** | Semi-broken | ? | ? |
| **115esr** | ✔️ | ✔️ | ? |
| **116** | ✔️ | ✔️ | ? |
| **118** | ✔️ | ✔️ | ? | 
## Installation
Open `about:config` and set:
* `toolkit.legacyUserProfileCustomizations.stylesheets` to `true`
* `svg.context-properties.content.enabled` to `true`
* `layout.css.has-selector.enabled` to `true`
* `browser.translations.enable` to `true` (recommended because of layout issues)

Create `change security.secure_connection_icon_color_gray` as a boolean and set it to `true` if you don't want the green connection icon.

Download the release for your version:
[Firefox 115esr]()
[Firefox 116 - 118]()

Extract the zip and move `zapsCoolPhotonTheme-main` to your profile which you can find by going to `about:profiles` and opening the root directory's folder.

Rename `zapsCoolPhotonTheme-main` to `chrome`


Make sure the directory is like this:
* `Profiles` > `your profile` > `chrome`

and not like this:
* `Profiles` > `your profile` > `chrome` > `zapsCoolPhotonTheme-main`

Restart Firefox

# Misc.
Photon Firefox icons are taken from the `omni.ja` file from Firefox 87 
