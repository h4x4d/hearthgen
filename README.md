# HearthGen - create your own hearthstone cards inside python

# About

Hearthgen is a python library using selenium webdriver to access 
https://hearthcards.net/ and make hearthstone cards inside python.

# Installing
You can install hearthgen from Github:
```
pip install https://github.com/h4x4d/hearthgen/blob/main/archive/hearthgen-0.0.2.tar.gz
```
Or from PyPi:
```
pip install hearthgen
```

# Using hearthgen

You can create card with 2 different methods:
- Using function create_card()
- Using class CardCreator()

What is the difference between them?

CardCreator initializes webdriver on the and can be used many times, but 
create_card() initializes webdriver on start of function and stop it at 
the end. So if you make one card, it's pretty good to use function, but 
if you make more cards in one run it's more suitable to use class.

So, what about using?

And don't forget about chromedriver in script path to run it!

```python
from hearthgen import create_card

create_card(
    card_type='minion',
    save_name='card.png',
    card_name='h4x4d',
    card_class='priest',
    rarity='leg',
    card_text='[b]Battlecry:[/b] create this test!',
    card_image=r'C:\Documents\favorite_image.png', # You need to pass full path to image
    mana_cost=3,
    attack=4,
    health=3,
    hd=True,
    addon='karazhan'
)
```
Not all of them a necessary and if you do spells, for example with class, you don't need to pass atack and health:
```python
from hearthgen import CardCreator

card_maker = CardCreator()

card_maker.create_card(
    card_type='spell',
    save_name='card.png',
    card_name='h4x4d`s spell',
    card_class='priest',
    rarity='leg',
    card_text='Creates class and one more test, but with spell!',
    card_image=r'C:\Documents\favorite_image_2.png', # You need to pass full path to image
    mana_cost=3,
    hd=True,
    addon='karazhan'
)
```

Also, if you need som changes in chromedriver, it's possible to pass it to CardCreator():

```python
from hearthgen import CardCreator
from selenium import webdriver

driver = webdriver.Chrome(r'C:\very_special_path\chromedriver.exe')

card_maker = CardCreator(driver=driver)
```

Full documentation is placed here: *soon it will be here...*

