# 4-4) Suomi-englanti dictionary
#
# Create a simple finnish-english dictionary

get_dictionary = {}

def main():
    dictionary = get_dictionary()

    while True:
        try:
            word = input('Anna sana>')

            if not word:
                break

            print(dictionary[word])
        except KeyError:
            print('???')
        except EOFError:
            break

def get_dictionary():
    # Source: http://randomfinnishlesson.blogspot.fi/2014/02/100-very-common-finnish-words.html
    return {
    	'aika': 'time, quite',
    	'aina': 'always',
    	'antaa': 'to give',
    	'asia': 'thing, matter',
    	'ehkä': 'maybe',
    	'eli': 'so, in other words',
    	'ennen': 'before',
    	'ensi': 'next ',
    	'ensin': 'at first',
    	'eri': 'different',
    	'että': 'that',
    	'heti': 'immediately',
    	'huono': 'bad',
    	'hyvä': 'good',
    	'itse': 'self',
    	'ja': 'and',
    	'jo': 'already',
    	'joka': 'which, every',
    	'joku': 'someone',
    	'jopa': 'even',
    	'jos': 'if',
    	'joskus': 'sometimes',
    	'jossa': 'in which',
    	'joten': 'so, therefore',
    	'jotka': 'which (plural)',
    	'jälkeen': 'after',
    	'kaikki': 'all, everybody',
    	'kaupunki': 'a town, a city',
    	'kanssa': 'with',
    	'kello': 'a clock',
    	'kertoa': 'to tell',
    	'koko': 'whole, all',
    	'koska': 'because, when',
    	'koti': 'home',
    	'kuin': 'than',
    	'kuinka': 'how',
    	'kuitenkin': 'however',
    	'kun': 'when',
    	'kuva': 'picture',
    	'kyllä': 'yes',
    	'käydä': 'to go, to visit',
    	'maa': 'a country, a land',
    	'mennä': 'to go',
    	'mies': 'a man, a husband',
    	'mikä': 'what',
    	'miksi': 'why',
    	'miten': 'how',
    	'monta': 'many',
    	'mukaan': 'with, according to',
    	'mutta': 'but',
    	'muu': 'other, else',
    	'myös': 'also, too',
    	'nainen': 'a woman',
    	'niin': 'so, like that',
    	'noin': 'like that, approximately',
    	'nyt': 'now',
    	'nähdä': 'to see',
    	'näin': 'like this',
    	'nämä': 'these',
    	'oikea': 'real, right, correct',
    	'olla': 'to be',
    	'paitsi': 'except',
    	'paljon': 'a lot, much',
    	'pitää': 'to like, to have to, to keep',
    	'pois': 'away',
    	'puoli': 'half, side',
    	'päivä': 'day',
    	'saada': 'to get, to receive',
    	'sama': 'same',
    	'sanoa': 'to say',
    	'se': 'it',
    	'siellä': 'over there',
    	'siinä': 'in there',
    	'silloin': 'then',
    	'sillä': 'because',
    	'sitten': 'then, when, ago, in that case',
    	'taas': 'again',
    	'tai': 'or',
    	'takaisin': 'back',
    	'tehdä': 'to do, to make',
    	'tila': 'space',
    	'tuo': 'that (something you can point at)',
    	'tulla': 'to come',
    	'tämä': 'this',
    	'tässä': 'here',
    	'vaan': 'but',
    	'vai': 'or',
    	'vaikka': 'although, for example',
    	'vain': 'only',
    	'vielä': 'yet, still, furthermore',
    	'viime': 'last',
    	'voida': 'to be able to',
    	'vuosi': 'a year',
    	'vähän': 'a little',
    	'väärä': 'wrong, false',
    	'yli': 'over, past',
    	'älä': 'don\'t',

        'koira': 'dog',
        'kieli': 'language',
        'maa': 'country'
    }

if __name__ == "__main__":
    main()
