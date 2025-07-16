import sys
import re

def create_relnotes(ver):
	current_esr = "v" + open(".github/workflows/ESR_VERSION", 'r').read()
	ver_num_only_esr = re.match(r'^v(\d+)', current_esr).group(1)

	notes = \
f'''# zapsCoolPhotonTheme for Firefox {ver_num_only_esr}esr
Based on zapsCoolPhotonTheme v{ver_num_only_esr} for Firefox {current_esr}esr.

### Changes
* Removed the aero fog in the titlebar for Windows 7 (#31)
* The tab highlight is now also aligned in all modes (i think)

____
**Full Changelog**: https://github.com/zapSNH/zapsCoolPhotonTheme/compare/v128...{ver}'''
	f = open('relnotes.md', 'w')
	f.write(notes)
	f.close()

if __name__ == '__main__':
    a, b, c = sys.argv[1], sys.argv[2], sys.argv[3]
    create_relnotes(a, b, c)