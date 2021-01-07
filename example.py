from navajo import navajoCodeTranslator

translator = navajoCodeTranslator()

text = "Than-zie lin dzeh No-da-ih nesh-chee tkin than-zie dzeh be Dibeh than-zie wol-la-chee than-zie dzeh dibeh Ma-e dibeh-yazzi dzeh dzeh than-zie Gloe-ih tkin dibeh-yazzi dibeh-yazzi Wol-la-chee than-zie than-zie wol-la-chee moashi klizzie-yazzi Na-as-tso-si tkin be gloe-ih wol-la-chee tsah-as-zih Tkin dibeh dibeh-yazzi wol-la-chee nesh-chee be Ma-e no-da-ih dibeh-yazzi dibeh-yazzi Ma-e ne-ash-jsn gah moashi dzeh Tkin nesh-chee Than-zie gloe-ih ne-ash-jsn Gloe-ih dzeh dzeh klizzie-yazzi dibeh Than-zie tkin na-as-tso-si dzeh. Gloe-ih dzeh Gloe-ih tkin dibeh-yazzi dibeh-yazzi Nesh-chee dzeh dzeh be Wol-la-chee dibeh Na-as-tso-si no-da-ih moashi lin Na-as-tso-si tkin dibeh-yazzi tkin than-zie wol-la-chee gah tsah-as-zih Bi-sodih dzeh gah dibeh ne-ash-jsn nesh-chee nesh-chee dzeh dibeh-yazzi Wol-la-chee dibeh Moashi wol-la-chee nesh-chee Shush dzeh Dibeh bi-sodih wol-la-chee gah dzeh be, Wol-la-chee dibeh Gloe-ih dzeh dibeh-yazzi dibeh-yazzi Wol-la-chee dibeh Wol-la-chee nesh-chee Tkin nesh-chee moashi gah dzeh wol-la-chee dibeh dzeh Tkin nesh-chee Na-as-tso-si dzeh be tkin moashi wol-la-chee dibey-yazzi Dibeh no-da-ih bi-sodih bi-sodih dibeh-yazzi tkin dzeh dibeh, Klizzie-yazzi Gah wol-la-chee than-zie tkin ne-ash-jsn nesh-chee dibeh, Gloe-ih dzeh wol-la-chee bi-sodih ne-sh-jsn nesh-chee dibeh, Wol-la-chee nesh-chee be Wol-la-chee na-as-tso-si na-as-tso-si ne-ash-jsn. Than-zie lin tkin dibeh Tkin dibeh Than-zie ne-ash-jsn bi-sodih Dibeh dzeh moashi gah dzeh than-zie. Wol-la-chee debeh-yazzi debeh-yazzi Lin wol-la-chee nesh-chee be dibeh Ne-ash-jsn nesh-chee Be dzeh moashi klizzie-yazzi. Than-zie lin wol-la-chee nesh-chee klizzie-yazzi Tsah-as-zih ne-ash-jsn no-da-ih Ma-e ne-ash-jsn gah Tsah-as-zih ne-ash-jsn no-da-ih gah Moashi ne-ash-jsn ne-ash-jsn bi-sodih dzeh gah wol-la-chee than-zie tkin ne-ash-jsn nesh-chee"

translated_text = translator.translate_code(text.lower())
print(translated_text)

translator = morseCodeTranslater()
text = "This string has been translated to morse code and back again"

# Translate text to morse code
morse = translator.translate_text(text)
# Translate morse code to text
translated_text = translator.translate_morse(morse)

print(morse)
print(translated_text)
