#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import pandas as pd

def get_match(match_id):
	url = "https://api.opendota.com/api/matches/%s" % match_id
	response = requests.get(url = url)
	if response.status_code == 200:
		js = json.loads(response.text)
	return js

# players

# def get_players():
# 	url = 


def parse_json(js):
	match_id = []
	barracks_status_dire = []
	barracks_status_radiant = []
	cluster = []
	dire_score = []
	duration = []
	engine = []
	first_blood_time = []
	game_mode = []
	human_players = []
	leagueid = []
	lobby_type = []
	match_seq_num = []
	negative_votes = []
	positive_votes = []
	radiant_score = []
	radiant_win = []
	skill = []
	start_time = []
	tower_status_dire = []
	tower_status_radiant = []
	version = []
	replay_salt = []
	series_id = []
	series_type = []
	patch = []
	region = []
	my_word_counts = []
	throw = []
	loss = []
	replay_url = []
	chat = []
	cosmetics = []
	draft_timings = []
	objectives = []
	picks_bans = []
	radiant_gold_adv = []
	radiant_xp_adv = []
	teamfights = []
	league = []
	radiant_team = []
	dire_team = []
	players = []
	all_word_counts = []
 	# ============================================================
	match_id.append(js['match_id'])
	barracks_status_dire.append(js['barracks_status_dire'])
	barracks_status_radiant.append(js['barracks_status_radiant'])
	cluster.append(js['cluster'])
	dire_score.append(js['dire_score'])
	duration.append(js['duration'])
	engine.append(js['engine'])
	first_blood_time.append(js['first_blood_time'])
	game_mode.append(js['game_mode'])
	human_players.append(js['human_players'])
	leagueid.append(js['leagueid'])
	lobby_type.append(js['lobby_type'])
	match_seq_num.append(js['match_seq_num'])
	negative_votes.append(js['negative_votes'])
	positive_votes.append(js['positive_votes'])
	radiant_score.append(js['radiant_score'])
	radiant_win.append(js['radiant_win'])
	skill.append(js['skill'])
	start_time.append(js['start_time'])
	tower_status_dire.append(js['tower_status_dire'])
	tower_status_radiant.append(js['tower_status_radiant'])
	version.append(js['version'])
	replay_salt.append(js['replay_salt'])
	series_id.append(js['series_id'])
	series_type.append(js['series_type'])
	patch.append(js['patch'])
	region.append(js['region'])
	my_word_counts.append(js['my_word_counts'])
	throw.append(js['throw'])
	loss.append(js['loss'])
	replay_url.append(js['replay_url'])
	# ------------------------------------
	chat.append(js['chat'])
	cosmetics.append(js['cosmetics'])
	draft_timings.append(js['draft_timings'])
	objectives.append(js['objectives'])
	picks_bans.append(js['picks_bans'])
	radiant_gold_adv.append(js['radiant_gold_adv'])
	radiant_xp_adv.append(js['radiant_xp_adv'])
	teamfights.append(js['teamfights'])
	league.append(js['league'])
	radiant_team.append(js['radiant_team'])
	dire_team.append(js['dire_team'])
	players.append(js['players'])
	all_word_counts.append(js['all_word_counts'])
	df_1 = {
		'match_id': match_id,
		'barracks_status_dire': barracks_status_dire,
		'barracks_status_radiant': barracks_status_radiant,
		'cluster': cluster,
		'dire_score': dire_score,
		'duration': duration,
		'engine': engine,
		'first_blood_time': first_blood_time,
		'game_mode': game_mode,
		'human_players': human_players,
		'leagueid': leagueid,
		'lobby_type': lobby_type,
		'match_seq_num': match_seq_num,
		'negative_votes': negative_votes,
		'positive_votes': positive_votes,
		'radiant_score': radiant_score,
		'radiant_win': radiant_win,
		'skill': skill,
		'start_time': start_time,
		'tower_status_dire': tower_status_dire,
		'tower_status_radiant': tower_status_radiant,
		'version': version,
		'replay_salt': replay_salt,
		'series_id': series_id,
		'series_type': series_type,
		'patch': patch,
		'region': region,
		'my_word_counts': my_word_counts,
		'throw': throw,
		'loss': loss,
		'replay_url': replay_url
	}
	df = pd.DataFrame(df_1)
	return df




	



def main():
	matchs_id = ["3704280890"]#, "3704183534", "3704076062", "3703959697", "3703866531"]
	for i in matchs_id:
		data = get_match(i)
		print(data.keys())
		df = parse_json(data)
		print(df)



if __name__ == "__main__":
	main()



#===========================================================
#
#===========================================================

