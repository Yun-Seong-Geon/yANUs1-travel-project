import numpy as np
from tensorflow import keras
import os

class img_processing:
    """_summary_
    이미지 전처리(라벨링) 클래스
    """    
    categories = [
        'bigben',
        'santorini',
        'Matterhorn',
        'Grand_Canyon',
        'the_statue_of_liberty',
        'eiffel_tower',
        'Gold_gate_bridge',
        'Osakajo',
        'pisa_tower',
        'ayasofya_camii',
        'Donggung_Palace_and_Wolji_Pond',
        'Gobi_Desert',
        'Iceland_Aurora',
        'kuta_beach',
        'Machu_Picchu',
        'Niagara_falls',
        'Pyramid',
        'Sydney_Opera_House',
        'Torre_pendente_di_Pisa',
        'Wat_Chedi_Luang'
    ] # 지역이름 추가하기
    
    def img_label(path,region:(str,dict))->(list,list):
        """_summary_
        이미지 배열과 라벨 배열 생성하는 함수
        Args:
            path (str): 이미지 경로
            region (dict): 지역 이름

        Returns:
            list: 이미지 배열
            list: 이미지 라벨 배열
        """        
        categories = {
            'bigben': 0,
            'santorini': 1,
            'Matterhorn': 2,
            'Grand_Canyon': 3,
            'the_statue_of_liberty': 4,
            'eiffel_tower': 5,
            'Gold_gate_bridge': 6,
            'Osakajo': 7,
            'pisa_tower': 8,
            'ayasofya_camii': 9,
            'Donggung_Palace_and_Wolji_Pond': 10,
            'Gobi_Desert': 11,
            'Iceland_Aurora': 12,
            'kuta_beach': 13,
            'Machu_Picchu': 14,
            'Niagara_falls': 15,
            'Pyramid': 16,
            'Sydney_Opera_House': 17,
            'Torre_pendente_di_Pisa': 18,
            'Wat_Chedi_Luang': 19
        }
        label = []
        images = []

        img_file = os.listdir(path)
        
        for img in img_file:
            label.append(categories[region])
            image = keras.preprocessing.image.load_img(f'{path}/{img}',target_size=(256,256))
            imageArr = np.array(image)
            images.append(imageArr)
        
        return images,label

    def concat(path,region,X,Y:(str,dict,list,list))->(list, list):
        """_summary_
        'X' 배열과 이미지 데이터 연결, Y배열과 라벨 데이터를 연결하는 함수
        Args:
            path (str): 이미지 경로
            region (dict): 지역 이름
            X (list): X축 배열
            Y (list): Y축 배열

        Returns:
            list: X축 이미지 배열
            list: Y축 라벨 배열
        """        
        NEW_X = np.concatenate((X,np.array(img_processing.img_label(path,region)[0])),axis=0)
        NEW_Y = np.concatenate((Y,np.array(img_processing.img_label(path,region)[1])),axis=0)
        return NEW_X, NEW_Y 

def processing():
    """_summary_
    카테고리의 이미지와 라벨데이터를 가져와서 하나의 큰 데이터 셋으로 결합하는 함수
    Returns:
        list: 이미지
        list: 라벨_
    """
    images = np.empty((0,256,256,3)) # 배열 생성
    labels = np.empty(0) # 배열생성

    for cate in img_processing.categories:
        images,labels = img_processing.concat(cate,cate,images,labels)

    return images,labels

if __name__ == '__main__':  
    images,labels = processing()
    print(images.shape,labels.shape)


