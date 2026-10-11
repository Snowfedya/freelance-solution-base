import json
from pathlib import Path


def test_catalog_is_valid_and_has_required_keys():
    catalog_path = Path(__file__).resolve().parent.parent / "catalog.json"
    data = json.loads(catalog_path.read_text())
    solutions = data.get("solutions", [])
    assert len(solutions) >= 8

    required_keys = {
        "id",
        "type",
        "target_order_classes",
        "repo",
        "license",
        "status",
        "test_summary",
        "adaptation_hours",
        "risk",
    }
    for item in solutions:
        assert required_keys.issubset(item.keys())
        assert item["license"] in {"MIT", "Apache-2.0", "BSD-3-Clause"}
        assert item["type"] in {
            "fork",
            "starter",
            "reference_dependency",
            "reference_service",
            "reference_tool",
        }


def test_forks_and_starters_point_to_user_repos():
    catalog_path = Path(__file__).resolve().parent.parent / "catalog.json"
    data = json.loads(catalog_path.read_text())
    solutions = data.get("solutions", [])

    owned = [s for s in solutions if s["type"] in {"fork", "starter"}]
    assert len(owned) == 4
    for item in owned:
        assert item["repo"].startswith("Snowfedya/")
