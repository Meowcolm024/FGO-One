from interface.Major import Major
import pytesseract


s = Major()
out = s.recognize()
print(out)
