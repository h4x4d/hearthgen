from hearthgen import create_card, CardCreator

create_card(
    card_type='spell',
    save_name='card.png',
    card_name='h4x4d',
    card_class='priest',
    rarity='leg',
    card_text='[b]Battlecry:[/b] create this test!',
    card_image=r'C:\Documents\favorite_image.png',
    mana_cost=3,
    attack=4,
    health=3,
    hd=True,
    addon='karazhan'
)


card_maker = CardCreator()

card_maker.create_card(
    card_type='spell',
    save_name='card.png',
    card_name='h4x4d`s spell',
    card_class='priest',
    rarity='leg',
    card_text='Creates class and one more test, but with spell!',
    card_image=r'C:\Documents\favorite_image_2.png',
    mana_cost=3,
    hd=True,
    addon='karazhan'
)
