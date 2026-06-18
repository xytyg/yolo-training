from ultralytics import YOLO

if __name__ == '__main__':
    # model = YOLO('E:/count/runs/detect/train-2/weights/last.pt') 
    model = YOLO('E:/count/src/best26n1280.pt')   
    results = model.train(
        data='src\\dataset\\data.yaml',
        optimizer='auto', # 鑷姩閫夋嫨銆傝嫢璁粌涓嶇ǔ瀹氬彲鎵嬪姩鏀逛负 'AdamW'
        imgsz=1280,
        batch=4,
        nbs=16,
        epochs=100,
        patience=50,
        lr0=0.01,
        lrf=0.05,        # 鏈€缁堝涔犵巼鍊嶆暟锛孨妯″瀷寤鸿杈冩繁鐨勮“鍑?        mosaic=0.5,
        rect=True,
        amp=False,
        verbose=True,
        workers=0,
        device=0,
        # resume=True,
        cos_lr=True,      # 浣欏鸡閫€鐏帶瀛︿範鐜囦笉椋?        mixup=0,
        copy_paste=0
    )
  


    


