import version
import os, sys

lv = version.lastversion

if os.getenv("lv") != lv:
    config.lastversion = os.getenv("lv")
    print("New Version found !")
    sys.exit(0)
else:
    print("No new Version found...")
    sys.exit(1)
