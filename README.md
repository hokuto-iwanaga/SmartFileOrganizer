# Smart File Organizer

Downloadsフォルダが散らかってきたので作った、ファイル自動整理ツールです。ファイルを拡張子ごとに分類して、それぞれのフォルダに移動します。

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

