import os
import sys
import pytest

# Ensure project root is importable
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Screenshot directory
SCREENSHOT_DIR = os.path.join(PROJECT_ROOT, "reports", "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# Global variable for pytest_html plugin
pytest_html = None


def pytest_configure(config):
    """
    Load the pytest_html plugin so we can use it in hooks.
    """
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Take a screenshot **and embed it** into the HTML report when a test fails.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)

        if page:
            screenshot_path = os.path.join(
                SCREENSHOT_DIR, f"{item.name}.png"
            )
            page.screenshot(path=screenshot_path)

            # Embed screenshot in HTML report
            if pytest_html:
                extra = getattr(report, "extra", [])
                extra.append(pytest_html.extras.image(screenshot_path))
                report.extra = extra
