from visual import get_visual_TOP10
from get_id import get_city_id
from city_detail import city_detail_deal

if __name__ == '__main__':
    get_city_id()
    c = city_detail_deal()
    c.get_detail_info()
    get_visual_TOP10()