import shutil

path = "C:\\Users\\Arad Sheybak\\Desktop\\letterToArad.txt"
path2 = "C:\\Users\\Arad Sheybak\\Desktop\\letterTo.txt"
path3 = "C:\\Users\\Arad Sheybak\\Desktop\\letter.txt"

shutil.copyfile('letterToArad', path)
shutil.copy('letterToArad', path2)
shutil.copy2('letterToArad', path3)
