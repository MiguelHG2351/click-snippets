import click

# basic command
# @click.command()
# def hello():
#   click.echo('Hello world!')
  
# if __name__ == '__main__':
#   hello()

@click.command()
def greet():
  click.echo('Hello world!')
  
@click.group()
def group():
  pass

group.add_command(greet)
