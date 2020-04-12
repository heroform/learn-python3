from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planishere

app = Flask(__name__)

@app.route("/")
def index():
    # This is used to "setup" the session with starting values
    session['room_name'] = planishere.START
    return redirect(url_for("game"))
    
@app.route('/game', methods=['POST', 'GET'])
def game():
    room_name = session.get('room_name')
    
    if request.method == "GET":
        if room_name:
            room = planishere.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            # Why is there here? Do you need it? Yes
            return render_template("you_died.html")
    else:
        action = request.form.get('action')
        
        if room_name and action:
            room = planishere.load_room(room_name)
            next_room = room.go(action)
            
            if not next_room:
                session['room_name'] = planishere.name_room(room)
            else:
                session['room_name'] = planishere.name_room(next_room)
                
        return redirect(url_for("game"))
        
# You should change this if you put onn the internet
app.secret_key = 'abczxy'
    
if __name__=="__main__":
    app.run()
