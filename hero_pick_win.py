#OPENDOTA STATS
import requests
import pandas as pd
   
hero_stats_call = requests.get("https://api.opendota.com/api/heroStats")
hero_stats = hero_stats_call.json()
hero_stats_df = pd.DataFrame.from_dict(hero_stats)
hero_stats_df["pro_winrate"] = hero_stats_df["pro_win"] / hero_stats_df["pro_pick"]


#PLOTTING
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(rc = {"axes.facecolor": "lightblue", "figure.facecolor": "lightgrey"})

plt.figure(figsize = (20, 20))
p1 = sns.scatterplot(data = hero_stats_df, x = "pro_pick", y = "pro_winrate", s = 100, color = "white")
for _, hero in hero_stats_df.iterrows():
    p1.text(hero.pro_pick + 0.01, hero.pro_winrate + 0.003, s = hero.localized_name,
            size = "medium", color = "black", weight = "semibold")
    
plt.title("Hero pick and wirrate in pro matches")
plt.xlabel("Total times picked")
plt.ylabel("Winrate") 
plt.axhline(y = 0.5, color = "black", linestyle = "-", linewidth = "2")

#without meepo
hero_stats_no_meepo = hero_stats_df[hero_stats_df["localized_name"] != "Meepo"]
plt.figure(figsize = (20, 20))
p1 = sns.scatterplot(data = hero_stats_no_meepo, x = "pro_pick", y = "pro_winrate", color = "white")
for _, hero in hero_stats_no_meepo.iterrows():
    p1.text(hero.pro_pick + 0.01, hero.pro_winrate + 0.003, s = hero.localized_name,
            size = "medium", color = "black", weight = "semibold")
    
plt.title("Hero pick and winrate in pro matches")
plt.xlabel("Total times picked")
plt.ylabel("Winrate")
plt.axhline(y = 0.5, color = "black", linestyle = "-", linewidth = "2")


# #PICTURES
# import requests

# for _, hero in hero_stats_df.iterrows():
#     name = hero["localized_name"]
#     img_data = requests.get(f"https://static.wikia.nocookie.net/dota2_gamepedia/images/2/26/{name}_icon.png").content
#     with open(f"hero_icons/{name}.png", 'wb') as handler:
#         handler.write(img_data)


