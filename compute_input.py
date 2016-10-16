## compute_input.py
import sys, json, numpy as np
from pb_py import main as API

host = 'aiaas.pandorabots.com'
user_key = '07d5b4bc9c18a5acb8b4fe15060d5898'
app_id = '1409613157940'
bot_list = ['test', 'callmom', 'squarebear']

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    lines = read_in()
    
    #lines contains [user string, bot_choice]
    info = lines
    #print "kappa"
    #SEEMS TO SPEFICALLY THE CLEVERBOT thing
    bot_response = js_respond(info[0], info[1])
    print (bot_response)
    
def js_respond(response, bot_choice):
    bot_name = ''
    if bot_choice == 1:
        return "NYI"
    else:
        if bot_choice == 2:
            bot_name = bot_list[0]
        elif bot_choice == 3:
            bot_name = bot_list[1]
        else:
            bot_name = bot_list[2]
        result = API.talk(user_key, app_id, host, bot_name, response, recent=True)
        bot_response = result['response']
        return bot_response
    

#start process
if __name__ == '__main__':
    main()
