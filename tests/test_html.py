from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"
BOOTSTRAP_CSS = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
BOOTSTRAP_ICONS = "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"
BOOTSTRAP_JS = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
CUSTOM_CSS = "../assets/css/styles.css"
CUSTOM_JS = "../assets/js/scripts.js"


@pytest.fixture(scope="module")
def html_files():
    return sorted(TEMPLATES.glob("*.html"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


@pytest.mark.parametrize("expected", [BOOTSTRAP_CSS, BOOTSTRAP_ICONS, CUSTOM_CSS])
def test_stylesheets_present(html_files, expected):
    for html_file in html_files:
        contents = read_text(html_file)
        assert expected in contents, f"{expected} missing from {html_file.name}"


@pytest.mark.parametrize("expected", [BOOTSTRAP_JS, CUSTOM_JS])
def test_scripts_present(html_files, expected):
    for html_file in html_files:
        contents = read_text(html_file)
        assert expected in contents, f"{expected} missing from {html_file.name}"


@pytest.mark.parametrize("class_name", ["navbar", "container", "card"])
def test_common_bootstrap_classes(html_files, class_name):
    for html_file in html_files:
        contents = read_text(html_file)
        assert class_name in contents, f"Expected class '{class_name}' missing from {html_file.name}"


def test_index_has_core_sections():
    index_html = read_text(TEMPLATES / "index.html")
    for section_id in [
        "hero",
        "features",
        "services",
        "portfolio",
        "pricing",
        "testimonials",
        "blog",
        "faq",
        "newsletter",
        "contact",
    ]:
        assert f'id="{section_id}"' in index_html, f"Section #{section_id} missing from index.html"


@pytest.mark.parametrize(
    "page,keywords",
    [
        ("about.html", ["Our mission", "Leadership", "Our values"]),
        ("services.html", ["Strategy", "Product Design", "Growth Marketing"]),
        ("portfolio.html", ["Case studies", "More Projects"]),
        ("blog.html", ["Ideas, frameworks", "Featured"]),
        ("contact.html", ["Tell us about your project", "Frequently asked questions"]),
        ("newsletter.html", ["Join 25,000+ professionals", "Recent issues"]),
    ],
)
def test_page_copy_exists(page, keywords):
    contents = read_text(TEMPLATES / page)
    for keyword in keywords:
        assert keyword in contents, f"'{keyword}' not found in {page}"
