# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionSetUserName(Action):
    def name(self) -> Text:
        return "set_username"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        usernm = tracker.get_slot("username")
        msg = "Nice to talk to you "
        dispatcher.utter_message(text="Hello {}:{}".format(usernm, msg))

        return [SlotSet(("username", usernm))]

class ActionSetNewsLetter(Action):
    def mail(self) -> Text:
        return "set_newsletter"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        usermel = tracker.get_slot("usermail")
        msg = " has been subscribed to newsletter successfully "
        dispatcher.utter_message(text="Great, {}:{}".format(usermel, msg))

        return [SlotSet(("usermail", usermel))]
