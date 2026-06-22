from pathlib import Path
import json
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "name": "Origin Asset",
        "schema": ROOT / "schemas" / "origin-asset.schema.json",
        "example": ROOT / "examples" / "origin-asset.example.yaml",
    },
    {
        "name": "Derivative Asset",
        "schema": ROOT / "schemas" / "derivative-asset.schema.json",
        "example": ROOT / "examples" / "derivative-asset.example.yaml",
    },
    {
        "name": "Origin Audit Record",
        "schema": ROOT / "schemas" / "origin-audit-record.schema.json",
        "example": ROOT / "examples" / "origin-audit-record.example.yaml",
    },
    {
        "name": "Royalty Allocation Graph",
        "schema": ROOT / "schemas" / "royalty-allocation-graph.schema.json",
        "example": ROOT / "examples" / "royalty-allocation-graph.example.yaml",
    },
    {
        "name": "Marketplace Listing",
        "schema": ROOT / "schemas" / "marketplace-listing.schema.json",
        "example": ROOT / "examples" / "marketplace-listing.example.yaml",
    },
]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if data is None:
        raise ValueError(f"{path} is empty")

    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML object at the root")

    return data


def validate_target(name: str, schema_path: Path, example_path: Path) -> bool:
    print(f"[validate] {name}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    if not schema_path.exists():
        print(f"[error] schema file not found: {schema_path}", file=sys.stderr)
        return False

    if not example_path.exists():
        print(f"[error] example file not found: {example_path}", file=sys.stderr)
        return False

    try:
        schema = load_json(schema_path)
        example = load_yaml(example_path)

        Draft202012Validator.check_schema(schema)

        validator = Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        )

        errors = sorted(
            validator.iter_errors(example),
            key=lambda error: list(error.path),
        )

        if errors:
            print(f"[error] {name} validation failed", file=sys.stderr)
            for error in errors:
                path = ".".join(str(part) for part in error.path)
                if not path:
                    path = "<root>"
                print(f"  - path: {path}", file=sys.stderr)
                print(f"    message: {error.message}", file=sys.stderr)
            return False

        print(f"[ok] {name} example is valid")
        return True

    except Exception as exc:
        print(f"[error] {name} validation crashed", file=sys.stderr)
        print(f"  {type(exc).__name__}: {exc}", file=sys.stderr)
        return False


def main() -> int:
    all_ok = True

    for target in VALIDATION_TARGETS:
        ok = validate_target(
            name=target["name"],
            schema_path=target["schema"],
            example_path=target["example"],
        )
        all_ok = all_ok and ok

    if all_ok:
        print("[done] all examples are valid")
        return 0

    print("[failed] one or more examples are invalid", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

