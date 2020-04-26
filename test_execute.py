
from utils import web_driver
from functions import api_requests
from graphs import (
        column_stacked,
        column_with_drilldown
    )

import pytest


@pytest.fixture(scope='function')
def driver(request):

    driver = web_driver.initiate_webdirver(headless=False)
    driver.implicitly_wait(10)
    driver.maximize_window()

    def close():
        driver.close()
        driver.quit()

    request.addfinalizer(close)

    return driver


def test_to_assert_graph_of_column_with_drilldown(driver):

    exp_output = api_requests.api_request_for_column_with_drilldown_hardcoded()

    act_output = column_with_drilldown.retrieve_graph_information(driver)

    result = column_with_drilldown.assertion_of_result(exp_output, act_output)

    assert all(result)


def test_to_assert_grapth_of_column_stacked(driver):

    exp_output = api_requests.api_request_for_column_stacked_harcoded()

    act_output = column_stacked.retrieve_graph_information(driver)

    result = column_stacked.assertion_of_result(exp_output, act_output)

    assert all(result)


