# import shutil
# from pathlib import Path
#
#
# def copy_assets():
#     src_dir = Path('src/lib/assets')
#     dst_dir = Path('dash_mosaic/assets')
#     dst_dir.mkdir(parents=True, exist_ok=True)
#
#     for file in src_dir.glob('*'):
#         shutil.copy2(file, dst_dir)
#
#
# if __name__ == "__main__":
#     copy_assets()