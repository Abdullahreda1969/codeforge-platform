"""Main CLI interface for CodeForge."""

import click
from typing import Optional


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """CodeForge - Professional SDLC Project Generator & Manager."""
    pass


@cli.command()
@click.option('--template', '-t', default='web-fastapi', 
              help='Template to use for project generation')
@click.option('--output-dir', '-o', default='.', 
              help='Output directory for the project')
def init(project_name: str, template: str, output_dir: str):
    """Initialize a new project from a template."""
    click.echo(f"Initializing project '{project_name}' with template '{template}'...")
    # TODO: Implement project initialization
    click.echo(f"Project created in {output_dir}/{project_name}")


@cli.command()
def list_templates():
    """List all available project templates."""
    click.echo("Available templates:")
    click.echo("  • web-fastapi    - FastAPI + React web application")
    click.echo("  • api-restful    - RESTful API service")
    click.echo("  • business-app   - Business application template")
    # TODO: Load templates dynamically


if __name__ == '__main__':
    cli()
