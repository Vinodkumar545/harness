
from utils import web_driver
from functions import api_requests

from IPython import embed
import glob
import json
import time
import re
import os

URL = "https://www.highcharts.com/demo/column-stacked"

def retrieve_graph_information(driver):
    try:
        result = {}

        driver.get(URL)
        driver.set_page_load_timeout(30)

        y_axis = driver.find_element_by_xpath("//*[@class='highcharts-axis-title']//*[name()='tspan']").text

        result['url'] = URL
        result['y_axis'] = y_axis

        series_xpath = "//*[name()='g' and @class='highcharts-series-group']//*[name()='g' and @role='region']"
        series_group = driver.find_elements_by_xpath(series_xpath)

        data = {}
        for i in range(1, len(series_group) + 1):
            rects_xpath = "%s[%s]//*[name()='rect']"%(series_xpath, i)
            rects = driver.find_elements_by_xpath(rects_xpath)

            fruit_consumption, fruit_name = {}, {}
            for rect in rects:
                details = rect.get_attribute('aria-label')

                li = re.split(r'\d+', details)
                fruit = re.sub(r'\W', '', li[1])

                total_fruit = int(''.join(re.findall(r'\d', details)[-1]))

                name = re.split(r'\s', details)[-1][:-1]


                if fruit not in data.keys():
                    data[fruit] = {name: total_fruit}
                else:
                    data[fruit].update({name: total_fruit})


        total_values = {}
        for fruit in data:
            total_values[fruit] = sum(data[fruit].values())

        result['data'] = data
        result['total'] = total_values

        time.sleep(5)
        driver.find_element_by_xpath("//button[@aria-label='View chart menu' and @class='highcharts-a11y-proxy-button']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//li[contains(text(),'Download PNG image')]").click()
        time.sleep(10) # wait for file to be downloaded

        list_of_files = glob.glob(web_driver.SCREENSHOTS+'/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        result['png'] = latest_file

        print(json.dumps(result))

        with open(os.path.join(web_driver.OUTPUT, 'column_stacked.json'), 'w') as wf:
            json.dump(result, wf)

    except Exception as e:
        print('Exception: %s'%(e))

    return result


def assertion_of_result(exp_output, act_output):
    result = []
    for fruit_details in exp_output['y-axis']:
        for fruit, values in fruit_details.items():
            for name, no in values.items():
                if act_output['data'][fruit][name] == no:
                    result.append(True)
                else:
                    result.append(False)

    return result

