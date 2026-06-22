from flask import Flask, render_template, redirect
import random

app = Flask(__name__)

weapon_count = {
    "starbreaker": 0,
    "nebula_slash": 0,
    "starfall_missile": 0,
    "solar_burst": 0,
    "void_reaper": 0,
    "eclipse_cannon": 0
}
weapon_damage = {
    "starbreaker": 20,
    "nebula_slash": 15,
    "starfall_missile": 25,
    "solar_burst": 10,
    "void_reaper": 30,
    "eclipse_cannon": 35
}
weapon_names = {
    "starbreaker": "NOVA ☄️",
    "nebula_slash": "NEXUS ⚔️",
    "starfall_missile": "STRIKE 🚀",
    "solar_burst": "BLAZE 🔥",
    "void_reaper": "VOID ⚡",
    "eclipse_cannon": "ECLIPSE 🌌"
}

player_health = 100
ai_health = 100
game_mode = "easy"

round_count = 0
max_rounds = 5


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/difficulty")
def difficulty():
    return render_template("difficulty.html")


@app.route("/start")
def start():

    return render_template(
        "index.html",
        player="",
        ai="",
        player_weapon_name="",
        ai_weapon_name="",
        result="",
        counts=weapon_count,
        favorite="",
        analysis="",
        player_health=player_health,
        ai_health=ai_health,
        round_count=round_count,
        max_rounds=max_rounds
    )


@app.route("/easy")
def easy():

    global game_mode

    game_mode = "easy"

    return render_template(
        "index.html",
        player="",
        ai="",
        player_weapon_name="",
        ai_weapon_name="",
        result="",
        counts=weapon_count,
        favorite="",
        analysis="Easy Mode Selected",
        player_health=player_health,
        ai_health=ai_health,
        round_count=round_count,
        max_rounds=max_rounds
    )


@app.route("/hard")
def hard():

    global game_mode

    game_mode = "hard"

    return render_template(
        "index.html",
        player="",
        ai="",
        player_weapon_name="",
        ai_weapon_name="",
        result="",
        counts=weapon_count,
        favorite="",
        analysis="Hard Mode Selected",
        player_health=player_health,
        ai_health=ai_health,
        round_count=round_count,
        max_rounds=max_rounds
    )


@app.route("/play/<weapon>")
def play(weapon):

    global player_health
    global ai_health
    global round_count

   
    weapon_count[weapon] += 1

    round_count += 1

    if round_count >= max_rounds:

        if player_health > ai_health:
            result = "PLAYER VICTORY"

        elif ai_health > player_health:
            result = "AI VICTORY"

        else:
            result = "DRAW"

        return render_template(
            "winner.html",
            result=result,
            player_health=player_health,
            ai_health=ai_health
        )

    favorite = max(
        weapon_count,
        key=weapon_count.get
    )

    weapons = [
    "starbreaker",
    "nebula_slash",
    "starfall_missile",
    "solar_burst",
    "void_reaper",
    "eclipse_cannon"
    ]


    if game_mode == "easy":
        ai_weapon = random.choice(weapons)
    else:
        counters = {
            "starbreaker": "void_reaper",
            "nebula_slash": "eclipse_cannon",
            "starfall_missile": "starbreaker",
            "solar_burst": "nebula_slash",
            "void_reaper": "solar_burst",
            "eclipse_cannon": "starfall_missile"
    }

        ai_weapon = counters[favorite]

    player_weapon_name = weapon_names[weapon]

    ai_weapon_name = weapon_names[ai_weapon]

    if weapon == ai_weapon:

        result = "Draw"

    else:

        player_wins = {
            "starbreaker": ["nebula_slash", "starfall_missile"],
            "nebula_slash": ["starfall_missile", "solar_burst"],
            "starfall_missile": ["solar_burst", "void_reaper"],
            "solar_burst": ["void_reaper", "eclipse_cannon"],
            "void_reaper": ["eclipse_cannon", "starbreaker"],
            "eclipse_cannon": ["starbreaker", "nebula_slash"]
        }

        if ai_weapon in player_wins[weapon]:

            damage = weapon_damage[weapon]

            ai_health -= damage

            if ai_health < 0:
                ai_health = 0

            result = f"You Hit AI (-{damage} HP)"

        else:

            damage = weapon_damage[ai_weapon]

            player_health -= damage

            if player_health < 0:
                player_health = 0

            result = f"AI Hit You (-{damage} HP)"
    return render_template(
        "index.html",
        player=weapon,
        ai=ai_weapon,
        player_weapon_name=player_weapon_name,
        ai_weapon_name=ai_weapon_name,
        result=result,
        counts=weapon_count,
        favorite=favorite,
        analysis=f"Player prefers {favorite} → Switching defense strategy",
        player_health=player_health,
        ai_health=ai_health,
        round_count=round_count,
        max_rounds=max_rounds
    )



@app.route("/reset")
def reset():

    global player_health
    global ai_health
    global round_count
    global weapon_count

    player_health = 100
    ai_health = 100
    round_count = 0

    weapon_count = {
        "starbreaker": 0,
        "nebula_slash": 0,
        "starfall_missile": 0,
        "solar_burst": 0,
        "void_reaper": 0,
        "eclipse_cannon": 0
    }

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
