import click
import requests


@click.command()
@click.argument('coin', default='bitcoin')
def cli(coin):
    c = coin.upper().replace(' ', '-')
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/'+c)
    if r.status_code == 200:
        data = r.json()
        click.echo(data[0]['symbol'])
        click.echo(data[0]['price_usd'])
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
