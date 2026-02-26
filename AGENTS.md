# AGENTS.md

## Cursor Cloud specific instructions

### Overview

This is a university coursework repository for "Seguridad de Aplicaciones" (Application Security) at CIBERTEC. It contains **static HTML pages**, SQL demo scripts, Node.js snippets, and Markdown documentation. There is **no build system, no package manager, no test framework, and no CI/CD**.

### Running the applications

All "applications" are static HTML mockups served from the filesystem. To view them in a browser:

```bash
python3 -m http.server 8080
```

Then navigate to:
- **NovaMarket**: `http://localhost:8080/Examen_T1/Pregunta_03_NovaMarket/index.html`
- **SaludPlus Online**: `http://localhost:8080/Examen_T1/Pregunta_02_SaludPlus/index.html`
- **Semana 02 exercises**: `http://localhost:8080/Semana_02/` (various HTML files)

### Node.js scripts

Two standalone Node.js scripts exist in `Semana_03/`:
- `loginSimulado.js` — runs standalone with `node Semana_03/loginSimulado.js` (no dependencies needed)
- `loginLDAP.js` — contains intentional typo (`requeri` instead of `require`); requires `ldapjs` package and an LDAP server; non-functional demo code

### Lint / Test / Build

- **No linter configured** — no ESLint, Prettier, or similar tooling exists.
- **No automated tests** — no test framework or test files exist.
- **No build step** — all files are static and served as-is.

### Notes

- The repository references DVWA (Damn Vulnerable Web App) as an external Docker container for SQL Injection practice: `docker run --rm -it -p 80:80 vulnerables/web-dvwa`. This is optional and not part of the repo itself.
- SQL scripts in `Semana_03/` target SQL Server (T-SQL) and are educational demos only.
