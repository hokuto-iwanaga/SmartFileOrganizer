# Smart File Organizer

Downloadsフォルダに散らばったファイルを、拡張子ごとに自動でフォルダー仕分けするPython、CLIファイル自動整理ツールです。

## フォルダ構成と整理イメージ

### 整理前
```text
SmartFileOrganizer/
└─ test_folder/
    ├─ Sample.jpg
    ├─ document.pdf
    ├─ memo.txt
    └─ game.exe

### 整理後
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
