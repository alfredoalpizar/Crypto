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
            table_data.append([item['rank'], item['name'], click.style(item['price_usd'], fg=color), click.style(item['percent_change_24h'], fg=color)])
        table = SingleTable(table_data, 'Crypto')
        click.echo(table.table)
    elif requests.get('https://api.coinmarketcap.com/v1/ticker/'+c).status_code == 200:
        data = requests.get('https://api.coinmarketcap.com/v1/ticker/'+c).json()
        table_data = []
        table_data.append(['#', 'Name', 'Price $USD', '24hr Change'])
        color = 'green' if float(data[0]['percent_change_24h']) > 0 else 'red'
        table_data.append([data[0]['rank'], data[0]['name'], click.style(data[0]['price_usd'], fg=color), click.style(data[0]['percent_change_24h'], fg=color)])
        
        table = SingleTable(table_data, 'Crypto')
        click.echo(table.table)
    else:
        r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
        data = r.json()
        found = False
        table_data = []
        table_data.append(['#', 'Name', 'Price $USD', '24hr Change'])
        for item in data:
            if item['symbol'] == coin.upper():
                color = 'green' if float(item['percent_change_24h']) > 0 else 'red'
                table_data.append([item['rank'], item['name'], click.style(item['price_usd'], fg=color), click.style(item['percent_change_24h'], fg=color)])
                found = True
                click.echo(table.table)
        if not found:
            click.echo('Coin could not be found')
