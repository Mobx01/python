import pandas as pd

df = pd.read_csv("pokemon.csv")

#filtering = keeping row that matches a  condition

#filter pokemon having height more than 2

tall_pokemon = df[df["Height"] >= 2]
print(tall_pokemon)

#pokemon having weight more than 350
heavy_pokemon = df[df["Weight"] >= 350 ]
print(heavy_pokemon)

#leagendry pokemon
leg_pokemon = df[df["Legendary"] == 1] #alternative - df[df["Legendary"] == True]
print(leg_pokemon)

#water pokemons
water_pok = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
print(water_pok)