from distutils.core import setup
import py2app
import os

plist = dict(
    CFBundleIdentifier="com.giovannipignoni.CWanalysisTool",
    LSMinimumSystemVersion="10.4.0",
    CFBundleShortVersionString="1.0.0",
    CFBundleVersion="1.0.0",
)

dataFiles = ['Resources/English.lproj']

setup(data_files=dataFiles,
      app=[dict(script="analysisTool.py", plist=plist)])
