<h1 align="center">
	<img src="https://github.com/user-attachments/assets/bb23b9b4-0011-4ac8-acfe-3996006bb2de" alt="oversized logowordmark" title="oversized logowordmark">
</h1>

<p align="center">
	A userChrome theme for Firefox-based browsers designed to be as <b>faithful</b> to Firefox Photon (specifically Firefox 87) as possible.
</p>

![okay](https://github.com/user-attachments/assets/7f67b471-e33a-4c2a-a9cb-94cbfd6ea5b2)
<h4 align="center"><a href="https://github.com/zapSNH/zapsCoolPhotonTheme/wiki/Showcase">&gt; (showcase) &lt;</a></h4>

<hr>
	
<h4 align="center">
	 Compatibility
</h4>

<div align="center">
	
Includes forks of Firefox (Waterfox, Floorp, etc.).
| | Windows | Linux (GNOME) | macOS | Notes |
|-|:-:|:-:|:-:|:-:|
| **115esr** | ✔️ | ✔️ | ✔️ | No longer updated |
| **128esr** | ✔️ | ✔️ | ✔️ | |
| **140** | ✔️ | ✔️ | ✔️ | |
| **142 nightly** | ✔️ | ✔️ | ? | |

See the [Forks](#forks-) section for more information about Firefox forks.

</div>


## Installation
There are four (4) ways of installing this theme.
* [Manual Installation 🛠](#manual-installation-)
* [Sine 🪐](#sine-)
* [Extension 🧩](#extension-)
* [Git :octocat:](#git-octocat)
  
____
### Manual Installation 🛠
Installable on all editions of Firefox (and forks). Configuration is handled in `about:config`. There is no auto-updating.

Open `about:config` and set:
| Pref | Value | Description |
|:-:|:-:|:-:|
| `toolkit.legacyUserProfileCustomizations.stylesheets` | `true` | Enables [userChrome](https://www.userchrome.org/) customization. |
| `svg.context-properties.content.enabled` | `true` | Required for proper icon coloring. |
| `browser.newtabpage.activity-stream.logowordmark.alwaysVisible` | `false` | Reverts the new tab Firefox logo behavior to what it was in Photon. |
| `widget.windows.mica.popups` | `0` | (Windows only) Disables transparency effects on menus.<br>If you're/you will be using [`uc.popups.transparent`](https://github.com/zapSNH/zapsCoolPhotonTheme/wiki/Config-Options#menu-transparency), then don't change this option. |
<details>
	<summary>For Firefox 121 and below...</summary>
	
| Pref | Value | Description |
|:-:|:-:|:-:|
| `layout.css.has-selector.enabled` | `true` | **Only for Firefox 121 and below.**<br>Required for some functionality to work. |
| `layout.css.nesting.enabled` | `true` | **Only for Firefox 117 and below.**<br>Required for theming and some other stuff to work. |
</details>

Optionally, you can set:
| Pref | Value | Description |
|:-:|:-:|:-:|
| `security.secure_connection_icon_color_gray` | `true` | Makes the connection icon gray instead of green.<br>Defaults to `true` in later versions of Photon. |
____
Too lazy to set all these prefs? You can visit https://zapsnh.github.io/zcpt-configurator/, enable `Include preferences for theme installation` (and maybe customize the theme a bit), and click `Export Options` to generate a `user.js` file that you can put in your profile folder.

**Make sure to delete the `user.js` file after you start Firefox so that it doesn't override any changes you make in `about:config`.**
____

Download the release for your browser version:

| __🪨 Static Release (stability)__ | __🛞 Rolling Release (features and bugfixes)__ |
|-|-|
| [Firefox 140](https://github.com/zapSNH/zapsCoolPhotonTheme/releases/tag/v140) **(recommended)**             | [Firefox 140](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/main.zip)             |
| [Firefox 128esr](https://github.com/zapSNH/zapsCoolPhotonTheme/releases/tag/v140) (download the ESR version) | [Firefox 128esr](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/128esr.zip)        |
| [Firefox 115esr](https://github.com/zapSNH/zapsCoolPhotonTheme/releases/tag/v128) (download the ESR version) | [Firefox Beta/Nightly](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/nightly.zip) |

<details>
	<summary>Older Versions</summary>

* [Firefox 99](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/archive-v99.zip)
* [Firefox 116 - 119](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/119.zip)
* [Other Versions (Firefox 120+)](https://github.com/zapSNH/zapsCoolPhotonTheme/releases)
</details>

____

Extract the zip and move `zapsCoolPhotonTheme-*` (where `*` is `main`, `128esr`, etc.) to your profile folder which you can find by going to `about:support` and opening your profile folder/directory.

Rename the `zapsCoolPhotonTheme-*` folder to `chrome`

Make sure the directory is like this:
* `Profiles` > `XXXXXXXX.profile_name_here` > `chrome` > `userChrome.css` and others

and **not** like this:
* `Profiles` > `XXXXXXXX.profile_name_here` > `chrome` > `zapsCoolPhotonTheme-*` > `userChrome.css` and others

Restart Firefox.

You're done! 🎉

____
### Sine 🪐
> [!NOTE]
> Currently experimental and subject to change

Installable on all editions of Firefox (and forks), though is partially broken on Firefox 128esr. Requires Sine. Has auto-updating and a basic configurator.

Install the Sine theme manager for your browser. ([follow this guide](https://github.com/CosmoCreeper/Sine?tab=readme-ov-file#%EF%B8%8F-installation))

You can install this theme by searching for it (zap's cool photon theme) in Sine's marketplace and installing it.

~You can also install it by typing in this repo (zapSNH/zapsCoolPhotonTheme), and optionally the branch (append tree/[the branch, e.g. nightly]), into the local installation text box and installing it there.~ (broken right now)

You're done! 🎉
____
### Extension 🧩
Only installable on Firefox Developer Edition, Firefox Nightly, and Firefox ESR (and forks based on these versions) since **you need to disable extension signing** (which may be insecure).

Has auto-updating and a built-in configurator.
This version is based on [Paxmod](https://github.com/numirias/paxmod).

Open `about:config` and set:
| Pref | Value | Description |
|:-:|:-:|:-:|
| `extensions.experiments.enabled`  | `true` | Enables extensions experiments which allows CSS theming in extensions. |
| `xpinstall.signatures.required` | `false` | Disables extension signing which may be insecure. See [this](https://github.com/numirias/paxmod#why-cant-i-install-paxmod-as-a-verified-extension-through-mozilla) for the reason.  |
  
All other preferences required to run the theme (see [the table above](#manual-installation-)) will be set automatically.

Download the release for your browser version:
| Browser Version | Extension Version |
|:-:|:-:|
| 128+ | [Latest Version](https://github.com/zapSNH/zcpt-webextension/releases/latest) |
| 115 - 127 | [v0.24.5](https://github.com/zapSNH/zcpt-webextension/releases/tag/v0.24.5) |

More info at: https://github.com/zapSNH/zcpt-webextension/blob/main/README.md

You're done! 🎉

____

### Git :octocat: 
<!-- yes i know that the github != git just shut up -->
Recommended for people who know what they're doing.

Installable on all editions of Firefox. Configuration is handled in `about:config`. There is no auto-updating (unless you make a script for that) but you can quickly update using `git pull` in your terminal.

Open `about:config` and set the same prefs in the [Manual](#manual-installation-) installation.

Download and install [Git](https://git-scm.com/) if you haven't already.

Open your profile folder which you can find by going to `about:support` and opening your profile folder/directory.

If you're in a file manager with a GUI (Explorer, Finder, etc.), open a terminal in the profile folder, usually by right clicking and clicking Open in Terminal (or similar). [(example)](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/c35ffc7d-0343-479a-9366-72d56833c4c3)

Copy (or type) this command into the terminal `git clone https://github.com/zapSNH/zapsCoolPhotonTheme.git chrome` and press enter. **Make sure the terminal is in the profile folder (like `Profiles` > `XXXXXXXX.profile_name_here`) and not in any of its subfolders.**

If you're using a version of Firefox that isn't the latest stable version then copy (or type) these commands into the terminal.
```
cd chrome
git checkout BRANCH_NAME
```
where `BRANCH_NAME` is [your Firefox version (i.e. `115esr` or `nightly`)](https://github.com/zapSNH/zapsCoolPhotonTheme/branches). (don't use the ones prefixed by `webextension`)

You're done! 🎉

# Forks 🍴
If you're using a Firefox fork (e.g. Waterfox, Floorp, etc.), you can set these prefs in `about:config` for theme fixes and adjustments for your browser.

It is recommended to disable any UI styles set by the browser to prevent conflicts.
| Pref | Value | Browser |
|:-:|:-:|:-:|
| `uc.waterfox` | `true` | Waterfox |
| `uc.floorp` | `true` | Floorp |
| `uc.librewolf` | `true` | LibreWolf |
| `uc.tor` | `true` | Tor Browser |
| `uc.mullvad` | `true` | Mullvad Browser |

# Configuration
Config options are available at the [Wiki](https://github.com/zapSNH/zapsCoolPhotonTheme/wiki/Config-Options).

An interactive configurator is available at https://zapsnh.github.io/zcpt-configurator/. To apply the settings, place the exported `user.js` file in your profile folder/directory (`Profiles` > `XXXXXXXX.profile`), launch Firefox, and then delete the `user.js` file afterwards.

For the WebExtension version, the configurator can be found in the extension's option page (`about:addons` > zap's cool photon theme > Preferences/Options). The settings will apply after you click `Apply` (unless you're 𝓯𝓻𝓮𝓪𝓴𝔂).

## Miscellaneous
Firefox Photon icons are primarily taken from Firefox 87 or Firefox 78esr.
Other icons not present in Firefox Photon are recreated based on their Proton/Acorn counterparts.

Special thanks to:
- [black7375's Lepton](https://github.com/black7375/Firefox-UI-Fix)
- [YukisCoffee's Phroton](https://github.com/YukisCoffee/phroton-legacy/)
- The folks over at r/FirefoxCSS
- [Mozilla](https://www.mozilla.org/) since they made Firefox so customizable [and made Photon (but they also made Proton >:()]
