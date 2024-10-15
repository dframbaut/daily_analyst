#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found. Installing Python3..."
    # Install Python3 (macOS)
    brew install python3
fi

# Create a virtual environment if it doesn't exist
if [ ! -d "env_daily_analyst" ]; then
    echo "Creating virtual environment..."
    python3 -m venv env_daily_analyst
fi

# Activate virtual environment
source env_daily_analyst/bin/activate

# Install required dependencies silently
echo "Installing required dependencies..."
pip install -q -r requirements.txt && echo "Requirements installed."

# Add alias to the shell profile (bash or zsh)
if [ -n "$ZSH_VERSION" ]; then
    SHELL_PROFILE="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    SHELL_PROFILE="$HOME/.bashrc"
else
    echo "Unsupported shell. Please add the alias manually to your shell profile."
    exit 1
fi

# Check if alias already exists, if not, add it
if ! grep -q "alias daily_analyst=" "$SHELL_PROFILE"; then
    echo "Adding alias 'daily_analyst' to $SHELL_PROFILE"
    echo "alias daily_analyst='cd $(pwd) && source env_daily_analyst/bin/activate && python main.py'" >> "$SHELL_PROFILE"
    echo "Alias added successfully. Please restart your terminal or run 'source $SHELL_PROFILE'."
else
    echo "Alias 'daily_analyst' already exists in $SHELL_PROFILE."
fi

echo "Setup completed. You can now run the tool with the command: daily_analyst"