#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import etree

class Login(object):
	def __init__(self):
		self.headers = {
			"Referer": "https://github.com/",
			"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
			"Host": "github.com"
		}
		self.login_url = "https://github.com/login"
		self.post_url = "https://github.com/session"
		self.logined_url = "https://github.com/settings/profile"
		self.session = requests.Session()

	# def __init__(self):
	# 	self.headers = {
	# 		'Referer': 'https://github.com/',
	# 		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
	# 		'Host': 'github.com'
	# 	}
	# 	self.login_url = 'https://github.com/login'
	# 	self.post_url = 'https://github.com/session'
	# 	self.logined_url = 'https://github.com/settings/profile'
	# 	self.session = requests.Session()

	def token(self):
		response = self.session.get(self.login_url, headers = self.headers)
		selector = etree.HTML(response.text)
		token = selector.xpath("//div[@id='login']/form/input[@name='authenticity_token']/@value")[0]
		print(token)
		return token

	def login(self, email, password):
		post_data = {
			"commit": "Sign in",
			"utf8": "✓",
			"authenticity_token": self.token(),
			"login": email,
			"password": password
		}
		response = self.session.post(self.post_url, data = post_data, headers = self.headers)
		# print(response.status_code)
		# print(response.text)
		if response.status_code == 200:
			self.dynamics(response.text)

		response = self.session.get(self.logined_url, headers = self.headers)
		# print(response.status_code)
		# print(response.text)
		if response.status_code == 200:
			self.profile(response.text)

	def dynamics(self, html):
		selector = etree.HTML(html)
		print(selector)
		dynamics = selector.xpath("//div[contains(@class, 'news')]//div[@class='watch_started']")
		print(dynamics)
		for item in dynamics:
			print(item)
			dynamics = " ".join(item.xpath(".//div//a//text()")).strip()
			print(dynamics)


	def profile(self, html):
		selector = etree.HTML(html)
		name = selector.xpath("//input[@id='user_profile_name']/@value")[0]
		email = selector.xpath("//select[@id='user_profile_email']/option[@value!='']/text()")
		print(name, email)

	# def profile(self, html):
	# 	selector = etree.HTML(html)
	# 	name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
	# 	email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
	# 	print(name, email)



def main():
	login = Login()
	login.login(email = "wangzhefengr@163.com", password = "wangzf711235813")


if __name__ == "__main__":
	main()

