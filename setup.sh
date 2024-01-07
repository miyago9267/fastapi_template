# Download poetry if command not found
if [ ! -x "$(command -v poetry)" ]; then
    echo "Poetry not found, installing..."
    curl -sSL https://install.python-poetry.org | python3 -
fi

poetry install