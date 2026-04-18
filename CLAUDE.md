# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run the app (debug mode, port 5001)
python app.py

# Run tests
pytest

# Run a single test file
pytest tests/test_auth.py

# Install dependencies
pip install -r requirements.txt
```

## Stack

**Spendly** is a Flask 3 + SQLite web app with server-side Jinja2 templates and vanilla CSS/JS. No Node.js, no bundler, no TypeScript.

- `app.py` — all routes and Flask app initialization
- `database/db.py` — SQLite layer (`get_db`, `init_db`, `seed_db` to be implemented)
- `templates/` — Jinja2 templates extending `base.html`
- `static/css/style.css` — custom design system (CSS variables, no Tailwind/Bootstrap)
- `static/js/main.js` — vanilla JS placeholder

## Architecture

All routes live in `app.py`. The database layer is intentionally stubbed out in `database/db.py` — `get_db()` should return a SQLite connection with `row_factory = sqlite3.Row` and foreign keys enabled; `init_db()` creates tables; `seed_db()` loads sample data.

Routes follow a simple pattern: fetch data via `db.py` helpers, pass to `render_template`. Auth state is managed via Flask sessions.

**Planned routes not yet implemented:** `GET /logout`, `GET /profile`, `POST /expenses/add`, `POST /expenses/<id>/edit`, `POST /expenses/<id>/delete`.

## Design System

The CSS in `static/css/style.css` uses CSS custom properties defined in `:root`. Fonts are DM Serif Display (headings) and DM Sans (body), loaded from Google Fonts. Currency displays use the ₹ (Indian Rupee) symbol.
