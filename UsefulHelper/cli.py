#!/usr/bin/python3.9
import click
from UsefulHelper import Start


@click.command()
@click.option(
    "--name", prompt="Project name",
    help="The person to greet."
)
@click.option(
    '--path', prompt='Project Path',
    help="None"
)
def start(name, path):
    try:
        Start(name, path)
    except IsADirectoryError:
        pass


if __name__ != '__main__':
    start()
else:
    print('Error')
