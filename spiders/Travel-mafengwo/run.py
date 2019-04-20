from visual import get_visual_TOP10
from get_id import get_city_id
from city_detail import city_detail_deal

if __name__ == '__main__':
    get_city_id()    # 获得城市id
    c = city_detail_deal()
    c.get_detail_info()  # 获得城市具体内容
    get_visual_TOP10()  # 食物，景点 TOP10可视化