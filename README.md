# MDF — Modular Discord Framework

**MDF (Modular Discord Framework)** is a self-hosted, extensible framework for building personal Discord bots with modular functionality and complete local control.

Unlike centralized Discord apps that lock features behind paywalls or harvest user data, MDF is designed for privacy, freedom and small-scale use. Ideal for personal servers, project teams, or tight-knit communities, MDF empowers you to run your own bot your way.

> MDF is named after **Medium Density Fiberboard**, continuing the materials-based naming theme from SLAG. Like its namesake, it's lightweight, customizable and meant to be built upon.

---

## Features

- **Self-hosted**: No reliance on third-party servers. You own the code, the data, and the behavior.
- **Modular**: Drop-in extensions can be enabled, disabled, or swapped at runtime. No restarts required.
- **No Python knowledge required**: Install and configure modules through simple manifests
- **Full Python access if desired**: Developers can write powerful custom modules with full access to the MDF API.
- **Optimized for 10 or fewer servers**: Avoids Discord verification hell, stays lean and under rate limits.
- **Fast iteration**: Live reload and isolated module development means fast testing without rebooting the entire bot.
- **No telemetry, no tracking, no nags**: Just you and your bot.

---

## Example Use Cases

- A small gaming community with custom commands, leveling, and moderation
- A research group automating paper citation and data formatting
- A private art community with queue management, tag filters, and uploads
- Your own personal bot that lives quietly and efficiently in one server

---

## Core Architecture: `app.py`

At the heart of MDF is **`app.py`**, a single Python file that handles:

- Discord connection and event lifecycle
- Module discovery and dynamic loading
- Command dispatch and routing
- Error handling and diagnostics
- Optional auto-reload for hot-swappable development

This single-file design makes MDF:
- **Extremely easy to audit**
- **Portable**, just copy the folder and go
- **Beginner-friendly**, with clear entry points and zero boilerplate

Advanced users can modify `app.py` directly to tweak the core behavior or fork it for their own needs. It's your engine.

---

## Modules

Modules are stored in the `/modules` directory. Each module includes:
- A manifest (`module.yaml`)
- Optional config schema
- Python logic (if needed)

Modules can be reloaded on-the-fly, allowing live updates and debugging.

Want to share your module? Just zip the folder or push to Git!

---

## Installation

```bash
git clone https://github.com/yourname/mdf.git
cd mdf
# optional: create a virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```
