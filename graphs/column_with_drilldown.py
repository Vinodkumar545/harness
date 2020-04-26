
from utils import web_driver
from functions import api_requests

from IPython import embed
import glob
import json
import time
import re
import os

URL = "https://www.highcharts.com/demo/column-drilldown"

def retrieve_graph_information(driver):
    try:
        result = {}

        driver.get(URL)
        driver.set_page_load_timeout(30)

        chart_title = driver.find_element_by_xpath("//*[name()='text' and @class='highcharts-title']//*[name()='tspan']").text
        y_axis = driver.find_element_by_xpath("//*[name()='text' and @class='highcharts-axis-title']//*[name()='tspan']").text
        x_axis = 'Various Browser'

        result['url'] = URL
        result['title'] = chart_title
        result['y_axis'] = y_axis
        result['x_axis'] = x_axis

        data = {}
        series_group = driver.find_elements_by_xpath("//*[name()='g' and @class='highcharts-series-group']//*[name()='rect']") 
        for rect in series_group:
            details = rect.get_attribute('aria-label')
            browser = re.findall(r"\B\D+", details)[0].strip()[:-1]
            share = re.split(r" ", details)[-1][:-1] + '%'

            data[browser] = share

        result['data'] = data

        driver.find_element_by_xpath("//button[@class='highcharts-a11y-proxy-button']").click()
        driver.find_element_by_xpath("//li[contains(text(),'Download PNG image')]").click()
        time.sleep(10) # wait for file to be downloaded

        list_of_files = glob.glob(web_driver.SCREENSHOTS+'/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        result['png'] = latest_file

        print(json.dumps(result))

        with open(os.path.join(web_driver.OUTPUT, 'column_drilldown.json'), 'w') as wf:
            json.dump(result, wf)

    except Exception as e:
        print('Exception: %s'%(e))

    return result


def assertion_of_result(exp_output, act_output):
    result = []
    for index, browser in enumerate(exp_output['x-axis']):
        if exp_output['y-axis'][index] == act_output['data'][browser]:
            result.append(True)
        else:
            result.append(False)

    return result


