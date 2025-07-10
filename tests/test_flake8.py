import subprocess


def test_flake8():
    subprocess.run(['flake8', '.'], check=True)
