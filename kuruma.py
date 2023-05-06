import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
years = []
distances = []
prices= []


def get_car_data(urls):
    car_list= []
    price_list= []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        car_list= car_list+soup.find_all('div', class_='databox-right')  # 
        price_list =price_list+soup.find_all('div', class_='hontai-price')
    
    
    for element in car_list:
        list = element.find_all('li')
        for li in list:
            if '年式' in li.text:
                year = li.text.replace('', '').strip()
                year = ''.join(filter(str.isdigit, year))
                
            if '走行距離' in li.text:
                distance = li.text.replace('', '').strip()
                distance = ''.join(c for c in distance if c.isdigit() or c == '.')
                 # 
                distance_num = float(distance)
                if distance_num > 30:
                    distance_num =  distance_num*0.001
                    distance=str(distance_num)
            # 
        if year and distance:
            years.append(float(year))
            distances.append(float(distance))
    print(len(years))        
    #price_list =soup.find_all('div', class_='data-wrapper')  # 
    
    for element in price_list:    
        if '車両本体価格 (税込)' in  element.text:
            price = element.text.strip()
            price = ''.join(c for c in price if c.isdigit() or c == '.')
            
            prices.append(float(price))
    print(len(prices)) 
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(distances, years, prices,c=years, cmap='viridis')

    ax.set_xlabel('distances')
    ax.set_ylabel('years')
    ax.set_zlabel('prices')

    plt.show()    
    # 
    return car_data

#url = 'https://www.goo-net.com/usedcar/brand-AUDI/car-A1_SPORTBACK/'  # 
urls = [
    "https://www.goo-net.com/usedcar/brand-AUDI/car-A1_SPORTBACK/",
    "https://www.goo-net.com/usedcar/brand-AUDI/car-A1_SPORTBACK/index-2.html",
    "https://www.goo-net.com/usedcar/brand-AUDI/car-A1_SPORTBACK/index-3.html",
    "https://www.goo-net.com/usedcar/brand-AUDI/car-A1_SPORTBACK/index-4.html",
    "https://www.goo-net.com/usedcar/brand-AUDI/car-A1_SPORTBACK/index-5.html",
    "https://www.goo-net.com/usedcar/brand-AUDI/car-A1_SPORTBACK/index-6.html",
    "https://www.goo-net.com/usedcar/brand-AUDI/car-A1_SPORTBACK/index-7.html",
    "https://www.goo-net.com/usedcar/brand-AUDI/car-A1_SPORTBACK/index-8.html",
    "https://www.goo-net.com/usedcar/brand-AUDI/car-A1_SPORTBACK/index-9.html",
    "https://www.goo-net.com/usedcar/brand-AUDI/car-A1_SPORTBACK/index-10.html"
]
car_data = get_car_data(urls)
#df = pd.DataFrame(car_data)



