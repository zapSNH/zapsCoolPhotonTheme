'''# zapsCoolPhotonTheme for Firefox 126 and Firefox 115.11esr
`zapsCoolPhotonTheme-v126.zip` is for Firefox 126.
`zapsCoolPhotonTheme-115esr.zip` is for Firefox 115esr.

### Changes
* Add `uc.always-show-close-button` which always shows the tab close button even when overflowing.(#3)
* The sidebar should now respect your color theme. (#4)
* Search bar has now been photonized.
* Padding adjustements and fixes.
* Other fixes for Firefox 127.
____

Corresponding Webextension Version: [v0.0.0](https://github.com/zapSNH/zcpt-webextension/releases/tag/v0.0.0)

____
**Full Changelog**: https://github.com/zapSNH/zapsCoolPhotonTheme/compare/v125...v126'''
import sys

def create_relnotes(ver_v):
	ver = ver_v.replace("v", "")
	notes = \
f'''# zapsCoolPhotonTheme for Firefox {ver} and Firefox 115esr
`zapsCoolPhotonTheme-v{ver}.zip` is for Firefox {ver}.
`zapsCoolPhotonTheme-v{ver}-esr.zip` is for Firefox 115esr.

### Changes
* TBA
____

Corresponding Webextension Version: [v0.0.0](https://github.com/zapSNH/zcpt-webextension/releases/tag/v0.0.0)

____
**Full Changelog**: https://github.com/zapSNH/zapsCoolPhotonTheme/compare/v{str(int(ver)-1)}...v{ver}'''
	f = open('relnotes.md', 'w')
	f.write(notes)
	f.close()

if __name__ == '__main__':
	globals()[sys.argv[1]](sys.argv[2])