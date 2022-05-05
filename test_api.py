import requests


# currently below method fetches only 10 beers
# we can modify it to fetch all of the beers by calling api multiple times and accumulating resut in a list
def GetBeersWithYeastAndHops():
    parameters = {
        'yeast': 'Wyeast 3522 - Belgian Ardennes',
        'hops': 'Tomahawk'
    }
    response = requests.get('https://api.punkapi.com/v2/beers?page=1&per_page=10', params=parameters)
    print(response.json());


GetBeersWithYeastAndHops();


# verifys hops quantity equals to 12.5 grams for a selected beer (accepts beer id)
# prints true if the beer has 12.5 grams of magnum hops in the selected beer
def VerifyHopsQuantity(id):
    beer = requests.get('https://api.punkapi.com/v2/beers', params={'id': id}).json();

    hops = beer[0]['ingredients']['hops'];
    magnumhops = list(filter(lambda x: x['name'] == 'Magnum' and x['amount']['value'] == 12.5, hops));
    print(len(magnumhops) == 1);


VerifyHopsQuantity(1)


# verified IBU content is type numeric or not for selected beer (accepts beer Id as a param)
# prints true if it is numeric else false
def VerifyIBUContent(id):
    beer = requests.get('https://api.punkapi.com/v2/beers', params={'id': id}).json();

    ibu = beer[0]['ibu'];
    print(ibu, isinstance(ibu, (int, float)));


VerifyIBUContent(100);


# verifies description is not empty
# prints false if empty else true
def VerifyDescriptionNotEmoty(id):
    beer = requests.get('https://api.punkapi.com/v2/beers', params={'id': id}).json();

    description = beer[0]['description'];
    print(len(description) != 0);


VerifyDescriptionNotEmoty(100);