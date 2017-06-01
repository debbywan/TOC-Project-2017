import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '378813989:AAFxa3Eel9eCzSRA6rQ-qN17jQpbCoSQ74Y'
WEBHOOK_URL = 'https://86d8424e.ngrok.io/hook/'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'start',
        'user',
        'state1',
        'state2',
        'state3',
        'state11',
        'state12',
        'state21',
        'state22',
        'state23',
        'state24',
        'state25',
        'state211',
        'state221',
        'state222',
        'state223',
        'state231',
        'state241',
        'state242',
        'state251',
        'state252'
        #'state4'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'user',
            'conditions': 'is_going_to_user'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state11',
            'conditions': 'is_going_to_state11'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state12',
            'conditions': 'is_going_to_state12'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state21',
            'conditions': 'is_going_to_state21'
        },
        {
            'trigger': 'advance',
            'source': 'state21',
            'dest': 'state211',
            'conditions': 'is_going_to_state211'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state22',
            'conditions': 'is_going_to_state22'
        },
        {
            'trigger': 'advance',
            'source': 'state22',
            'dest': 'state221',
            'conditions': 'is_going_to_state221'
        },
        {
            'trigger': 'advance',
            'source': 'state22',
            'dest': 'state222',
            'conditions': 'is_going_to_state222'
        },
        {
            'trigger': 'advance',
            'source': 'state22',
            'dest': 'state223',
            'conditions': 'is_going_to_state223'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state23',
            'conditions': 'is_going_to_state23'
        },
        {
            'trigger': 'advance',
            'source': 'state23',
            'dest': 'state231',
            'conditions': 'is_going_to_state231'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state24',
            'conditions': 'is_going_to_state24'
        },
        {
            'trigger': 'advance',
            'source': 'state24',
            'dest': 'state241',
            'conditions': 'is_going_to_state241'
        },
        {
            'trigger': 'advance',
            'source': 'state24',
            'dest': 'state242',
            'conditions': 'is_going_to_state242'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state25',
            'conditions': 'is_going_to_state25'
        },
        {
            'trigger': 'advance',
            'source': 'state25',
            'dest': 'state251',
            'conditions': 'is_going_to_state251'
        },

        {
            'trigger': 'advance',
            'source': 'state25',
            'dest': 'state252',
            'conditions': 'is_going_to_state252'
        },

        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        #{
            #'trigger': 'advance',
            #'source': 'user',
            #'dest': 'state4',
            #'conditions': 'is_going_to_state4'
        #},
        {
            'trigger': 'go_back',
            'source': [
                #'state11',
                #'state12',
                'state211',
                #'state221',
                #'state222',
                #'state223',
                'state231',
                #'state241',
                #'state242',
                #'state251',
                #'state252',
                'state3'
                #'state4'
            ],
            'dest': 'user'
        },
        {
            'trigger': 'advance',
            'source': [
                'state11',
                'state12'
               ],
            'dest': 'state1',
            'conditions': 'back_to_state1'
        },
         {
            'trigger': 'advance',
            'source': [
                'user',             
               ],
            'dest': 'start',
            'conditions': 'back_to_start'
        },
        {
            'trigger': 'advance',
            'source': [
                'state221',
                'state222',
                'state223'
               ],
            'dest': 'state22',
            'conditions': 'back_to_state22'
        },
       
        {
            'trigger': 'advance',
            'source': [
                'state241',
                'state242'
               ],
            'dest': 'state24',
            'conditions': 'back_to_state24'
        },
        {
            'trigger': 'advance',
            'source': [
                'state251',
                'state252'
               ],
            'dest': 'state25',
            'conditions': 'back_to_state25'
        },
        {
            'trigger': 'advance',
            'source': [
                'state11',
                'state12',
                'state221',
                'state222',
                'state223',   
                'state241',
                'state242', 
                'state251',
                'state252'    
            ],
            'dest': 'user',
            'conditions': 'end'
        }
       
        
    ],
    initial='start',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook/', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
app.run()
