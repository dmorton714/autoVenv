import subprocess
import sys
import os


def create_venv():
    try:
        # Create virtual environment with the name 'venv'
        subprocess.run([sys.executable, '-m', 'venv', 'venv'], check=True)
        print("Virtual environment 'venv' created successfully.")

        # Set the VIRTUAL_ENV environment variable to activate the virtual environment
        os.environ['VIRTUAL_ENV'] = os.path.abspath('venv')
        print("Virtual environment 'venv' activated.")
        print("Enter deactivate to close 'venv'")

    except subprocess.CalledProcessError:
        print("Failed to create or activate virtual environment.")
        sys.exit(1)


if __name__ == "__main__":
    create_venv()
