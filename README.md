# Zap's Cool Photon Theme
A userChrome designed to be as faithful to Firefox Photon (specifically Firefox 87) as possible.

![it's cool](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/5b0dbcc3-78f2-497e-a949-39f0fdfa63cf)
____

#### Compatibility
| | Windows 10/11 | Linux (GNOME 45) | MacOS | Notes |
|-|:-:|:-:|:-:|:-:|
| **115esr** | ✔️ | Semi-broken | ? | No Updates |
| **120** | ✔️ | ✔️ | ? | |
| **122** | ✔️ | ✔️ | ? | |
## Installation
Open `about:config` and set/create:
* `toolkit.legacyUserProfileCustomizations.stylesheets` to `true`
* `svg.context-properties.content.enabled` to `true`
* `layout.css.has-selector.enabled` to `true`
* `layout.css.nesting.enabled` to `true`
* `browser.newtabpage.activity-stream.logowordmark.alwaysVisible` to `false`
____
If you're too lazy to copy and paste these `about:config` preferences, you can visit https://zapsnh.github.io/zcpt-configurator/, enable `Include preferences for theme installation`, and generate a `user.js` file that you can put in your profile folder.

Make sure to delete it after you start Firefox so that it doesn't override any changes you make in `about:config`.

Create `security.secure_connection_icon_color_gray` as a boolean and set it to `true` if you don't want the green connection icon.
____

Download the release for your version:

__Static Release (stability):__
* [Firefox 120](https://github.com/zapSNH/zapsCoolPhotonTheme/releases/tag/v120)
* [Firefox 115esr](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/115esr.zip)

__Rolling Release (features and bugfixes):__
* [Firefox 120 - 121](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/main.zip)
* [Firefox Nightly](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/nightly.zip)

__Experimental WebExtension Version (auto updates):__
* [Firefox Nightly/Dev](https://github.com/zapSNH/zcpt-webextension) (follow the README.md instructions)

<details>
	<summary>Older Versions</summary>

* [Firefox 99](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/archive-v99.zip)
* [Firefox 116 - 119](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/119.zip)
* [Other Versions](https://github.com/zapSNH/zapsCoolPhotonTheme/releases)
</details>

_Note: Firefox versions other than the latest versions (nightly, beta/dev, and stable, but NOT esr) will not get feature updates._
____

Extract the zip and move `zapsCoolPhotonTheme-*` to your profile which you can find by going to `about:support` and opening your profile folder/directory.

Rename `zapsCoolPhotonTheme-*` to `chrome`


Make sure the directory is like this:
* `Profiles` > `XXXXXXXX.profile` > `chrome`

and not like this:
* `Profiles` > `XXXXXXXX.profile` > `chrome` > `zapsCoolPhotonTheme-*`

Restart Firefox

# Configuration
Config options are available at the [Wiki](https://github.com/zapSNH/zapsCoolPhotonTheme/wiki/Config-Options).

An interactive configurator is available at https://zapsnh.github.io/zcpt-configurator/. To apply the settings, place the exported `user.js` file in your profile folder/directory (`Profiles` > `XXXXXXXX.profile`), launch Firefox, and then delete it afterwards.

For the WebExtension version, the configurator is can be found in the extension's option page. The settings apply after you click `Apply`.

## Misc.
Photon Firefox icons are taken from the `omni.ja` file from Firefox 87.
Some other icons are modified/made by me.

Special thanks to:
- [black7375's Lepton](https://github.com/black7375/Firefox-UI-Fix)
- [YukisCoffee's Phroton](https://github.com/YukisCoffee/phroton/)
- The folks over on r/FirefoxCSS
- [Mozilla](https://www.mozilla.org/) since they made Firefox so customizable (and they made Photon)
- Windows 11 for opening Edge everytime I accidentally press F1 instead of F2 to rename stuff in explorer. I think YOU need to get help Microsoft.
