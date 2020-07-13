from flask import Flask, render_template, request, url_for, redirect
import os
import random
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        details = request.form
        player_result  = details['p_league1']
        team_result = details['t_league1']
        print(player_result + " " +  team_result)
        if player_result == 'true':
            with open('application/textfiles/players.txt') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    player = str(row[random.randint(0,5)])
                    print(player)
                    
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)

