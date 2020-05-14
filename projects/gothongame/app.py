from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothongame import planisphere

app = Flask(__name__)
app.config['TESTING'] = True
app.secret_key = '12341234' #if I was to post this on the web I'd need a real secret key, not this bs

@app.route('/')
def index():
    print('='*30)
    print(session)
    print('='*30)
    session['room_name'] = planisphere.START #initialize the session with central_corridor
    return redirect(url_for('game')) #and then immediately send the user to the game URL

@app.route('/game', methods=['GET','POST']) #this is the main url where everything is happening
def game():
    print('-'*30)
    print(session)
    print('-'*30)

    room_name = session.get('room_name') #because session is dictionary, we use get to fetch the room name, which is a string of the form laser_weapon_armory

    if request.method == 'GET':
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template('show_room.html', room=room)
        else:
            #why is this here? do you need it?
            return render_template('you_died.html')
            #i think this is a catchall for all possible failures / cheats - if we cant find the room in the dictionary, you die and ahve to sart all over
    else: #ie POST!
        action = request.form.get('action') #we receive the request from action form

        if room_name and action:
            #setup the room
            room = planisphere.load_room(room_name)
            #store the next room in this variable
            next_room = room.go(action)

            if not next_room: #in other words if you died or won
                session['room_name'] = planisphere.name_room(room)
            else:
                session['room_name'] = planisphere.name_room(next_room)

        return redirect(url_for('game'))

if __name__ == "__main__":
    app.run()


"""
ok I think I get it
we basically constantly update the "room_name" variable with next room (which could be actually next room or simply death)
and we redirect the user back to /game during each update

the way we get user input is from a form that uses POST and sends it to our server
their input determines what next room they go into (as coded in planisphere)
if they type in the right commands they go all the way through until they the_end_winner
if they make the mistake at any point during the game, they end up in generic_death
if they pick the wrong pod at the end, the die from the_end_loser

not too sure about:
why * doesn't seem to work right (ie how do I accept any other input?)
what is the role of you_died.html? It would be loaded only if we somehow issued a get request without a room_name?
"""
