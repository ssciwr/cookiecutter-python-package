import click


@click.command()
def main():
    click.echo("This is {{ cookiecutter|modname }}'s command line interface.")


if __name__ == "__main__":
    main()
