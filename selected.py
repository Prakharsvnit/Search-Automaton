import os
import webbrowser

new = 2 # open in a new tab, if possible
var = os.popen('xsel').read()

url = "https://google.com/search?q=" + var
webbrowser.open(url,new=new)