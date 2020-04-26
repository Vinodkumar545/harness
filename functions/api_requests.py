
import requests


def api_request_for_column_with_drilldown_hardcoded():

    # API GET request to retrieve the graph details

    return_json = {
        'x-axis': ['Chrome', 'Firefox', 'Internet Explorer', 'Safari', 'Edge', 'Opera', 'Other'],
        'y-axis': ['62.74%', '10.57%', '7.23%', '5.58%', '4.02%', '1.92%', '7.62%']
    }

    return return_json


def api_request_for_column_stacked_harcoded():

    # API GET request to retrieve the graph details

    return_json = {
        'x-axis': ['Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas'],
        'y-axis': [{
                'Apples': {
                    'John': 5,
                    'Jane': 2,
                    'Joe': 3
                },
                'Oranges': {
                    'John': 3,
                    'Jane': 2,
                    'Joe': 4
                },
                'Pears': {
                    'John': 4,
                    'Jane': 3,
                    'Joe': 4
                },
                'Grapes': {
                    'John': 7,
                    'Jane': 2,
                    'Joe': 2
                },
                'Bananas': {
                    'John': 2,
                    'Jane': 1,
                    'Joe': 5
                }
            }]
    }

    return return_json

