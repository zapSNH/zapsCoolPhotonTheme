import sys

def create_relnotes(ver_v):
	current_esr = open(".github/workflows/ESR_VERSION", 'r').read()
	ver = ver_v.replace("v", "")
	ver_string = "v" + str(int(ver)-1) + "...v" + ver
	notes = \
f'''# zapsCoolPhotonTheme for Firefox {ver} and Firefox {current_esr}esr
`zapsCoolPhotonTheme-v{ver}.zip` is for Firefox {ver}.
`zapsCoolPhotonTheme-v{ver}-esr.zip` is for Firefox {current_esr}esr.

### Changes
* TBA
____

Corresponding Webextension Version: [v0.0.0](https://github.com/zapSNH/zcpt-webextension/releases/tag/v0.0.0)

____
**Full Changelog**: https://github.com/zapSNH/zapsCoolPhotonTheme/compare/{ver_string}'''
	f = open('relnotes.md', 'w')
	f.write(notes)
	f.close()

if __name__ == '__main__':
	globals()[sys.argv[1]](sys.argv[2])