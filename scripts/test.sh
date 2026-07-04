#!/bin/bash
if [ -f "venv/Scripts/activate" ]; then source venv/Scripts/activate; else source venv/bin/activate; fi

export PYTHONPATH=$(pwd)
pytest tests/