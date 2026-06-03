from pathlib import Path
import shutil

# 【本番用アップデート】パソコンごとの「ダウンロードフォルダ」の場所を自動で取得する
target_dir = Path.home() / "Downloads"

# ※もし、まだDownloadsフォルダで動かすのが怖い場合は、
# 下の行の先頭の「#」を消せば、いつでもテスト環境（test_folder）に戻せます。
# target_dir = Path(__file__).resolve().parent / "test_folder"

FILE_RULES = {
    ".jpg": "images",
    ".png": "images",
    ".pdf": "pdf",
    ".txt": "text",
    ".zip": "zip",
}

print(f"--- ファイルの自動整理を開始します（対象: {target_dir}） ---")

if not target_dir.exists():
    print(f"❌ エラー: 対象フォルダが見つかりません。")
else:
    for file_path in target_dir.iterdir():
        # フォルダは無視し、ファイルのみを対象にする
        if file_path.is_file():
            
            ext = file_path.suffix.lower()
            
            # ルール判定
            if ext in FILE_RULES:
                folder_name = FILE_RULES[ext]
            else:
                folder_name = "others"
                
            new_folder = target_dir / folder_name
            new_folder.mkdir(exist_ok=True)
            
            destination = new_folder / file_path.name
            
            # 同名ファイルの衝突回避
            if destination.exists():
                print(f"⚠️ スキップ: {file_path.name} は既に {folder_name} 内に存在します。")
                continue
            
            # ファイルの移動
            shutil.move(str(file_path), str(destination))
            print(f"✅ {file_path.name} → {folder_name} に移動しました")

print("--- 整理が完了しました！ ---")
