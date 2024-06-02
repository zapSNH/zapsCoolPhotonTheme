# Zap's Cool Photon Theme
A Firefox userChrome theme designed to be as faithful to Firefox Photon (specifically Firefox 87) as possible.

![it's cool](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/5b0dbcc3-78f2-497e-a949-39f0fdfa63cf)
<p align="center"><a href="https://github.com/zapSNH/zapsCoolPhotonTheme/wiki/Showcase">(showcase)</a></p>

#### Compatibility
| | Windows 10/11 | Linux (GNOME) | macOS 14 | Notes |
|-|:-:|:-:|:-:|:-:|
| **115esr** | ✔️ | ✔️ | ✔️ | Includes forks of Firefox (Waterfox, Floorp, etc.) |
| **126** | ✔️ | ✔️ | ✔️ | |
| **128** | ✔️ | ✔️ | ? | |

See [Forks](#forks) for information about Firefox forks.

## Installation
There are 3 ways of installing this theme.
* [Manually 🛠](#manually-)
* [As an Extension 🧩](#as-an-extension-)
* [Using Git :octocat:](#using-git-octocat)
  
____
### Manually 🛠
Can be installed on all editions of Firefox. Configuration is handled in `about:config`. There is no auto-updating.

Open `about:config` and set:
| Pref | Value | Description |
|:-:|:-:|:-:|
| `toolkit.legacyUserProfileCustomizations.stylesheets` | `true` | Enables [userChrome](https://www.userchrome.org/) customization. |
| `svg.context-properties.content.enabled` | `true` | Required in order to make the icons colored correctly. |
| `browser.newtabpage.activity-stream.logowordmark.alwaysVisible` | `false` | Reverts the new tab Firefox logo behavior to what it was in Photon. |
| `layout.css.has-selector.enabled` | `true` | `true` by default in FF 121+. Required for some functionality to work. |
| `layout.css.nesting.enabled` | `true` | `true` by default in FF 117+. Required for theming and some other stuff to work. |

Optionally, you can set:
| Pref | Value | Description |
|:-:|:-:|:-:|
| `security.secure_connection_icon_color_gray` | `true` | Makes the connection icon gray instead of green.<br>Default behavior in later versions of Photon. |
____
Too lazy to set all these prefs? You can visit https://zapsnh.github.io/zcpt-configurator/, enable `Include preferences for theme installation`, and click `Export Options` to generate a `user.js` file that you can put in your profile folder.

**Make sure to delete the `user.js` file after you start Firefox so that it doesn't override any changes you make in `about:config`.**
____

Download the release for your version:

| __🪨 Static Release (stability)__ | __🛞 Rolling Release (features and bugfixes)__ |
|-|-|
| [Firefox 126](https://github.com/zapSNH/zapsCoolPhotonTheme/releases/tag/v126) **(recommended)**             | [Firefox 126](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/main.zip)             |
| [Firefox 115esr](https://github.com/zapSNH/zapsCoolPhotonTheme/releases/tag/v126) (download the ESR version) | [Firefox 115esr](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/115esr.zip)        |
|                                                                                                              | [Firefox Beta/Nightly](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/nightly.zip) |

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

You're done! 🎉

____

### As an Extension 🧩
Can only be installed on Firefox Developer Edition, Firefox Nightly, and Firefox ESR (and forks based on ESR) since you need to disable extension signing (which may be insecure).

Has auto-updating and a built-in configurator.
This version is based on [Paxmod](https://github.com/numirias/paxmod).

Open `about:config` and set:
| Pref | Value | Description |
|:-:|:-:|:-:|
| `extensions.experiments.enabled`  | `true` | Enables extensions experiments which allows CSS theming in extensions |
| `xpinstall.signatures.required` | `false` | Disables extension signing which may be insecure. See [this](https://github.com/numirias/paxmod#why-cant-i-install-paxmod-as-a-verified-extension-through-mozilla) for the reason.  |
  
All other preferences required to run the theme (see [the table above](#manually-)) will be set automatically.

Download the latest version at: https://github.com/zapSNH/zcpt-webextension/releases

More info at: https://github.com/zapSNH/zcpt-webextension/blob/main/README.md

You're done! 🎉

____

### Using Git :octocat:
Recommended for tech-savvy people.

Can be installed on all editions of Firefox. Configuration is handled in `about:config`. There is no auto-updating (unless you make a script for that) but you can quickly update using `git pull` in your terminal.

Open `about:config` and set the same prefs in the [Manual](#manually-) installation.

Download and install [Git](https://git-scm.com/) if you haven't already.

Open your profile folder which you can find by going to `about:support` and opening your profile folder/directory.

If you're in a file manager with a GUI (Explorer, Finder, etc.), open a terminal in the profile folder, usually by right clicking and clicking Open in Terminal (or similar). [(example)](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/c35ffc7d-0343-479a-9366-72d56833c4c3)

Copy (or type) this command into the terminal `git clone https://github.com/zapSNH/zapsCoolPhotonTheme.git chrome` and run it. **Make sure the terminal is in the profile folder and not in any of its subfolders.**

If you're using a version of Firefox that isn't the latest stable version then copy (or type) these commands into the terminal.
```
cd chrome
git checkout BRANCH_NAME
```
where `BRANCH_NAME` is [the branch of your Firefox version (i.e. `115esr` or `nightly`)](https://github.com/zapSNH/zapsCoolPhotonTheme/branches). (don't use the ones prefixed by `webextension`)

You're done! 🎉

# Forks
If you're using a Firefox fork (e.g. Waterfox, Floorp, etc.), you can set these prefs in `about:config` for theme fixes and adjustments for your browser.
| Pref | Value | Browser |
|:-:|:-:|:-:|
| `uc.waterfox` | `true` | Waterfox |
| `uc.floorp` | `true` | Floorp |

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
