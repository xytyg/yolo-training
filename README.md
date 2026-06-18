# YOLO训练项目

这是一个基于YOLO的目标检测训练项目，包含Python训练脚本和C++ RTSP录视频程序。

## 项目结构

```
├── train.py              # YOLO训练脚本
├── test.py               # 测试脚本
├── CMakeLists.txt        # C++项目配置
├── src/
│   ├── dataset/          # 训练数据集
│   ├── best26n1280.pt    # 最佳模型权重
│   ├── yolo11s.pt        # YOLO11s模型
│   ├── yolo26n.pt        # YOLO26n模型
│   └── yolo26s.pt        # YOLO26s模型
├── runs/                 # 训练结果
└── bin/                  # 编译输出
```

## 功能特性

### Python训练脚本
- 基于ultralytics的YOLO训练
- 支持多种模型架构（YOLO11s, YOLO26n, YOLO26s）
- 可配置训练参数（epochs, batch size, learning rate等）

### C++ RTSP录视频程序
- 使用OpenCV实现RTSP流录制
- 支持FFmpeg解码
- 自动复制运行时DLL依赖

## 使用方法

### Python训练
```bash
python train.py
```

### C++编译
```bash
mkdir build && cd build
cmake ..
cmake --build .
```

## 依赖

- Python 3.x
- ultralytics (YOLO)
- OpenCV 4.x (C++部分)
- CMake 3.16+

## 训练配置

训练参数在`train.py`中配置，主要参数：
- `imgsz`: 输入图像尺寸 (1280)
- `batch`: 批次大小 (4)
- `epochs`: 训练轮数 (100)
- `patience`: 早停耐心值 (50)
- `lr0`: 初始学习率 (0.01)

## 数据集

数据集位于`src/dataset/`目录，配置文件为`data.yaml`。

## 许可证

MIT License