from pathlib import Path
import yaml

CONFIG_DIR = Path.home() / ".config" / "bbcli"
CREDENTIALS_FILE = CONFIG_DIR / "credentials.yaml"


def load_credentials() -> dict:
    if not CREDENTIALS_FILE.exists():
        raise FileNotFoundError(
            "No credentials found. Run [bold]bb auth login[/bold] first."
        )
    with CREDENTIALS_FILE.open() as f:
        return yaml.safe_load(f)


def save_credentials(email: str, api_token: str) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CREDENTIALS_FILE.write_text(yaml.dump({"email": email, "api_token": api_token}))
    CREDENTIALS_FILE.chmod(0o600)
