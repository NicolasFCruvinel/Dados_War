import PyInstaller.__main__
import os
    
PyInstaller.__main__.run([  
     'name-%s%' % 'dadosWar.exe',
     '--onefile -w',
     '--windowed',
     os.path.join('\Users\Nicolas Cruvinel\Problemas II\War', 'dadosWar.py'),                                      
])