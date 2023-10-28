# Zap's Cool Photon Theme (Firefox 116 - 119)
A userChrome designed to be as faithful to Firefox Photon (specifically Firefox 87) as possible.

![it's cool](https://github.com/zapSNH/zapsCoolPhotonTheme/assets/134786889/5b0dbcc3-78f2-497e-a949-39f0fdfa63cf)
____

#### Compatibility
| | Windows 10/11 | Linux (Ubuntu) | MacOS |
|-|:-:|:-:|:-:|
| **119** | ✔️ | ✔️ | ? |
## Installation
Open `about:config` and set/create:
* `toolkit.legacyUserProfileCustomizations.stylesheets` to `true`
* `svg.context-properties.content.enabled` to `true`
* `layout.css.has-selector.enabled` to `true`
* `uc.reduced-megabar` to `false`
* `browser.newtabpage.activity-stream.logowordmark.alwaysVisible` to `false`

Switching `uc.reduced-megabar` to `true` reduces the size of the megabar to Proton's size. Yes, the highlighted/open megabar is smaller in Proton.

Create `security.secure_connection_icon_color_gray` as a boolean and set it to `true` if you don't want the green connection icon.

Download the release for your version:
* [Firefox 116 - 119](https://github.com/zapSNH/zapsCoolPhotonTheme/archive/refs/heads/main.zip)

Extract the zip and move `zapsCoolPhotonTheme-119` to your profile which you can find by going to `about:support` and opening your profile folder/directory.

Rename `zapsCoolPhotonTheme-119` to `chrome`

Make sure the directory is like this:
* `Profiles` > `your profile` > `chrome`

and not like this:
* `Profiles` > `your profile` > `chrome` > `zapsCoolPhotonTheme-main`

Restart Firefox

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
- You will need to (re)move Firefox View and any other buttons in the tabbar to the navigation bar.

## Misc.
Photon Firefox icons are taken from the `omni.ja` file from Firefox 87.
Some other icons are modified/made by me.

Special thanks to:
- [black7375's Lepton](https://github.com/black7375/Firefox-UI-Fix)
- [YukisCoffee's Phroton](https://github.com/YukisCoffee/phroton/)
- The folks over on r/FirefoxCSS
- [Mozilla](https://www.mozilla.org/) since they made Firefox so customizable (and they made Photon)
- Windows 11 for opening Edge everytime I accidentally press F1 instead of F2 to rename stuff in explorer. I think YOU need to get help Microsoft.
