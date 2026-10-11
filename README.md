# Freelance Solution Base

A curated, tested index and decision guide for freelance automation, website support, and small backend tasks.

## Why this exists

Market research showed that generic proposals for Telegram bots or parsers enter crowded fields: 10 of 78 Kwork IT projects targeted Telegram bots with a median of 58 competing proposals, while full-product web/app requests showed negative economics.

This repository anchors work in:

- tested forks where ownership and direct modification help;
- tested proprietary starters for file processing and webhook integration;
- direct upstream dependencies and services rather than unmaintained forks;
- clear boundaries: no full-product builds from scratch, no desktop takeovers, and no 1C ERP.

## Inventory

| ID | Role | Repository / Target | License | Tests / Status | Typical adaptation |
|---|---|---|---|---|---|
| `form-to-telegram` | Fork | [Snowfedya/form-to-telegram](https://github.com/Snowfedya/form-to-telegram) | MIT | 41 passed | 0.5–2 h |
| `booking-bot` | Fork | [Snowfedya/booking_bot](https://github.com/Snowfedya/booking_bot) | MIT | 43 passed, 8 skipped | 1–3 h |
| `file-processor-starter` | Starter | [Snowfedya/freelance-file-processor-starter](https://github.com/Snowfedya/freelance-file-processor-starter) | MIT | 4 passed | 1–4 h |
| `integration-starter` | Starter | [Snowfedya/freelance-integration-starter](https://github.com/Snowfedya/freelance-integration-starter) | MIT | 5 passed | 1–4 h |
| `tablib` | Dependency | [jazzband/tablib](https://github.com/jazzband/tablib) | MIT | PyPI package | 0.5–1 h |
| `crawlee-python` | Dependency | [apify/crawlee-python](https://github.com/apify/crawlee-python) | Apache-2.0 | PyPI package | 2–6 h |
| `gotenberg` | Service | [gotenberg/gotenberg](https://github.com/gotenberg/gotenberg) | MIT | Docker service | 1–2 h |
| `pocketbase` | Service | [pocketbase/pocketbase](https://github.com/pocketbase/pocketbase) | MIT | Docker / binary | 1–3 h |
| `doctor-command` | Tool | [wp-cli/doctor-command](https://github.com/wp-cli/doctor-command) | MIT | WP-CLI package | 0.5–2 h |

## Qualification gate

Apply this gate before responding to a freelance task:

1. Competence: can the maintainer verify the output directly?
2. Automation: can an agent do 80%+ without a remote desktop session?
3. Boundaries: does the client already own the spec, design, or existing site?
4. Unit economics: does the budget cover discovery, development, verification, and communication?
5. Reusability: does the task map to an existing item in `catalog.json`?

## Test catalog

```bash
python -m venv .venv
.venv/bin/pip install -e '.[dev]'
.venv/bin/python -m pytest
```

## License

MIT
