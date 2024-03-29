# Zap's Cool Photon Theme
A Firefox userChrome theme designed to be as faithful to Firefox Photon (specifically Firefox 87) as possible.

![it's cool](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/5b0dbcc3-78f2-497e-a949-39f0fdfa63cf)
____

#### Compatibility
| | Windows 10/11 | Linux (GNOME) | macOS | Notes |
|-|:-:|:-:|:-:|:-:|
| **115esr** | ✔️ | ✔️ | ? | Includes forks of Firefox (Waterfox, Floorp, etc.) |
| **124** | ✔️ | ✔️ | ? | |
| **126** | ✔️ | ✔️ | ? | |

## Installation
There are 2 ways of installing this theme.
* [Manually](#manually)
* [As an Extension](#as-an-extension)

### Manually
Can be installed on all editions of Firefox. Configuration is handled in `about:config`. There is no auto-updating.

Open `about:config` and set:
| Pref | Value | Description |
|:-:|:-:|:-:|
| `toolkit.legacyUserProfileCustomizations.stylesheets` | `true` | Enables [userChrome](https://www.userchrome.org/) customization |
| `svg.context-properties.content.enabled` | `true` | Required in order to make the icons colored correctly |
| `layout.css.has-selector.enabled` | `true` | `true` by default in FF 121+. Required for some functionality to work. |
| `layout.css.nesting.enabled` | `true` | `true` by default in FF 117+. Required for theming and some other stuff to work. |
| `browser.newtabpage.activity-stream.logowordmark.alwaysVisible` | `false` | Reverts the new tab Firefox logo behavior to what it was in Photon |
____
If you're too lazy to copy and paste these `about:config` preferences, you can visit https://zapsnh.github.io/zcpt-configurator/, enable `Include preferences for theme installation`, and click `Export Options` to generate a `user.js` file that you can put in your profile folder.

Make sure to delete it after you start Firefox so that it doesn't override any changes you make in `about:config`.

Create `security.secure_connection_icon_color_gray` as a boolean and set it to `true` if you don't want the green connection icon.
____

Download the release for your version:

__Static Release (stability):__
* [Firefox 124](https://github.com/zapSNH/zapsCoolPhotonTheme/releases/tag/v124) **(recommended)**
* [Firefox 115esr](https://github.com/zapSNH/zapsCoolPhotonTheme/releases/tag/v124) (download the ESR version)

__Rolling Release (features and bugfixes):__
* [Firefox 124](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/main.zip)
* [Firefox Beta/Nightly](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/nightly.zip)
* [Firefox 115esr](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/115esr.zip)

<details>
	<summary>Older Versions</summary>

* [Firefox 99](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/archive-v99.zip)
* [Firefox 116 - 119](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/119.zip)
* [Other Versions (FF 120+)](https://github.com/zapSNH/zapsCoolPhotonTheme/releases)
</details>

____

Extract the zip and move `zapsCoolPhotonTheme-*` to your profile folder which you can find by going to `about:support` and opening your profile folder/directory.

Rename the `zapsCoolPhotonTheme-*` folder to `chrome`

Make sure the directory is like this:
* `Profiles` > `XXXXXXXX.profile` > `chrome` > `userChrome.css` and others

and **not** like this:
* `Profiles` > `XXXXXXXX.profile` > `chrome` > `zapsCoolPhotonTheme-*` > `userChrome.css` and others

Restart Firefox.

____

### As an Extension
Can only be installed on Firefox Developer Edition, Firefox Nightly, and Firefox ESR (and forks based on ESR). Has auto-updating and a built-in configurator.
This version is based on [Paxmod](https://github.com/numirias/paxmod).

Open `about:config` and set:
* `extensions.experiments.enabled` to `true`
* `xpinstall.signatures.required` to `false` [(Why?)](https://github.com/numirias/paxmod#why-cant-i-install-paxmod-as-a-verified-extension-through-mozilla)

Download the latest version at: https://github.com/zapSNH/zcpt-webextension/releases

You're done!

# Configuration
Config options are available at the [Wiki](https://github.com/zapSNH/zapsCoolPhotonTheme/wiki/Config-Options).

An interactive configurator is available at https://zapsnh.github.io/zcpt-configurator/. To apply the settings, place the exported `user.js` file in your profile folder/directory (`Profiles` > `XXXXXXXX.profile`), launch Firefox, and then delete the `user.js` file afterwards.

For the WebExtension version, the configurator is can be found in the extension's option page (`about:addons` > zap's cool photon theme > Preferences/Options). The settings apply after you click `Apply`.

## Miscellaneous
Photon Firefox icons are taken from the `omni.ja` file from Firefox 87.
Some other icons are modified/made by me.

Special thanks to:
- [black7375's Lepton](https://github.com/black7375/Firefox-UI-Fix)
- [YukisCoffee's Phroton](https://github.com/YukisCoffee/phroton/)
- The folks over on r/FirefoxCSS
- [Mozilla](https://www.mozilla.org/) since they made Firefox so customizable (and they made Photon)
