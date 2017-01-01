from components.py2exe import py2exe

#insert filename here.
install = py2exe("anime-tracker.py")
install.installing()
install.posthandling()

