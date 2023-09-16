import requests
from bs4 import BeautifulSoup
from lxml import html
#pip install beautifulsoup4
#pip install lxml

# 정보 스크래핑
def scrap_tourist_site_info(tourist_site:str)->str:
    """_summary_

    Args:
        tourist_site (str):관광지의 이름을 입력받음

    Returns:
        str: 관광지 내용을 스크래핑하고 그 결과를 반환
    """
    # 페이지 URL 
    url = f"https://ko.wikipedia.org/wiki/{tourist_site}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # HTML 문자열을 lxml.etree.Element 객체로 파싱인데 신기하쥬?
    root = html.fromstring(response.text)

    # XPath 주소 설정
    xpath_address = '//*[@id="mw-content-text"]/div[1]/p[2]'

    result = root.xpath(xpath_address)
    if result:
        description = result[0].text_content()
    else:
        description = "관광지 정보를 찾을 수 없습니다."
    
    return description

if __name__ == "__main__":
# 관광지 이름 입력
    tourist_site = input("검색할 관광지 이름을 입력하세요: ")

    # 관광지 정보 스크래핑
    tourist_site_info = scrap_tourist_site_info(tourist_site)
    print("관광지 정보:")
    print(tourist_site_info)