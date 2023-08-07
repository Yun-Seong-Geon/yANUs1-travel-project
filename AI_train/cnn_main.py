# import train_model_v1 as v1
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from tensorflow import keras
import test_model_v1 as tt
# import big_tranformer_model as bt

#모델 훈련



def main():    

    num = int(input('Train Model[0] / Test Model[1] / BIT Modle Train[2]:'))

    if num == 0:
        # v1.train()
        # print('다음 행동을 선택하세요.')
        # main()
        pass

    elif num == 1:
        path = input('파일 경로를 입력하세요.')
        tt.test(path)
        print('다음 행동을 선택하세요.')
        main()
    elif num== 2:
        # bt.train_bit()
        # print('다음 행동을 선택하세요.')
        # main()
        pass
#    elif num==3 :
main()