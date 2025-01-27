# Python GUI exploration

This project aims to explore modern Python application development, with the following aims:
- tidy project structure with tools for dependency management
- modern UI framework with a nice developer experience
- UI tables connected to database
- packaging and distribution

## Project management

[This article](https://www.stuartellis.name/articles/python-modern-practices) describes some good practices. [uv](https://docs.astral.sh/uv/) seems to do a good job of both managing the project's virtual environment and the dependencies, and the project config is defined in [pyproject.toml](pyproject.toml).

## UI framework

PySide and Pyedifice.

### UI Tables and database
QTableView and QSql.

## Packaging and distribution
Nuitka
