import os, sys
import xml.etree.ElementTree as ET


version = os.getenv("version")
path = os.getenv("GITHUB_WORKSPACE")

tree = ET.parse( path + '/osu/osu.Android/Properties/AndroidManifest.xml' )

root = tree.getroot()

for elem in root.iter('manifest'):
    elem.set('versionName', str(version))

tree.write(path + '/osu/osu.Android/Properties/AndroidManifest.xml')
sys.exit(0)