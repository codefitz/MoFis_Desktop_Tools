import subprocess
import pytest


scripts = [
    'pasta.py',
    'mouse_jiggle.py',
    'ss_window.py',
    'ss_window.pyw'
]


@pytest.mark.parametrize('script', scripts)
def test_compile(script):
    subprocess.run(['python', '-m', 'py_compile', script], check=True)
