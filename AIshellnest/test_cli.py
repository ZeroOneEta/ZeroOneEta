import subprocess
import os
import json
import pytest

# Adjust state path to temp directory for tests
@pytest.fixture(autouse=True)
def temp_state(tmp_path, monkeypatch):
    monkeypatch.setenv('AISHELLNEST_DIR', str(tmp_path))
    yield

CLI = os.path.abspath(os.path.join(os.path.dirname(__file__), 'main.py'))

def run_cmd(args):
    result = subprocess.run(['python3', CLI] + args, capture_output=True, text=True)
    return result

def test_create_and_list():
    res = run_cmd(['create', 'songwriter'])
    assert "Created agent 'songwriter'" in res.stdout
    res = run_cmd(['list'])
    assert 'songwriter' in res.stdout

def test_run_songwriter():
    # ensure agent exists
    run_cmd(['create', 'songwriter'])
    res = run_cmd(['run', 'songwriter', 'write', 'a', 'song'])
    assert "Agent 'songwriter' running task: write a song" in res.stdout

if __name__ == '__main__':
    pytest.main()
