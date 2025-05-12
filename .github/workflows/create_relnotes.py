import sys
import re

def create_relnotes(ver, prev_ver, ext_ver):
	current_esr = "v" + open(".github/workflows/ESR_VERSION", 'r').read()
	ver_num_only = re.match(r'^v(\d+)', ver).group(1)
	ver_num_only_esr = re.match(r'^v(\d+)', current_esr).group(1)

	notes = \
f'''# zapsCoolPhotonTheme for Firefox {ver_num_only} and Firefox {ver_num_only_esr}esr
`zapsCoolPhotonTheme-{ver}.zip` is for Firefox {ver_num_only}.
`zapsCoolPhotonTheme-{ver}-esr.zip` is for Firefox {ver_num_only_esr}esr.

### Changes
* TBA
____

Corresponding Webextension Version: [{ext_ver}](https://github.com/zapSNH/zcpt-webextension/releases/tag/{ext_ver})

____
**Full Changelog**: https://github.com/zapSNH/zapsCoolPhotonTheme/compare/{prev_ver}...{ver}'''
	f = open('relnotes.md', 'w')
	f.write(notes)
	f.close()

if __name__ == '__main__':
    a, b, c = sys.argv[1], sys.argv[2], sys.argv[3]
    create_relnotes(a, b, c)