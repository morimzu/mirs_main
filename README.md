# mirs_main

'''
ssd_model.detect(image, count)
'''
opencvで読み込んだ画像とint型を受け取り，認識した物体のラベルをリストで返す．

'''
camera.get_image()
'''
カメラの画像を取得して，同じファイルのimagesフォルダに .jpg 形式で画像を保存する．

'''
calc.calc_dist(width)
'''
認識したバインディングボックスの横幅のピクセル数を受け取り，予測される机との距離を返す．
