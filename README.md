# Zap's Cool Photon Theme
A userChrome designed to be as faithful to Firefox Photon (specifically Firefox 87) as possible.

![it's cool](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/5b0dbcc3-78f2-497e-a949-39f0fdfa63cf)
____

#### Compatibility
| | Windows 10/11 | Linux (Ubuntu) | MacOS | Notes |
|-|:-:|:-:|:-:|:-:|
| **102esr** | Semi-broken | ? | ? | No Updates |
| **115esr** | ✔️ | Semi-broken | ? | No Updates |
| **120** | ✔️ | ✔️ | ? | |
| **122** | ✔️ | ✔️ | ? | |
## Installation
Open `about:config` and set/create:
* `toolkit.legacyUserProfileCustomizations.stylesheets` to `true`
* `svg.context-properties.content.enabled` to `true`
* `layout.css.has-selector.enabled` to `true`
* `browser.newtabpage.activity-stream.logowordmark.alwaysVisible` to `false`
____
If you're too lazy to copy and paste these `about:config` preferences, you can visit https://zapsnh.github.io/zcpt-configurator/, enable `Include preferences for theme installation`, and generate a `user.js` file that you can put in your profile folder.

Make sure to delete it after you start Firefox so that it doesn't override any changes you make in `about:config`.

Create `security.secure_connection_icon_color_gray` as a boolean and set it to `true` if you don't want the green connection icon.
____
Download the release for your version:
* [Firefox 120](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/main.zip)
* [Firefox 121](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/main.zip)
* [Firefox Nightly](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/nightly.zip)
* [Firefox 115esr](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/115esr.zip)

<details>
	<summary>Older Versions</summary>
	
* [Firefox 99](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/archive-v99.zip)
* [Firefox 116 - 119](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/119.zip)
</details>

_Note: Firefox versions other than the latest versions (nightly, beta/dev, and stable, but NOT esr) will not get feature updates._

Extract the zip and move `zapsCoolPhotonTheme-*` to your profile which you can find by going to `about:support` and opening your profile folder/directory.

Rename `zapsCoolPhotonTheme-*` to `chrome`


Make sure the directory is like this:
* `Profiles` > `your profile` > `chrome`

and not like this:
* `Profiles` > `your profile` > `chrome` > `zapsCoolPhotonTheme-main`

Restart Firefox

# Configuration

## Context menus
In `about:config`, if you want native (Windows) context menus, you can create:
**Note: These context menus have not been tested on platforms other than Windows**
| Config Name | Result | Image |
|-|:-:|:----:|
| `uc.contextmenu.win-10` | Windows 10 styled menu | ![image](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/e4720c5f-ce0c-4178-9b5c-dc60844a265d) |
| `uc.contextmenu.win-11` | Windows 11 styled menu, Also kinda looks the GNOME context menu | ![image](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/7c1c78bf-0b67-410a-85bf-133bdba1fce6) |
| `uc.contextmenu.dark` | Makes the context menu dark | ![image](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/7c1c78bf-0b67-410a-85bf-133bdba1fce6) ![image](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/e4720c5f-ce0c-4178-9b5c-dc60844a265d) |
| `uc.contextmenu.light` | Makes the context menu light | ![image](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/3ee54b09-3c05-420c-9693-4fe5e76f8aa1) ![image](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/e9a1f904-fe21-415e-9421-1d995edc1781) |

If you don't set `uc.contextmenu.light` or `uc.contextmenu.dark`, then the context menu will take the colors from the theme:

![Windows 11 style context menu with the dark Alpenglow theme](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/09246fb9-66ab-4406-bc94-4e46157dd167)

## Megabar
In `about:config`, if you want to reduce the megabar or disable it, create:
| Config Name | Result | Image |
|-|:-:|:-:|
| _none_ | Default Photon Megabar | ![normal](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/ef1bc738-28bf-439b-8c6f-68c188e8e942) |
| `uc.reduced-megabar` | Slightly smaller Proton-sized Megabar | ![reducedmegabar](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/596e4445-ddee-49c9-a4b4-e58da184ea4a) |
| `uc.no-megabar` | No megabar | ![nomegabar](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/a60585ff-d7fe-4ef1-af0c-09269160bc6b) |


## Themes
For themes where the tab color and navbar color are different (and for people who want them to be the same), go to `about:config` and create:
| Config Name | Result | Image |
|-|:-:|:-:|
| _none_ | Default behavior <br><br> Top: Theme in Proton <br> Bottom: Theme with config | ![Normal](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/9e5023be-b76a-4ec1-bfcb-ec693490d4c6) |
| `uc.theme.tab-color-same-as-navbar` | Tab color takes the navbar color <br><br> Top: Theme in Proton <br> Bottom: Theme with config | ![Navbar Color](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/10fdd8a3-895a-4c25-b485-9df1f22d62b4) |
| `uc.theme.navbar-color-same-as-tab` | Navbar color takes the tab color <br><br> Top: Theme in Proton <br> Bottom: Theme with config | ![Tab Color](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/ceee4529-ca7a-48df-83d9-7ce11e7ded92) |

## Tab title text color
If the tab title text color is unreadable with your accent color, go to `about:config` and create:
| Config Name | Result | Image |
|-|:-:|:-:|
| _none_ | Default color | ![whiteonlight](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/4fb2df18-8701-45fc-954e-7de875888f91) |
| `uc.titlebar-accent.darktext` | Dark tab title color | ![blackonlight](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/25c46b14-fb64-4e41-814a-c32a036bf747) |
| `uc.titlebar-accent.lighttext` | Light tab title color | ![lightondark](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/88f1fb0e-8f77-43d7-bd51-b62958096257) |

## Sidebery
There is basic support for [Sidebery](https://github.com/mbnuqw/sidebery). You can turn it on with:
| Config Name | Result | Image |
|-|:-:|:-:|
| `uc.sidebery` | Vertical Tabs | ![image](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/e3514bd2-13d5-4eca-aee6-9415c0f8a97a) |

#### Notes:
- You will need to insert [this](https://gist.github.com/zapSNH/1ad90c69ca59dc7139d9e0454d52728f) into Sidebery's style editor.
- To be able to switch between vertical tabs mode and normal mode, turn on `Add preface to the browser window's title if Sidebery sidebar is active` and set the preface value to `[VT] ` (incl. space at the end).
- Using `uc.reduced-megabar` or `uc.no-megabar` is recommended.
- Set the font-size to `XXS` under the Appearance section. [(where?)](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/af103b3b-d8d7-4a01-93ee-2a1347dca638)
- Set the theme to `plain` under the Appearance section. [(where?)](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/2df7e60f-7ecd-4821-a17c-293f2490d2c5)
- Set the density to `relaxed` under the Appearance section. [(where?)](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/a3c59c99-261a-4727-8438-404a8ad98aa0)

## Bottom Tabs
In `about:config`, you can turn on bottom tabs with:
| Config Name | Result | Image |
|-|:-:|:-:|
| `uc.bottom-tabs` | Bottom Tabs | ![bottombook](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/6071b70b-2ca0-4d10-89a5-c532f24f189c) |
| `uc.bottom-tabs.bookmark-on-top` | Bottom Tabs with bookmarks on top | ![topbook](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/f1f72e70-c736-4ad6-a6f9-9c9b3177187c) |

#### Notes:
- Using `uc.reduced-megabar` or `uc.no-megabar` is recommended.

## New Tab Background
In `about:config`, you can turn on a new tab background with:
| Config Name | Result | Image |
|-|:-:|:-:|
| `uc.newtab.background` | New tab background | ![image](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/1bbda37a-2577-4592-aac7-e8848cb1a30d) |

#### Notes:
- Replace `background.png` in `resources` with your own PNG image.

## Full Width 
In `about:config`, you can turn on full width tabs with:

| Config Name | Result | Image |
|-|:-:|:-:|
| `uc.full-width-tabs` | Full width tabs<br>Can be coupled with `uc.bottom-tabs` if you want the 🤮Safari🤮 look.| ![image](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/6c965793-afb3-488e-b3b3-c6ef46905a71) |

## Tab separators (Firefox ESR)
Sometimes the tab separators go missing. If you want them to show up always then find and remove these lines from `tabs-and-urlbar.css`

```css
.tabbrowser-tab:has(+ .tabbrowser-tab[selected="true"]:not([hidden])) 
.tab-stack::before, :root #firefox-view-button[open] + #tabbrowser-tabs arrowscrollbox > :first-child:not([selected="true"]) .tab-stack::after {
	border-right-color: transparent !important;
}
```

This will result in a separator before the selected tab, so if you don't want that look and are fine with separators sometimes going missing, then don't remove it.

## Misc.
Photon Firefox icons are taken from the `omni.ja` file from Firefox 87.
Some other icons are modified/made by me.

Special thanks to:
- [black7375's Lepton](https://github.com/black7375/Firefox-UI-Fix)
- [YukisCoffee's Phroton](https://github.com/YukisCoffee/phroton/)
- The folks over on r/FirefoxCSS
- [Mozilla](https://www.mozilla.org/) since they made Firefox so customizable (and they made Photon)
- Windows 11 for opening Edge everytime I accidentally press F1 instead of F2 to rename stuff in explorer. I think YOU need to get help Microsoft.


<details>
	<summary>experimental webextension version</summary>
	https://github.com/zapSNH/zcpt-webextension
</details>
