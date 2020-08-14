import os, sys
import yaml

version = os.getenv("version")
path = os.getenv("GITHUB_WORKSPACE")

with open(path + "/osu/apktool.yml") as f:
     filechange = yaml.load(f, Loader=yaml.FullLoader)

filechange["versionInfo"]["versionName"] = version

with open(path + "/osu/apktool.yml", "w") as f:
    yaml.dump(filechange, f)        
sys.exit(0)
