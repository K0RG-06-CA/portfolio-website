from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_accessible_placeholder():
    html = (ROOT / "index.html").read_text(encoding="utf-8")

    for snippet in (
        "<!doctype html>",
        '<html lang="en">',
        'name="viewport" content="width=device-width, initial-scale=1"',
        "<main>",
        "<h1>David Ahn</h1>",
        "<title>David Ahn — Engineering student</title>",
        "Engineering student",
        "under construction",
        'href="styles.css"',
    ):
        assert snippet in html


def test_white_responsive_shell():
    css = (ROOT / "styles.css").read_text(encoding="utf-8")

    assert "background: #fff;" in css
    assert "min-height: 100dvh;" in css
    assert "max-width: 32rem;" in css


def test_planning_files_stay_out_of_public_repo():
    ignored = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()

    assert ".claude/" in ignored
    assert "task_plan.md" in ignored
