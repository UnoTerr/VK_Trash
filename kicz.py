import vk_requests
import sys
import getpass

#True LogIn
n = raw_input('Enter UserName:  ')
p = getpass.getpass('Enter PassWord: ')
appid = #YOURAPPID
api = vk_requests.create_api(app_id = appid, login = n, password = p, scope = 'offline,messages')

try:
        while True:
                mes = raw_input('--> ')
                api.messages.send(user_id = 'id', message = mes);               
except KeyboardInterrupt:
        pass
        print "Interrupted by user"
        sys.exit()

