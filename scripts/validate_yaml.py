#!/usr/bin/env python3
from pathlib import Path

import yaml


class HomeAssistantLoader(yaml.SafeLoader):
    pass


HomeAssistantLoader.add_constructor(
    "!secret", lambda loader, node: loader.construct_scalar(node)
)


FILES = (
    Path("home-assistant/packages/vnish_antminer_package.yaml"),
    Path("home-assistant/dashboards/vnish_antminer_card.yaml"),
)


for path in FILES:
    with path.open(encoding="utf-8") as source:
        document = yaml.load(source, Loader=HomeAssistantLoader)
    if not isinstance(document, dict):
        raise ValueError(f"{path} no contiene un documento YAML raíz válido")
    print(f"OK: {path}")
