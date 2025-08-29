from __future__ import annotations

import click


@click.command()
@click.option("--config", type=click.Path(exists=True, dir_okay=False), default="config/train.yaml")
def main(config: str) -> None:
    click.echo("Hello from preset_train (Phase 4 stub)")


if __name__ == "__main__":
    main()


