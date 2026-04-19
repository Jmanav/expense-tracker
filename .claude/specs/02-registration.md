# Spec: Registration

## Overview
This step implements user registration. It wires up the `POST /register` route to accept a sign-up form, validate input, hash the password, insert a new row into the `users` table, and redirect the user to the login page on success. The `GET /register` route already renders the template; this step makes the form functional.

## Depends on
- Step 01: Database Setup — `users` table and `get_db()` must exist and work correctly.

## Routes
- `GET /register` — render the registration form — public (already exists, no change needed)
- `POST /register` — process sign-up form submission — public

## Database changes
No new tables or columns. Uses the existing `users` table:
- `name` TEXT NOT NULL
- `email` TEXT NOT NULL UNIQUE
- `password_hash` TEXT NOT NULL
- `created_at` TEXT NOT NULL DEFAULT (date('now'))

## Templates
- **Modify:** `templates/register.html` — add a `<form method="POST" action="/register">` with fields for `name`, `email`, `password`, and `confirm_password`; display flash messages for errors and success.

## Files to change
- `app.py` — add `POST /register` route; import `get_db` from `database.db`; import `generate_password_hash` from `werkzeug.security`; import `flash`, `redirect`, `url_for`, `request`, `session` from `flask`
- `templates/register.html` — add the HTML form and flash message display

## Files to create
No new files.

## New dependencies
No new dependencies.

## Rules for implementation
- No SQLAlchemy or ORMs
- Parameterised queries only — never use string formatting in SQL
- Passwords hashed with `werkzeug.security.generate_password_hash`
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`
- Validate that `name`, `email`, and `password` are non-empty before inserting
- Validate that `password == confirm_password`; show a flash error if they don't match
- Validate that `email` is not already registered; catch the `UNIQUE` constraint error and show a user-friendly flash message
- On success, flash a success message and redirect to `GET /login`
- On failure, re-render `register.html` with the flash error (do not clear the form fields via session — a simple re-render is fine)
- Enable `app.secret_key` in `app.py` if not already set (required for `flash`)

## Definition of done
- [ ] `GET /register` renders the registration form with name, email, password, and confirm password fields
- [ ] Submitting the form with valid data inserts a new user into the database with a hashed password
- [ ] The inserted `password_hash` is verifiable with `werkzeug.security.check_password_hash`
- [ ] Submitting with mismatched passwords shows a flash error and does not insert a row
- [ ] Submitting with an already-registered email shows a flash error and does not insert a duplicate row
- [ ] Submitting with any empty field shows a flash error and does not insert a row
- [ ] Successful registration redirects to `/login`
- [ ] App starts without errors after changes
