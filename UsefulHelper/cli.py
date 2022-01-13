#!/usr/bin/python3.9
import click
# from UsefulHelper import Start

key_list = ['start']


@click.command()
@click.option(
    "--things", prompt="[UsefulHelper]>>",
    help="NONE."
)
def main(things):
    if things == 'start':
        print(0)
    else:
        things = None
        main(things)


if __name__ != '__main__':
    main()
