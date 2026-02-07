#!/usr/bin/env python3
import click
import os
import json
import curses
import sys

# State management

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

# CLI with Click and non-TUI flags
@click.group()
def cli():
    "AI ShellNest CLI"
    pass

@cli.command()
def start():
    "Start or connect to the local LLM instance (stub)"
    click.echo("[MVP] Starting local Ollama instance... (stub)")

@cli.command()
@click.argument('name')
def create(name):
    "Create a new AI agent session"
    agents = load_agents()
    if name in agents:
        click.echo(f"Agent '{name}' already exists.")
    else:
        agents.append(name)
        save_agents(agents)
        click.echo(f"Created agent '{name}'.")

@cli.command('list')
def list_agents():
    "List all AI agents"
    agents = load_agents()
    if not agents:
        click.echo("No agents found.")
    else:
        for a in agents:
            click.echo(a)

@cli.command()
@click.argument('agent')
@click.argument('task', nargs=-1)
def run(agent, task):
    "Run a task with an agent"
    agents = load_agents()
    if agent not in agents:
        click.echo(f"Agent '{agent}' does not exist.")
    else:
        click.echo(f"[MVP] Agent '{agent}' running task: {' '.join(task)}")

# TUI entry if no args passed
def launch_tui():
    def inner(stdscr):
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
        idx = 0
        MENU = ['List Agents', 'Create Agent', 'Run Agent Task', 'Quit']
        while True:
            stdscr.clear()
            h, w = stdscr.getmaxyx()
            stdscr.addstr(1, w//2 - len('AI ShellNest TUI')//2, 'AI ShellNest TUI', curses.A_BOLD)
            for i, item in enumerate(MENU):
                x = w//2 - len(item)//2
                y = 3 + i
                if i == idx:
                    stdscr.attron(curses.color_pair(1)); stdscr.addstr(y, x, item); stdscr.attroff(curses.color_pair(1))
                else:
                    stdscr.addstr(y, x, item)
            stdscr.refresh()
            key = stdscr.getch()
            if key == curses.KEY_UP and idx>0: idx-=1
            elif key == curses.KEY_DOWN and idx<len(MENU)-1: idx+=1
            elif key in [curses.KEY_ENTER, ord('\n')]:
                if MENU[idx]=='Quit': break
                elif MENU[idx]=='List Agents':
                    agents=load_agents();
                    stdscr.clear(); stdscr.addstr(1,2, 'Agents: '+', '.join(agents) if agents else 'No agents found.' ); stdscr.getch()
                elif MENU[idx]=='Create Agent':
                    curses.echo(); stdscr.clear(); stdscr.addstr(1,2,'Enter agent name:'); name=stdscr.getstr(2,2).decode(); curses.noecho()
                    agents=load_agents()
                    if name in agents: stdscr.addstr(4,2,f"Agent '{name}' exists"); stdscr.getch()
                    else: agents.append(name); save_agents(agents); stdscr.addstr(4,2,f"Created '{name}'"); stdscr.getch()
                elif MENU[idx]=='Run Agent Task':
                    curses.echo(); stdscr.clear(); stdscr.addstr(1,2,'Agent name:'); a=stdscr.getstr(2,2).decode();
                    stdscr.addstr(3,2,'Task:'); t=stdscr.getstr(4,2).decode(); curses.noecho()
                    stdscr.clear(); stdscr.addstr(1,2,f"Running '{t}' on '{a}' (stub)"); stdscr.getch()
    curses.wrapper(inner)

if __name__=='__main__':
    if len(sys.argv)>1:
        cli()
    else:
        launch_tui()