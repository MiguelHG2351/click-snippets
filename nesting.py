import click

""""""
# nesting command
# @click.group()
# def cli():
#   pass

# @click.command()
# def initdb():
#   click.echo('Initialized the database')
  
# @click.command()
# def dropdb():
#   click.echo('Dropped the database')

# cli.add_command(initdb)
# cli.add_command(dropdb)

# if __name__ == '__main__':
#   cli()

""""""
# Add later command
# @click.command()
# def greet():
#   click.echo('Hello world!')
  
# @click.group()
# def group():
#   pass

# group.add_command(greet)

""""""
# Auto nesting command
@click.group()
def cli():
  pass

@cli.command()
def initdb():
  click.echo('Initialized the database')
  
@cli.command()
def dropdb():
  click.echo('Dropped the database')


if __name__ == '__main__':
  cli()

