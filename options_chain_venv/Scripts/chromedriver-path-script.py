#!c:\users\sique\documents\django\rest-framework-options-api\options_chain_venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'chromedriver-binary==111.0.5563.19.0','console_scripts','chromedriver-path'
__requires__ = 'chromedriver-binary==111.0.5563.19.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('chromedriver-binary==111.0.5563.19.0', 'console_scripts', 'chromedriver-path')()
    )
