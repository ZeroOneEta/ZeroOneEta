#!/usr/bin/env python3
import click
import os
import json

# Simple MVP: manage agent names in a JSON file
def get_state_path():
    dir = os.path.expanduser('~/.aishellnest')
    os.makedirs(dir, exist_ok=True)
    return os.path.join(dir, 'agents.json')

def load_agents():
    path = get_state_path()
    if os.path.exists(path):
        return json.load(open(path))
    return []

def save_agents(agents):
    path = get_state_path()
    json.dump(agents, open(path, 'w'), indent=2)

@click.group()
def cli():
    """AI ShellNest MVP CLI"""
    pass

@cli.command()
def start():
    """Start or connect to the local LLM instance (MVP stub)"""
    click.echo("[MVP] Starting local Ollama instance... (stub)")

@cli.command()
@click.argument('name')
def create(name):
    """Create a new AI agent session"""
    agents = load_agents()
    if name in agents:
        click.echo(f"Agent '{name}' already exists.")
    else:
        agents.append(name)
        save_agents(agents)
        click.echo(f"Created agent '{name}'.")

@cli.command()
def list():
    """List all AI agents"""
    agents = load_agents()
    if not agents:
        click.echo("No agents found.")
    else:
        click.echo("Agents:")
        for a in agents:
            click.echo(f" - {a}")

@cli.command()
@click.argument('agent')
@click.argument('task', nargs=-1)
def run(agent, task):
    """Run a task with an agent"""
    agents = load_agents()
    if agent not in agents:
        click.echo(f"Agent '{agent}' does not exist.")
        return
    click.echo(f"[MVP] Agent '{agent}' running task: {' '.join(task)}")

if __name__ == '__main__':
    cli()