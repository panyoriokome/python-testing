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
    """ð§sloppy docstring parserð§"""
    lines = docstring.splitlines()
    sections = _parse_section(lines)
    return dict(map(lambda x: (x[1], _parse_content(x[0], lines)), sections))


def pytest_html_report_title(report):
    report.title = "ãã¹ãä»æ§æ¸" # ã¤ãã§ã«ã¬ãã¼ãã¿ã¤ãã«ãå¤æ´


# def pytest_configure(config):
#     config._metadata["Version"] = "9.9.9" # ã¤ãã§ã«Versionæå ±ãè¿½å 


def pytest_html_results_table_header(cells):
    del cells[1:]
    cells.insert(0, html.th("Tests"))
    cells.insert(1, html.th("Expects"))
    cells.append(html.th("Time", class_="sortable time", col="time"))


def pytest_html_results_table_row(report, cells):
    del cells[1:]
    cells.insert(0, html.td(report.tests)) #ããã¹ãåå®¹ããã¬ãã¼ãã«åºå
    cells.insert(1, html.td(report.expects)) #ãæå¾çµæããã¬ãã¼ãã«åºå
    cells.append(html.td(datetime.now(), class_="col-time")) #ã¤ãã§ã«ãæéããã¬ãã¼ãã«åºå


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    docstring = parse(str(item.function.__doc__))
    report.tests = docstring["Tests"] #ããã¹ãåå®¹ãã`report`ã«è¿½å 
    report.expects = docstring["Expects"] #ãæå¾çµæãã`report`ã«è¿½å 