# AI ShellNest MVP

AI ShellNest is a minimal CLI tool for managing local AI agent sessions using Ollama (stubbed).

## Features

- `start`: Initialize or connect to the LLM instance (stub)
- `create <name>`: Create a named agent
- `list`: List all agents
- `run <agent> <task>`: Run a simple task with an agent

## Usage

```bash
# Install
chmod +x main.py
mv main.py aishellnest

# Start
./aishellnest start

# Create agents
./aishellnest create research
./aishellnest create draft

# List agents
./aishellnest list

# Run a task
./aishellnest run research "summarize recent AI papers"
```

## Example Output

```
$ ./aishellnest start
[MVP] Starting local Ollama instance... (stub)

$ ./aishellnest create research
Created agent 'research'.

$ ./aishellnest list
Agents:
 - research

$ ./aishellnest run research "summarize AI trends"
[MVP] Agent 'research' running task: summarize AI trends
```

## Screenshot

!(Screenshot placeholder showing CLI usage)

---
*This is an MVP stub and does not launch a real model yet.*