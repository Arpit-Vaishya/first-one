def moneyheist():
    print("Money Heist is a popular Spanish television series.")
    characters = ['Tokyo', 'Berlin', 'Nairobi', 'Rio', 'Denver', 'Moscow','Helsinki', 'Lisbon', 'Stockholm', 'Palermo', 'Bogotá', 'Marseille','professor']
    names = ['seria olivera', 'Pedro Alonso', 'Alba Flores', 'Miguel Herrán', 'Jaime Lorente', 'Paco Tous','Darko Peric', 'Itziar Ituño', 'Esther Acebo', 'Rodrigo de la Serna', 'Hovik Keuchkerian', 'Luka Peroš','Álvaro Morte']
    for index, character in enumerate(characters):
        name=names[index]
        print(f"{index}: {character} played by {name}")


if __name__ == "__main__":
    moneyheist()
