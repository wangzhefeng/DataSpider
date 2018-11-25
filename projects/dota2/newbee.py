#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import pandas as pd
import json



def get_match(match_id):
	url = "https://api.opendota.com/api/matches/%s" % match_id
	response = requests.get(url = url)
	if response.status_code == 200:
		data_dict = json.loads(response.text)
	return data_dict


def main():
	matchs_id = ["3704280890", "3704183534", "3704076062", "3703959697", "3703866531"]
	for i in matchs_id:
		data = get_match(i)
		print("==================================")
		print(data)
		df = pd.DataFrame(data)
		print(df)
		df.to_csv("/home/wangzhefeng/project/python/dota/test.csv")




if __name__ == "__main__":
	main()
