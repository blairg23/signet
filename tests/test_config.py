from __future__ import annotations

from pathlib import Path

from signet.config import Config, find_config_file, load_config


def test_default_config_has_expected_paths() -> None:
    config = Config()
    assert config.paths.data_dir == "./data"
    assert config.paths.work_dir == "~/.local/state/signet/work"


def test_load_config_missing_file_returns_defaults(tmp_path: Path) -> None:
    config = load_config(tmp_path / "nonexistent.toml")
    assert config.paths.data_dir == "./data"


def test_load_config_reads_toml(tmp_path: Path) -> None:
    config_path = tmp_path / "signet.toml"
    config_path.write_text(
        '[paths]\ndata_dir = "./mydata"\nwork_dir = "./mywork"\n', encoding="utf-8"
    )
    config = load_config(config_path)
    assert config.paths.data_dir == "./mydata"
    assert config.data_dir == (tmp_path / "mydata").resolve()


def test_data_dir_resolves_relative_to_config_file(tmp_path: Path) -> None:
    nested = tmp_path / "nested"
    nested.mkdir()
    config_path = nested / "signet.toml"
    config_path.write_text('[paths]\ndata_dir = "./data"\n', encoding="utf-8")
    config = load_config(config_path)
    assert config.data_dir == (nested / "data").resolve()


def test_find_config_file_walks_up(tmp_path: Path) -> None:
    (tmp_path / "signet.toml").write_text("", encoding="utf-8")
    child = tmp_path / "a" / "b"
    child.mkdir(parents=True)
    found = find_config_file(child)
    assert found == tmp_path / "signet.toml"


def test_find_config_file_returns_none_when_absent(tmp_path: Path) -> None:
    assert find_config_file(tmp_path) is None


def test_load_config_reads_registry_settings(tmp_path: Path) -> None:
    config_path = tmp_path / "signet.toml"
    config_path.write_text(
        "[registry]\nphash_distance_min = 20\ntuple_overlap_max = 1\n",
        encoding="utf-8",
    )
    config = load_config(config_path)
    assert config.registry.phash_distance_min == 20
    assert config.registry.tuple_overlap_max == 1
