from datetime import datetime
from py.xml import html  # type: ignore
import pytest

import re
from itertools import takewhile


_section_rgx = re.compile(r"^\s*[a-zA-Z]+:\s*$")
_lspace_rgx = re.compile(r"^\s*")


def _parse_section(lines: list[str]) -> list[tuple[int, str]]:
    matches = map(lambda x: _section_rgx.match(x), lines)
    indexes = [i for i, x in enumerate(matches) if x is not None]
    return list(map(lambda x: (x, lines[x].strip()[:-1]), indexes))


def _count_lspace(s: str) -> int:
    rgx = _lspace_rgx.match(s)
    if rgx is not None:
        return rgx.end()
    return 0


def _parse_content(index: int, lines: list[str]) -> str:
    lspace = _count_lspace(lines[index])
    i = index + 1
    contents = takewhile(lambda x: _count_lspace(x) > lspace, lines[i:])
    return "".join(map(lambda x: x.strip(), contents))


def parse(docstring: str) -> dict[str, str]:
    """🚧sloppy docstring parser🚧"""
    lines = docstring.splitlines()
    sections = _parse_section(lines)
    return dict(map(lambda x: (x[1], _parse_content(x[0], lines)), sections))


def pytest_html_report_title(report):
    report.title = "テスト仕様書" # ついでにレポートタイトルを変更


# def pytest_configure(config):
#     config._metadata["Version"] = "9.9.9" # ついでにVersion情報を追加


def pytest_html_results_table_header(cells):
    del cells[1:]
    cells.insert(0, html.th("Tests"))
    cells.insert(1, html.th("Expects"))
    cells.append(html.th("Time", class_="sortable time", col="time"))


def pytest_html_results_table_row(report, cells):
    del cells[1:]
    cells.insert(0, html.td(report.tests)) #「テスト内容」をレポートに出力
    cells.insert(1, html.td(report.expects)) #「期待結果」をレポートに出力
    cells.append(html.td(datetime.now(), class_="col-time")) #ついでに「時間」もレポートに出力


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    docstring = parse(str(item.function.__doc__))
    report.tests = docstring["Tests"] #「テスト内容」を`report`に追加
    report.expects = docstring["Expects"] #「期待結果」を`report`に追加