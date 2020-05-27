# 使用方法: 命令行输入 python3 get_opendota_data.py，或者双击这个文件。
# 目的: 从opendota.com下载比赛数据
# 方法: 先找到一些玩家的账号，然后找每个玩家玩过的比赛，下载这些比赛。
# 蓝珲 2020-03-05

import json
import time
import requests
import re

API_URL = 'https://api.opendota.com/api/'
SLEEP_SECONDS = 2  # 访问API网址间隔时间
MAX_PLAYER  = 2    # 考虑的玩家个数
MAX_MATCH = 100      # 下载比赛场次


##########################################################
def get_json_given_url(url):
    return requests.get(url).content


##########################################################
# main

all_matches = []


#print('Get player information ...')
#s = get_json_given_url(API_URL + 'playersByRank')
#lst = json.loads(s)

#for player in lst[:min(MAX_PLAYER, len(lst))]:
   # account_id = player['account_id']
matches = json.loads(get_json_given_url(API_URL + 'parsedmatches?less_than_match_id=5336349194'))
for match in matches:
    match_id = match['match_id']
    if not match_id in all_matches:
        all_matches.append(match_id)
   
  #  print(account_id)
  #  time.sleep(SLEEP_SECONDS)

print('Get match information ...')

d = {}
f = open('matches.txt','w', encoding='utf8')
num_matches = len(all_matches)
for match_id in sorted(all_matches)[:min(MAX_MATCH,num_matches)]:
    time.sleep(SLEEP_SECONDS)
    print(match_id)
    d[match_id] = json.loads(get_json_given_url(API_URL + 'matches/%s' % (match_id)))
   # print(d[match_id]['barracks_status_dire'])
    # s = json.dump(d[match_id]['barracks_status_dire'], f, ensure_ascii=False, sort_keys=False)
    s = json.dump(d[match_id]['match_id'], f, indent=4, ensure_ascii=False, sort_keys=False)
    f.write("\t");
    s = json.dump(d[match_id]['radiant_win'], f, indent=4, ensure_ascii=False, sort_keys=False)
    f.write("\t");
    s = json.dump(d[match_id]['duration'], f, indent=4, ensure_ascii=False, sort_keys=False)
    f.write("\t");
    s = json.dump(d[match_id]['barracks_status_radiant'], f, indent=4, ensure_ascii=False, sort_keys=False)
    f.write("\t");
    s = json.dump(d[match_id]['barracks_status_dire'], f, indent=4, ensure_ascii=False, sort_keys=False)
    f.write("\t");
    s = json.dump(d[match_id]['tower_status_radiant'], f, indent=4, ensure_ascii=False, sort_keys=False)
    f.write("\t");
    s = json.dump(d[match_id]['tower_status_dire'], f, indent=4, ensure_ascii=False, sort_keys=False)
    f.write("\t");
    for x in d[match_id]['players']:
        s = json.dump(x['hero_id'], f, indent=4, ensure_ascii=False, sort_keys=False)
        f.write("\t");
        s = json.dump(x['hero_damage'], f, indent=4, ensure_ascii=False, sort_keys=False)
        f.write("\t");
        s = json.dump(x['tower_damage'], f, indent=4, ensure_ascii=False, sort_keys=False)
        f.write("\t");
        s = json.dump(x['total_xp'], f, indent=4, ensure_ascii=False, sort_keys=False)
        f.write("\t");
        s = json.dump(x['total_gold'], f, indent=4, ensure_ascii=False, sort_keys=False)
        f.write("\t");
    f.write("\n");

print('Write match information to matches.txt ...')

f.close()
    
    
    
  
