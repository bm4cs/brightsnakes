#!/usr/bin/env sh
sudo apt install pipx
pipx install poetry
poetry self add "poetry-dynamic-versioning[plugin]"
