import config
import os, sys

lv = config.lastversion

if os.getenv("lv") != lv:
    config.lastversion = os.getenv("lv")
    sys.exit(0)
else:
    sys.exit(1)
