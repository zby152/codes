import json
from country_codes import get_country_code
import pygal_maps_world
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

filename = 'population_data.json'

# 将数据转化成一个列表
with open(filename) as f:
    pop_data = json.load(f)

# 存储国别码和人口数量
cc_populations = {}
# 遍历列表中的每一个字典读取年份是2010年的所有数据
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))  # 不能将带有小数点的字符直接转换成小数
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# 按照人口数量对所有的国家进行分组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 查看每组的国家数量
# print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

# 绘制地图
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = 'Populations in 2010,by country'
wm.add("0-10m", cc_pops_1)
wm.add("10m-1bn", cc_pops_2)
wm.add(">1bn", cc_pops_3)

wm.render_to_file('world_populations.svg')
