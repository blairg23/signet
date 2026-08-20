from __future__ import annotations

from pathlib import Path

import pytest

from signet.clients import client_dir, new_client, slugify
from signet.config import Config


def test_slugify() -> None:
    assert slugify("Club Moon") == "club-moon"
    assert slugify("The Gatsby!!") == "the-gatsby"


def test_new_client_creates_directory(tmp_path: Path) -> None:
    config = Config()
    config._config_dir = tmp_path
    created = new_client("Club Moon", config=config)
    assert created.exists()
    assert created.name == "club-moon"
    assert created.parent.parent == config.data_dir


def test_new_client_rejects_empty_slug(tmp_path: Path) -> None:
    config = Config()
    config._config_dir = tmp_path
    with pytest.raises(ValueError):
        new_client("!!!", config=config)


def test_client_dir_rejects_empty_slug(tmp_path: Path) -> None:
    config = Config()
    config._config_dir = tmp_path
    with pytest.raises(ValueError):
        client_dir("!!!", config=config)


def test_client_dir_does_not_require_existence(tmp_path: Path) -> None:
    config = Config()
    config._config_dir = tmp_path
    path = client_dir("club-moon", config=config)
    assert not path.exists()
    assert path.name == "club-moon"


def test_multiple_clients_are_siblings(tmp_path: Path) -> None:
    config = Config()
    config._config_dir = tmp_path
    a = new_client("club-moon", config=config)
    b = new_client("the-gatsby", config=config)
    assert a.parent == b.parent
