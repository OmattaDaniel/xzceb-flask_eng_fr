"""
This moduleis is a Language translator between French and English
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION_LT='2018-05-01'

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(version = VERSION_LT,authenticator = authenticator)
language_translator.set_service_url(URL)
print(language_translator)

def english_to_french(english_text):
    """
    This function translates English to French
    """
    french = language_translator.translate(
    text=english_text, model_id='en-fr')
    translation_2 = french.get_result()
    french_text = translation_2['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    This function translates French to English
    """
    english = language_translator.translate(
    text=french_text, model_id='fr-en').get_result()
    english_text = english['translations'][0]['translation']
    return english_text

# french_translation = english_to_french(
#     "Do reach out to the Stanbic IBTC or Digital Jewels support team if you have any enquiries.")
# print(french_translation)

# english_translation = french_to_english(french_translation)
# print(english_translation)
