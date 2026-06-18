# YOLO璁粌椤圭洰

杩欐槸涓€涓熀浜嶻OLO鐨勭洰鏍囨娴嬭缁冮」鐩紝鍖呭惈Python璁粌鑴氭湰鍜孋++ RTSP褰曡棰戠▼搴忋€?
## 椤圭洰缁撴瀯

```
鈹溾攢鈹€ train.py              # YOLO璁粌鑴氭湰
鈹溾攢鈹€ test.py               # 娴嬭瘯鑴氭湰
鈹溾攢鈹€ CMakeLists.txt        # C++椤圭洰閰嶇疆
鈹溾攢鈹€ src/
鈹?  鈹溾攢鈹€ dataset/          # 璁粌鏁版嵁闆?鈹?  鈹溾攢鈹€ best26n1280.pt    # 鏈€浣虫ā鍨嬫潈閲?鈹?  鈹溾攢鈹€ yolo11s.pt        # YOLO11s妯″瀷
鈹?  鈹溾攢鈹€ yolo26n.pt        # YOLO26n妯″瀷
鈹?  鈹斺攢鈹€ yolo26s.pt        # YOLO26s妯″瀷
鈹溾攢鈹€ runs/                 # 璁粌缁撴灉
鈹斺攢鈹€ bin/                  # 缂栬瘧杈撳嚭
```

## 鍔熻兘鐗规€?
### Python璁粌鑴氭湰
- 鍩轰簬ultralytics鐨刌OLO璁粌
- 鏀寔澶氱妯″瀷鏋舵瀯锛圷OLO11s, YOLO26n, YOLO26s锛?- 鍙厤缃缁冨弬鏁帮紙epochs, batch size, learning rate绛夛級

### C++ RTSP褰曡棰戠▼搴?- 浣跨敤OpenCV瀹炵幇RTSP娴佸綍鍒?- 鏀寔FFmpeg瑙ｇ爜
- 鑷姩澶嶅埗杩愯鏃禗LL渚濊禆

## 浣跨敤鏂规硶

### Python璁粌
```bash
python train.py
```

### C++缂栬瘧
```bash
mkdir build && cd build
cmake ..
cmake --build .
```

## 渚濊禆

- Python 3.x
- ultralytics (YOLO)
- OpenCV 4.x (C++閮ㄥ垎)
- CMake 3.16+

## 璁粌閰嶇疆

璁粌鍙傛暟鍦╜train.py`涓厤缃紝涓昏鍙傛暟锛?- `imgsz`: 杈撳叆鍥惧儚灏哄 (1280)
- `batch`: 鎵规澶у皬 (4)
- `epochs`: 璁粌杞暟 (100)
- `patience`: 鏃╁仠鑰愬績鍊?(50)
- `lr0`: 鍒濆瀛︿範鐜?(0.01)

## 鏁版嵁闆?
鏁版嵁闆嗕綅浜巂src/dataset/`鐩綍锛岄厤缃枃浠朵负`data.yaml`銆?
## 璁稿彲璇?
MIT License