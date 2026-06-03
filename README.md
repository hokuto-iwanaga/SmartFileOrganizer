# Smart File Organizer

散らかったダウンロードフォルダを簡単に整理できるPythonでつくったCLIツールです。実行すると、ファイルを種類ごとにフォルダ分けして管理しやすくします。

## フォルダ構成と整理前と整理後のイメージ

### Before
```text
SmartFileOrganizer/
└─ test_folder/
    ├─ Sample.jpg
    ├─ document.pdf
    ├─ memo.txt
    └─ game.exe
```
### after
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

