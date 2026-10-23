from __future__ import annotations

from typer.testing import CliRunner

from signet import __version__
from signet.cli import app

runner = CliRunner()


def test_version_flag() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_new_creates_client_dir(tmp_path, monkeypatch) -> None:
    config_path = tmp_path / "signet.toml"
    config_path.write_text('[paths]\ndata_dir = "./data"\n', encoding="utf-8")
    (tmp_path / "data").mkdir()
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(app, ["new", "club-moon"])
    assert result.exit_code == 0
    assert "club-moon" in result.stdout
