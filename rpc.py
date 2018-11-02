from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
import random

@app.route('/')
def rockpaperscissors():
    return render_template('index.html')

results={'rock':{'paper':'lose', 'rock':'tie', 'scissors':'win'},
'paper':{'paper': 'tie', 'rock' : 'win', 'scissors': 'lose'},
'scissors':{'paper' : 'win', 'rock': 'lose', 'scissors': 'tie'}}

    
def random_weapon():
    weapons=['rock', 'paper', 'scissors']
    print("random is working")
    return weapons[random.randint(0,2)]

@app.route('/results', methods= ['POST'])
def playthegame():
    # weapon_from_form = request.form['weapon']
    # computer_choice=random_weapon()
    # winner = results[weapon_from_form][computer_choice]
    session['weapon_from_form'] = request.form['weapon']
    session['computer_weapon']=random_weapon()
    session['winner'] = results[session['weapon_from_form']][session['computer_weapon']]
        count = 0
        if session['winner'] == 'win'
        count = count +1
    return redirect('/')
    # , winner=winner, computer_weapon=computer_choice, user_weapon=weapon_from_form

if __name__=="__main__":
    app.run(debug=True)