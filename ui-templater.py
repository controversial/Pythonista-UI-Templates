import editor
import os
import dialogs
import shutil

curdir=os.path.dirname(editor.get_path())

options=["iPads (non pro)",
		  "iPad Pro",
		  "iPhone 4, iPhone 4S",
		  "iPhone 5, iPhone 5S",
		  "iPhone 6, iPhone 6S",
		  "iPhone 6+, iPhone 6S+",
]

pyuiFiles=[
			"ipads-non-pro.pyui",
			"ipad-pro.pyui",
			"iphone-4,4S.pyui",
			"iphone-5,5S.pyui",
			"iphone-6,6S.pyui",
			"iphone-6+,iphone-6S+.pyui",
]

mapChoicesToFiles=dict(zip(options,pyuiFiles))

title="Choose a screen size"
choice=mapChoicesToFiles[ dialogs.list_dialog(title,options) ]

shutil.copy(choice,os.path.join(curdir,choice))
