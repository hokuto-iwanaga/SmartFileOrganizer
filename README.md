# Smart File Organizer

散らかったダウンロードフォルダを簡単に整理できるPythonでつくったCLIツールです。実行すると、ファイルを種類ごとにフォルダ分けして管理しやすくします。

## フォルダ構成と整理前と整理後のイメージ

### 整理前(Before)
```text
SmartFileOrganizer/
└─ test_folder/
    ├─ Sample.jpg
    ├─ document.pdf
    ├─ memo.txt
    └─ game.exe
```
### 整理後(after)
```text
SmartFileOrganizer/
└── test_folder/
    ├── images/
    │   └── Sample.jpg
    ├── pdf/
    │   └── document.pdf
    ├── text/
    │   └── memo.txt
    └── exes/
        └── game.exe
```

