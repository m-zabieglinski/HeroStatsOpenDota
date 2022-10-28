from flask import Flask, render_template
import hero_pick_win

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/plot/<plot_name>")
def premade_plot(plot_name):
    return render_template("hero_plot.html",
                           name = plot_name,
                           url = f"/static/images/{plot_name}.png")
    
@app.route("/plot/stats/<rank_key>")
def stats_plot(rank_key):
    hero_pick_win.plot_hero_stats(rank_key)
    return render_template("stats_plot.html",
                           name = f"Hero total picks and winrate in {rank_key.capitalize()}",
                           url = f"/static/images/{rank_key}_stats.png")
if __name__ == "__main__":
    app.run()
