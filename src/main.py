import questionary as q


#_______entry_______

env_config = []

from pathlib import Path

rootPath = Path(__file__).resolve().parent
shared = Path(__file__).resolve().parent / "Shared"

DOCKER = q.confirm("Init Docker?").ask()
# Handle docker 


API_APP = q.confirm("Init API App?").ask()
CLI_APP = q.confirm("Init CLI app?").ask()
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
        except:
            print("please delete src/Shared/database_one.py and rename the other one to database.py")

else:
    try:
        (shared / "database_both.py").unlink()
        (shared / "database_one.py").rename(shared / "database.py")
    except:
        print("please delete src/Shared/database_both.py and rename the other one to database.py")

with open(".env", "w") as f:
    f.writelines(env_config)

#______RUNNING______
import subprocess

try:
    subprocess.run([f"{rootPath}/.venv/bin/pip","install","-e","."])
    try:
        subprocess.run([f"{rootPath}/.venv/scripts/pip","install","-e","."])
    except:
        pass
except:
    pass

try:
    subprocess.run([f"{rootPath}/.venv/bin/alembic","upgrade","head"])
    try:
        subprocess.run([f"{rootPath}/.venv/scripts/alembic","upgrade","head"])
    except:
        pass
except:
    pass

print("Haber is ready to use! \n"\
    "For any use you'll need virtual Environment \n"\
    "run virtual Environment linux(src/.venv/bin/activate) Windows(src/.venv/scripts/activate) \n"\
    "Or run uv sync in 'src' dir and then run commands with 'uv run' \n"
)


if API_APP:
    print(
        "To start fastAPI App run haber-run-fastapi and Done!"
    )

if CLI_APP:
    print(
        "To see list of CLI App commands run haber-cli and Done!"
    )