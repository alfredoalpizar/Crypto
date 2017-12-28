import click
import requests
from terminaltables import SingleTable


@click.command()
@click.argument('coin', default='all')
def cli(coin):
    isNUM = coin.isdigit() and float(coin) <= 100
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
    elif coin.isdigit() and (float(coin) > 100 or float(coin) <= 0):
        click.echo("Invalid rank range. 0-100 Please")
    else:
        r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
        data = r.json()
        found = False
        table_data = []
        table_data.append(['#', 'Name', 'Price $USD', '24hr Change'])
        for index, item in enumerate(data):
            if isNUM and index+1 <= 100:
                color = 'green' if float(item['percent_change_24h']) > 0 else 'red'
                table_data.append([item['rank'], item['name'], click.style(item['price_usd'], fg=color), click.style(item['percent_change_24h'], fg=color)])
                if index+1 == float(coin):
                    table = SingleTable(table_data, 'Crypto')
                    click.echo(table.table)
                    found = True
                    break
   
            elif item['symbol'] == coin.upper() and not isNUM:
                color = 'green' if float(item['percent_change_24h']) > 0 else 'red'
                table_data.append([item['rank'], item['name'], click.style(item['price_usd'], fg=color), click.style(item['percent_change_24h'], fg=color)])
                found = True
                table = SingleTable(table_data, 'Crypto')
                click.echo(table.table)
        if not found:
            click.echo('Coin could not be found')
