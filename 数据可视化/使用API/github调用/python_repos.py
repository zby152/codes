import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def print_information(repo_dict):
    """打印对应仓库的信息"""
    # 打印键的数量
    # print("\nKeys:", len(repo_dict))

    # 打印所有的键
    # for key in sorted(repo_dict.keys()):
    #     print(key)

    # 打印相关信息
    print("\nSelected information about first repository:")
    print("Name:", repo_dict['name'])
    print("Owner:", repo_dict['owner']['login'])
    print("Stars:", repo_dict['stargazers_count'])
    print("Repository:", repo_dict['html_url'])
    print("Created:", repo_dict['created_at'])
    print("Updated:", repo_dict['updated_at'])
    print("Description:", repo_dict['description'])


if __name__ == "__main__":
    # 执行调用并存储响应
    url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
    r = requests.get(url)
    print("Status code:", r.status_code)

    # 总的响应的json文件,打印总的python仓库的个数
    response_dict = r.json()
    print("Total repositories:", response_dict['total_count'])

    # 能够获得的仓库的个数
    repo_dicts = response_dict['items']
    # print("Repositories returned:", len(repo_dicts))

    # 研究第一个仓库的信息,打印其键的数量
    # print_information(repo_dicts[0])

    # 打印所有的仓库的信息
    for repo_dict in repo_dicts:
        print_information(repo_dict)

    # 获取每个仓库的星的信息
    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        plot_dict = {'value': repo_dict['stargazers_count'], 'label': repo_dict['description'],
                     'xlink': repo_dict['html_url']}
        plot_dicts.append(plot_dict)

    # 定制图表的外观
    my_style = LS('#336699', base_style=LCS)
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_lengend = False
    my_config.title_font_size = 24  # 图表标题字号
    my_config.label_font_size = 14  # 图标副标签字号
    my_config.major_label_font_size = 18  # 图表主标签字号y轴刻度
    my_config.truncate_label = 15  # 将较长的项目名缩短为15字符
    my_config.show_y_guides = False  # 隐藏图表中的水平线
    my_config.which = 1000  # 自定义宽度

    chart = pygal.Bar(my_config, style=my_style)  # x轴的标签旋转45度,隐藏图例
    chart.title = "Most-Stared Python Projects on Github"
    chart.x_labels = names

    chart.add('', plot_dicts)
    chart.render_to_file('python_repos.svg')
