#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'这是一个文档注释'

__author__ = 'Alvin Wang'

import json

def parse_json(js):
	match_id = []
	barracks_status_dire = []
	barracks_status_radiant = []
	chat = []
	cluster = []
	cosmetics = []
	dire_score = []
	draft_timings = []
	duration = []
	engine = []
	first_blood_time = []
	game_mode = []
	human_players = []
	leagueid = []
	lobby_type = []
	match_seq_num = []
	negative_votes = []
	objectives = []
	picks_bans = []
	positive_votes = []
	radiant_gold_adv = []
	radiant_score = []
	radiant_win = []
	radiant_xp_adv = []
	skill = []
	start_time = []
	teamfights = []
	tower_status_dire = []
	tower_status_radiant = []
	version = []
	replay_salt = []
	series_id = []
	series_type = []
	league = []
	dire_team = []
	radiant_team = []
	players = []
	patch = []
	region = []
	all_word_counts = []
	my_word_counts = []
	comeback = []
	stomp = []
	replay_url = []
 	# ============================================================
	match_id.append(js['match_id'])
	barracks_status_dire.append(js['barracks_status_dire'])
	barracks_status_radiant.append(js['barracks_status_radiant'])
	chat.append(js['chat'])
	cluster.append(js['cluster'])
	cosmetics.append(js['cosmetics'])
	dire_score.append(js['dire_score'])
	draft_timings.append(js['draft_timings'])
	duration.append(js['duration'])
	engine.append(js['engine'])
	first_blood_time.append(js['first_blood_time'])
	game_mode.append(js['game_mode'])
	human_players.append(js['human_players'])
	leagueid.append(js['leagueid'])
	lobby_type.append(js['lobby_type'])
	match_seq_num.append(js['match_seq_num'])
	negative_votes.append(js['negative_votes'])
	objectives.append(js['objectives'])
	picks_bans.append(js['picks_bans'])
	positive_votes.append(js['positive_votes'])
	radiant_gold_adv.append(js['radiant_gold_adv'])
	radiant_score.append(js['radiant_score'])
	radiant_win.append(js['radiant_win'])
	radiant_xp_adv.append(js['radiant_xp_adv'])
	skill.append(js['skill'])
	start_time.append(js['start_time'])
	teamfights.append(js['teamfights'])
	tower_status_dire.append(js['tower_status_dire'])
	tower_status_radiant.append(js['tower_status_radiant'])
	version.append(js['version'])
	replay_salt.append(js['replay_salt'])
	series_id.append(js['series_id'])
	series_type.append(js['series_type'])
	league.append(js['league'])
	dire_team.append(js['dire_team'])
	radiant_team.append(js['radiant_team'])
	players.append(js['players'])
	patch.append(js['patch'])
	region.append(js['region'])
	all_word_counts.append(js['all_word_counts'])
	my_word_counts.append(js['my_word_counts'])
	comeback.append(js['comeback'])
	stomp.append(js['stomp'])
	replay_url.append(js['replay_url'])




def main():
	matchs_id = ["3704280890"]#, "3704183534", "3704076062", "3703959697", "3703866531"]
	for i in matchs_id:
		data = get_match(i)
		print("==================================")
		print(data)
		print(data.keys())
		print(data['match_id']
		print(data['barracks_status_dire']
		print(data['barracks_status_radiant']
		print(data['chat']
		print(data['cluster']
		print(data['cosmetics']
		print(data['dire_score']
		print(data['draft_timings']
		print(data['duration']
		print(data['engine']
		print(data['first_blood_time']
		print(data['game_mode']
		print(data['human_players']
		print(data['leagueid']
		print(data['lobby_type']
		print(data['match_seq_num']
		print(data['negative_votes']
		print(data['objectives']
		print(data['picks_bans']
		print(data['positive_votes']
		print(data['radiant_gold_adv']
		print(data['radiant_score']
		print(data['radiant_win']
		print(data['radiant_xp_adv']
		print(data['skill']
		print(data['start_time']
		print(data['teamfights']
		print(data['tower_status_dire']
		print(data['tower_status_radiant']
		print(data['version']
		print(data['replay_salt']
		print(data['series_id']
		print(data['series_type']
		print(data['radiant_team']
		print(data['league']
		print(data['dire_team']
		print(data['players']
		print(data['patch']
		print(data['region']
		print(data['all_word_counts']
		print(data['my_word_counts']
		print(data['throw']
		print(data['loss']
		print(data['replay_url']




if __name__ == "__main__":
	main()



#===========================================================
#
#===========================================================