# Logomachy

A Django application for indexing, analysing, and comparing text, particularly EULA, ToS, privacy statements, and other documents.

## Technical Overview

There are a number of Django applications included in the default Logomachy Django project.

See `DEVELOPEMENT.md` for information about setting up a development environment.

The project is `logomach_project`. The settings (`logomach_project.settings.`) are split into a number of use cases.
All except `base` can be used for `DJANGO_SETTINGS_MODULE`.
- `base`: The common/shared settings used by all other settings files.
- `dev_console`
- `dev_web`
- `prod_console`
- `prod_web`
- `stag_conosle`
- `stag_web`

The applications are:
- `logomachy.logomachy_core`
- `logomachy.logomachy_auth`
- `logomachy.logomachy_text_stats`



## Setup

Logomachy is best deployed in a Python virtual environment. It supports Python versions >= 3.5.
