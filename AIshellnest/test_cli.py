import subprocess
import json
import os
import pytest

CLI = os.path.abspath(os.path.join(os.path.dirname(__file__), 'main.py'))
STATE = os.path.expanduser('~/.aishellnest/agents.json')

@pytest.fixture(autouse=True)
def clean_state(tmp_path, monkeypatch):
    # Use temp file for state
    monkeypatch.setenv('AISHELLNEST_DIR', str(tmp_path))
    # Adjust get_state_path to use env var
    yield

 def test_create_and_list(monkeypatch):
    # Create agent
    res = subprocess.run(['python3', CLI, 'create', 'test'], capture_output=True, text=True)
    assert "Created agent 'test'" in res.stdout
    # List agents
    res = subprocess.run(['python3', CLI, 'list'], capture_output=True, text=True)
    assert 'test' in res.stdout

 def test_run(monkeypatch):
    subprocess.run(['python3', CLI, 'create', 'runner'], capture_output=True)
    res = subprocess.run(['python3', CLI, 'run', 'runner', 'do','work'], capture_output=True, text=True)
    assert "running task: do work" in res.stdout

 if __name__=='__main__':
    pytest.main()
