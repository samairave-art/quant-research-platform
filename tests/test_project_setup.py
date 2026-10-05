from config.settings import (
    PROJECT_NAME,
    PROJECT_VERSION,
)


def test_project_metadata():
    assert PROJECT_NAME == "Quantitative Research & Algorithmic Trading Platform"
    assert PROJECT_VERSION == "0.1.0"


def test_project_version_format():
    parts = PROJECT_VERSION.split(".")

    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)