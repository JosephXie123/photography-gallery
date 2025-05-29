import os
import shutil
from pathlib import Path

def create_photographer_structure(base_path):
    """创建摄影师作品集结构"""
    # 基础目录结构
    photographers = {
        'zengwu': {
            'collections': {
                'VOGUE_Collection': [
                    'VOGUE_CHINA', 'NUMERO_CHINA', 'ELLE', 'LOFFICIEL',
                    'BAZZAR', 'COSMO_China', 'MADAME_FIGARO_CHINA'
                ],
                'Lifestyle_Collection': [
                    'MODERN_WEEKLY_CHINA', 'T_MAGAZINE', 'ISERIES',
                    'THE_GOODLIFE', 'WALLPAPER_CHINA', 'EVENING',
                    'FEMINA', 'GQ_CHINA', 'InStyle_China'
                ],
                'Brand_Collection': [
                    'Various_Campaigns', 'CRUSH_COLLECTION', 'ARETE',
                    'AWAY_LEE', 'BLOCCO_5', 'Dazed_China', 'LABORON',
                    'MAYA_LI', 'NEIWAI', 'Nicole_Zhang', 'OVV',
                    'RICOSTRU', 'SHUSHUTONG', 'YIRANTIAN'
                ],
                'Art_Collection': ['zengwu', 'Wonderland_China', 'YOHO_MAGAZINE']  # 个人作品集
            }
        }
        # 可以在这里添加更多摄影师
    }

    # 创建新的目录结构
    for photographer, data in photographers.items():
        photographer_path = Path(base_path) / 'photographers' / photographer
        
        # 创建摄影师目录
        for collection_name, source_folders in data['collections'].items():
            collection_path = photographer_path / collection_name
            collection_path.mkdir(parents=True, exist_ok=True)
            
            # 从源文件夹复制文件
            for source_folder in source_folders:
                source_path = Path(base_path) / source_folder
                if source_path.exists():
                    # 复制文件并重命名
                    files = list(source_path.glob('*.*'))
                    # 只处理包含摄影师名字的文件
                    photographer_files = [f for f in files if photographer in f.name.lower()]
                    
                    for i, file_path in enumerate(photographer_files, 1):
                        if file_path.is_file():
                            new_name = f"{photographer}_{collection_name}_{i:03d}{file_path.suffix}"
                            try:
                                shutil.copy2(
                                    file_path,
                                    collection_path / new_name
                                )
                                print(f"Copied {file_path} to {collection_path / new_name}")
                            except Exception as e:
                                print(f"Error copying {file_path}: {str(e)}")

def main():
    # 获取当前工作目录
    current_dir = os.getcwd()
    works_dir = os.path.join(current_dir, 'images', 'works')
    
    # 确保works目录存在
    if not os.path.exists(works_dir):
        os.makedirs(works_dir)
    
    # 开始重组文件
    create_photographer_structure(works_dir)
    
    print("文件重组完成！")

if __name__ == "__main__":
    main() 