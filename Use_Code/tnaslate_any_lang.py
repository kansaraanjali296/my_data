
from googletrans import Translator

## tanslate of any language in english  please see lang code use this link using src, desc-- https://py-googletrans.readthedocs.io/en/latest/
# and install this pack--[pip install googletrans==3.1.0a0] in cmd

translater = Translator()
any_language = "जोर से बोलना पढना समझना सीखना, साहित्यिक ज्ञान पढाई पढे जाने का ढंग पढना अर्थ पठन, पढा जाना"  ## any language writen
translate_in_eng = translater.translate(any_language, desc="en").text
print(translate_in_eng)

