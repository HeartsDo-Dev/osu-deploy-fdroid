import os, sys
import yaml

version = os.getenv("version")
path = os.getenv("GITHUB_WORKSPACE")

def meta_constructor(loader, node):
    value = loader.construct_mapping(node)
    return value

yaml.add_constructor(u'tag:yaml.org,2002:brut.androlib.meta.MetaInfo', meta_constructor)

with open(path + "/osu/apktool.yml") as f:
     filechange = yaml.load(f, Loader=yaml.FullLoader)

filechange["versionInfo"]["versionName"] = version

with open(path + "/osu/apktool.yml", "w") as f:
    yaml.dump(filechange, f)        
sys.exit(0)
