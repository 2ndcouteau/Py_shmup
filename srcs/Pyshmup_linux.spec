# -*- mode: python -*-
import os

HOME = os.environ['HOME']
PATH = HOME + "/z/py_shmup/srcs"

block_cipher = None

a = Analysis(['main.py'],
			 pathex=[PATH],
			 binaries=[],
			 datas=[
			 ('*', 'media/'),
			 ('*', 'media/images/'),
			 ('*', 'media/sounds/'),
			 ],
			 hiddenimports=[],
			 hookspath=[],
			 runtime_hooks=[],
			 excludes=[],
			 win_no_prefer_redirects=False,
			 win_private_assemblies=False,
			 cipher=block_cipher,
			 noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
			 cipher=block_cipher)
exe = EXE(pyz,
		  a.scripts,
		  a.binaries,
		  a.zipfiles,
		  a.datas,
		  [],
		  name='Pyshmup',
		  debug=False,
		  bootloader_ignore_signals=False,
		  strip=False,
		  upx=True,
		  runtime_tmpdir=None,
		  console=False )
