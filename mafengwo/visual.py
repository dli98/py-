import pandas as pd
from pyecharts import Bar
from pyecharts import Geo, Grid
from save_mongo import db, MONGO_DB
import matplotlib.pyplot as plt


def read_mongo(db, collection, query={}):
    cursor = db[collection].find({'provice_id': {'$ne': '0'}}, query)
    city = []
    for i in cursor:
        city.extend(i['citys'])
    df = pd.DataFrame(city)
    return df

def nums_Top10():
    df = read_mongo(db, MONGO_DB, {'_id': 0, 'citys': 1})
    info = df.sort_values(by='nums')[-15::]
    bar = Bar('热门城市')
    bar.add('热门城市TOP10', info['city_name'], info['nums'], is_splitline_show=False, xaxis_rotate=30)
    return bar


def heat_diagram():
    df =  read_mongo(db, MONGO_DB, {'_id': 0, 'citys': 1})
    i = [i for i in df['city_name']]
    j = [j for j in df['nums']]
    data = list(zip(i, j))
    geo = Geo("全国主要旅游城市", title_color="#fff", title_pos="center",
              width = 1200, height = 600, background_color = '#404a59')
    attr, value = geo.cast(data)
    geo.add("", attr, value, visual_range=[0, 55000], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
    geo.render('旅游景点热力图.html')


def food_top10():
    cursor = db['city_detail'].find({}, {'_id': 0})
    food = []
    for i in cursor:
        for j in i['food']:
            # 将食物名称和所属城市名称拼接
            name = i['city_name'] + '_' + j ['food_name']
            food.append({'food_name': name, 'food_count': j['food_count']})
    df = pd.DataFrame(food)
    food_info = df.sort_values(by='food_count')[-15::]
    bar = Bar('热门食物', title_top="25%")
    bar.add('热门食物TOP10', food_info['food_name'], food_info['food_count'],
            legend_top="25%",is_splitline_show=False, xaxis_rotate=30)
    return bar


def jd_top10():
    cursor = db['city_detail'].find({}, {'_id': 0})
    food = []
    for i in cursor:
        for j in i['jd']:
            # 将景点名称和所属城市名称拼接
            name = i['city_name'] + '_' + j['jd_name']
            food.append({'jd_name': name, 'jd_count': j['jd_count']})
    df = pd.DataFrame(food)
    food_info = df.sort_values(by='jd_count')[-15::]
    bar = Bar('热门景点', title_top="55%")
    bar.add('热门景点TOP10',food_info['jd_name'], food_info['jd_count'],
            legend_top="55%", is_splitline_show=False, xaxis_rotate=30)
    return bar

def get_visual_TOP10():
    bar1 = nums_Top10()
    bar2 = food_top10()
    bar3 = jd_top10()
    grid = Grid(height=1000)
    grid.add(bar1, grid_bottom="80%")
    grid.add(bar2, grid_top="30%", grid_bottom="50%")
    grid.add(bar3, grid_top="60%", grid_bottom="20%")
    grid.render()



if __name__ == '__main__':
    get_visual_TOP10()
