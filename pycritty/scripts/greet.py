import click

@click.command()
@click.option('--name', '-n', default='World', help='Who to greet.')
def cli(name):
    """Example script."""
    click.echo(f'Hello, {name}!')