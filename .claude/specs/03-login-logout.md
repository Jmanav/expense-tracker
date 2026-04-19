# Spec: Login and Logout

## Overview
This step implements user authentication. It wires up the `POST /login` route to accept credentials, verify the password hash, store the user's id and name in the Flask session, and redirect to a dashboard placeholder. The `GET /logout` route clears the session and redirects to the landing page. Together these two routes complete the auth loop started by registration in Step 02.

## Depends on
- Step 01: Database Setup — `users` table and `get_db()` must exist.
- Step 02: Registration — at least one user must be insertable to test login.

## Routes
- `GET /login` — render the login form — public (already exists, needs POST added)
- `POST /login` — validate credentials, set session, redirect to `/dashboard` — public
- `GET /logout` — clear session, redirect to `/` — logged-in (currently a stub)

## Database changes
No database changes. Reads from the existing `users` table using the `email` column.

## Templates
- **Modify:** `templates/login.html` — add a `<form method="POST" action="/login">` with `email` and `password` fields; display flash messages for errors.
- **Create:** `templates/dashboard.html` — minimal logged-in landing page showing the user's name and a logout link; extends `base.html`.

## Files to change
- `app.py` — replace the `GET /login` stub with `GET/POST /login`; implement `GET /logout`; import `check_password_hash` from `werkzeug.security`

## Files to create
- `templates/dashboard.html` — minimal dashboard extending `base.html`

## New dependencies
No new dependencies.

## Rules for implementation
- No SQLAlchemy or ORMs
- Parameterised queries only — never use string formatting in SQL
- Passwords verified with `werkzeug.security.check_password_hash`
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`
- Fetch user row by email first; if no row found, show a generic "Invalid email or password" flash error (do not reveal which field was wrong)
- If row found but password check fails, show the same generic error
- On success, store `session["user_id"]` and `session["user_name"]`; redirect to `GET /dashboard`
- `GET /logout` must call `session.clear()` then redirect to `url_for("landing")`
- `GET /dashboard` must redirect to `/login` if `session.get("user_id")` is absent

## Definition of done
- [ ] `GET /login` renders a form with email and password fields
- [ ] Submitting valid credentials sets `session["user_id"]` and `session["user_name"]` and redirects to `/dashboard`
- [ ] `/dashboard` displays the logged-in user's name
- [ ] Submitting an unrecognised email shows "Invalid email or password" and does not set a session
- [ ] Submitting a correct email with a wrong password shows "Invalid email or password" and does not set a session
- [ ] `GET /logout` clears the session and redirects to `/`
- [ ] Visiting `/dashboard` while logged out redirects to `/login`
- [ ] App starts without errors after changes
