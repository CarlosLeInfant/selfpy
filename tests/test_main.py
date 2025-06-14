import sys
from importlib import reload
from pathlib import Path
import runpy

# Ensure the project root is on sys.path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import main


def test_main_prints_hello_world(capsys):
    main.main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"


def test_module_execution_prints_hello_world(capsys):
    runpy.run_module("main", run_name="__main__", alter_sys=True)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"
