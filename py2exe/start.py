from components.py2exe import py2exe

#insert filename here.
install = py2exe("your-file.py")
install.pre_install()
install.installing()
install.posthandling()

