# Hello World 2019 Alexa Skill
# Provides information about the CUhackit Hello World '19 hackathon event.
# Copyright (C) 2019 Ben Godfrey
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import alexa
import random
import logging

sample_questions = [
    "When is the hackathon?",
    "What time is cup stacking?",
    "What time is judging?"
]

def handle_request_launch(request: alexa.Request, logger: logging.Logger) -> alexa.Response:
    response = alexa.Response()

    response.speech = "Hi there! You've successfully launched the Clemson Canvas skill. "
    response.speech += "You can ask me questions about your grades, classes, homework assignments on Canvas. What do you want to know?"

    response.end_session = False

    return response


def handle_intent_help(request: alexa.IntentRequest, logger: logging.Logger) -> alexa.Response:
    response = alexa.Response()

    response.speech = "You can ask me basic questions about the hackathon. For example, try asking: "
    response.speech += random.choice(sample_questions)

    return response


# def handle_intent_what_day(request: alexa.IntentRequest, logger: logging.Logger) -> alexa.Response:
#     response = alexa.Response()

#     response.speech = "CU hack-it Hello World 2019 will take place on Saturday, October 19th, 2019."

#     return response


# def handle_intent_event_time(request: alexa.IntentRequest, logger: logging.Logger) -> alexa.Response:
#     response = alexa.Response()

#     event_id = request.id_value_of_slot("event_name")

#     if event_id is None or event_id not in hackathon_events:
#         response.speech = "Sorry, I don't have information about that event."
#         return response
    
#     event_details = hackathon_events[event_id]
#     event_time = event_details[0]
#     event_name = event_details[1]

#     response.speech = "{} is at {}.".format(event_name, event_time)

#     return response


def handle_intent_stop_cancel(request: alexa.IntentRequest, logger: logging.Logger) -> alexa.Response:
    response = alexa.Response()

    response.speech = "Goodbye."

    return response


request_handlers = {
    alexa.Request.TYPE_LAUNCH: handle_request_launch,
}

intent_handlers = {
    alexa.Request.INTENT_FALLBACK: handle_intent_help,
    alexa.Request.INTENT_HELP: handle_intent_help,
    alexa.Request.INTENT_CANCEL: handle_intent_stop_cancel,
    alexa.Request.INTENT_STOP: handle_intent_stop_cancel
    
}
 
router = alexa.Router(request_handlers, intent_handlers)
lambda_handler = router.handle_request
