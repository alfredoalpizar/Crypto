import click
import requests
from terminaltables import SingleTable


@click.command()
@click.argument('coin', default='all')
def cli(coin):
    c = coin.upper().replace(' ', '-')
    if c == 'ALL':
        r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
        data = r.json()
        table_data = []
        table_data.append(['#', 'Name', 'Price $USD', '24hr Change'])
        for item in data:
            color = 'green' if float(item['percent_change_24h']) > 0 else 'red' 
            table_data.append([item['rank'], item['name'], click.style(item['price_usd'], fg=color), item['percent_change_24h']])
        table = SingleTable(table_data, 'Crypto')
        click.echo(table.table)
    elif requests.get('https://api.coinmarketcap.com/v1/ticker/'+c).status_code == 200:
        data = requests.get('https://api.coinmarketcap.com/v1/ticker/'+c).json()
        table_data = []
        table_data.append(['#', 'Name', 'Price $USD', '24hr Change'])
        table_data.append([data[0]['rank'], data[0]['name'], data[0]['price_usd'], data[0]['percent_change_24h']])
        
        table = SingleTable(table_data, 'Crypto')
        click.echo(table.table)
    else:
        r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
        data = r.json()
        found = False
        for item in data:
            if item['symbol'] == coin.upper():
                click.echo(coin.upper())
                click.echo(item['price_usd'])
                found = True
        if not found:
            click.echo('Coin could not be found')
