import pathlib
import tomli

path = pathlib.Path(__file__).parent / "config_module_import_1.toml"
with path.open(mode="rb") as fp:
    mod_import_1 = tomli.load(fp)

path = pathlib.Path(__file__).parent / "config_module_import_2.toml"
with path.open(mode="rb") as fp:
    mod_import_2 = tomli.load(fp)
