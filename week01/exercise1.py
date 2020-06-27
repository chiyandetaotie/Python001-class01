import requests,pandas
from bs4 import BeautifulSoup as bs


def get_url_info(myurl):
    film_list = []
    headers = {
        'Cookie': 'uuid_n_v=v1; uuid=4D902480B5BD11EAB7FDDF490BC946C0C5FE887490594FB29BD13F21D952C08F; mojo-uuid=d251cad6b98bacd0c9eb30a6b1d3cdda; _lxsdk_cuid=172e4066b2ac8-0711cfd3dd16d2-3e7e045d-1fa400-172e4066b2ac8; _lxsdk=4D902480B5BD11EAB7FDDF490BC946C0C5FE887490594FB29BD13F21D952C08F; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592963525,1592964015,1593210160; _csrf=0dba9a1afdd6ec75f5852348aa7fc31751b5a10738d3e6273d854c71d93b1a4e; mojo-session-id={"id":"f457fa4dbe0c244d7c407fad498d788e","time":1593210160200}; mojo-trace-id=6; __mta=249975481.1592963525551.1592964792303.1593210201034.9; _lxsdk_s=172f2b9c420-109-53-87%7C%7C11',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    response = requests.get(myurl, headers=headers)
    bs_info = bs(response.text, 'html.parser')
    for movie in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}, limit=10):
        # name = movie.find(class_='name').text
        movie_info = movie.find_all(class_='movie-hover-title')
        name = movie_info[0].find(class_='name').text.strip()
        tag = movie_info[1].text.strip()
        time = movie_info[3].text.strip()
        flim = {'name': name, 'tag': tag, 'time': time}
        film_list.append(flim)
    return film_list

# 'Cookie': 'uuid_n_v=v1; uuid=CF2A5180B44D11EA8C8DE3118EB8AC1A4B40B5FBD2F74EE1A61F05482897D817; mojo-uuid=f011bf395319af23ad9f86e1224dcca8; _lxsdk_cuid=172da9e4a3ec8-0d5ee2f5940bb7-f7d123e-144000-172da9e4a3ec8; _lxsdk=CF2A5180B44D11EA8C8DE3118EB8AC1A4B40B5FBD2F74EE1A61F05482897D817; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592805708,1592830877,1592830931,1592830942; _csrf=cbbfe141e303af35121ffe5efb857746a4e3adb2a0639fe89dd0efbc5db771a2; mojo-session-id={"id":"101dbc0195ca482927d1f5dd106536ab","time":1592869913808}; mojo-trace-id=2; __mta=55409172.1592805708597.1592831009924.1592869934788.10; _lxsdk_s=172de7204ef-e6e-0fe-c32%7C%7C4',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'


url = 'https://maoyan.com/films?showType=3'
film_list = get_url_info(url)

print(film_list)

movie = pandas.DataFrame(film_list)
movie.to_csv('./request_bs4_maoyan_top10.csv',index=False)
