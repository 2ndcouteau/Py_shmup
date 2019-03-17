rm -rf build dist

pyinstaller Pyshmup_mac.spec

cd dist
./Pyshmup_mac
