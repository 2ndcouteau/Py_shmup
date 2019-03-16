rm -rf build dist

pyinstaller Pyshmup_linux.spec

cd dist
./Pyshmup
