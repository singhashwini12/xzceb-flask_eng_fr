"""
Module for language Translation via IBM Watson Services
"""

import json
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

try:
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)

    #language_translator.set_disable_ssl_verification(True)

except ApiException as ex:
    print("Method failed with status code " + str(ex.code) + ": " + ex.message)

def english_to_french(english_text):
    """This function takes Enligh text as input and returns its French translation"""

    if len(english_text)>0:
        french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        return french_text["translations"]

def french_to_english(french_text):
    """This function takes French text as input and returns its English translation"""

    if len(french_text)>0:
        english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        return english_text["translations"]
