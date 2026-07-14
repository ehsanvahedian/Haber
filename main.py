import questionary as q


#_______entry_______

env_config = []

from pathlib import Path
import shutil
rootPath = Path(__file__).resolve().parent
shared = Path(__file__).resolve().parent / "src" / "Shared" 

DOCKER = q.confirm("Init Docker?").ask()
# Handle docker 

CLI_APP = True
API_APP = q.confirm("Init API App?").ask()
if API_APP:
    CLI_APP = q.confirm("Init CLI app?").ask()
    if not CLI_APP:
        cli_dir = (rootPath / "src/presentation/CLI")
        if cli_dir.exists():
            shutil.rmtree(cli_dir)
elif not API_APP:
    api_dir = (rootPath / "src/presentation/API")
    if api_dir.exists():
        shutil.rmtree(api_dir)



DB = q.confirm("Do you have PostgreSQL database(url:port, userName, password, DBName)? ").ask()


if DB:
    API_APP_DB_URL = q.text("Database URL: ").ask()
    API_APP_DB_PORT = q.text("Database port: ").ask()
    API_APP_DB_USERNAME = q.text("Database User Name: ").ask()
    API_APP_DB_PASSWORD = q.text("Database Password: ").ask()
    API_APP_DB_DBNAME = q.text("Database DB Name: ").ask()
    env_config.append(
            f"DATABASE_URL=postgresql://{API_APP_DB_USERNAME}:{API_APP_DB_PASSWORD}@{API_APP_DB_URL}:{API_APP_DB_PORT}/{API_APP_DB_DBNAME}"
        )
else:
    env_config.append(
            "DATABASE_URL=sqlite:///haber.db"
        )
if CLI_APP and DB:
    CLI_APP_DB = q.select("Which DB for CLI App? ", choices=["API_app_DB", "SQLITE"])
    if CLI_APP_DB:
        env_config.append(
            "SECOND_DATABASE_URL=sqlite:///haber.db"
        )
        try:
            (shared / "database_one.py").unlink()
            (shared / "database_both.py").rename(shared / "database.py")
            print("Database file initialized")
        except:
            print("please delete src/Shared/database_one.py and rename the other one to database.py")

else:
    try:
        (shared / "database_both.py").unlink()
        (shared / "database_one.py").rename(shared / "database.py")
        print("Database file initialized")
    except:
        print("please delete src/Shared/database_both.py and rename the other one to database.py")

with open(".env", "w") as f:
    f.writelines(env_config)

#______RUNNING______
import subprocess

try:
    subprocess.run([f"{rootPath}/src/.venv/bin/pip","install","-e","."])
    try:
        subprocess.run([f"{rootPath}/src/.venv/scripts/pip","install","-e","."])
    except:
        pass
except:
    pass

try:
    subprocess.run([f"{rootPath}/src/.venv/bin/alembic","upgrade","head"])
    try:
        subprocess.run([f"{rootPath}/src/.venv/scripts/alembic","upgrade","head"])
    except:
        pass
except:
    pass

#_____Exported Table_____
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

table = Table(title="📦 Haber Setup Guide", style="bold cyan")
table.add_column("Step", style="bold green", no_wrap=True)
table.add_column("Description", style="bold white")
table.add_column("Command", style="bold yellow")

table.add_row(
    "1️⃣", 
    "Enter to src directory", 
    "cd src"
)
table.add_row(
    "2️⃣", 
    "Activate (Linux/Mac)", 
    "source .venv/bin/activate"
)
table.add_row(
    "2️⃣", 
    "Activate (Windows)", 
    ".venv\\Scripts\\activate"
)
table.add_row(
    "3️⃣", 
    "You have UV Installed?", 
    "uv sync & uv run 'below-commands'"
)
table.add_row(
    "4️⃣", 
    "Use below Commands", 
    "--------"
)

console.print(" ")
console.print("_____________")
console.print(table)


if API_APP:
    api_panel = Panel(
        "[bold green]🚀 To start FastAPI App:[/]\n"
        "[bold yellow]haber-run-fastapi[/]",
        title="✨ API App",
        border_style="cyan"
    )
    console.print(api_panel)


if CLI_APP:
    cli_panel = Panel(
        "[bold green]📋 To see CLI commands:[/]\n"
        "[bold yellow]haber-cli[/]",
        title="⚡ CLI App",
        border_style="magenta"
    )
    console.print(cli_panel)
