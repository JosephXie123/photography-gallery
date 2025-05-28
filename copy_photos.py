import os
import shutil
from pathlib import Path

source_dir = "/Users/josephxie/Desktop/Masterpiece/曾无/杂志"
target_base_dir = "/Users/josephxie/Desktop/网页/images/works"

# 文件夹名称映射（原始名称到目标名称的映射）
folder_mapping = {
    "ARETE FALL WINTER 2015": "ARETE/fall_winter_2015",
    "AWAY LEE FALL WINTER 2015": "AWAY_LEE/fall_winter_2015",
    "BAZZAR": "BAZZAR",
    "BLOCCO 5": "BLOCCO_5",
    "COSMO China": "COSMO_China",
    "CRUSH COLLECTION FALL WINTER 2016": "CRUSH_COLLECTION/fall_winter_2016",
    "Dazed & Confused Korea": "Dazed_China/korea",
    "Dazed China": "Dazed_China",
    "ELLE": "ELLE",
    "EVENING": "EVENING",
    "Esquire China": "Esquire_China",
    "FEMINA": "FEMINA",
    "GQ CHINA": "GQ_CHINA",
    "ISERIES 春夏 2016": "ISERIES/spring_summer_2016",
    "InStyle China": "InStyle_China",
    "LABORON": "LABORON",
    "L'OFFICIEL": "LOFFICIEL",
    "MADAME FIGARO CHINA": "MADAME_FIGARO_CHINA",
    "MARIE CLAIRE": "MARIE_CLAIRE",
    "MAYA LI 春夏 2017": "MAYA_LI/spring_summer_2017",
    "MODERN WEEKLY CHINA": "MODERN_WEEKLY_CHINA",
    "NEIWAI2018春夏": "NEIWAI/spring_summer_2018",
    "NUMÉRO CHINA": "NUMERO_CHINA",
    "Nicole Zhang 春夏 2015": "Nicole_Zhang/spring_summer_2015",
    "OVV2018春夏": "OVV/spring_summer_2018",
    "RICOSTRU": "RICOSTRU",
    "SHUSHUTONG": "SHUSHUTONG",
    "T MAGAZINE": "T_MAGAZINE",
    "THE GOODLIFE 2014": "THE_GOODLIFE/2014",
    "VOGUE CHINA": "VOGUE_CHINA",
    "Various Campaigns": "Various_Campaigns",
    "WALLPAPER CHINA": "WALLPAPER_CHINA",
    "Wonderland China July 2021": "Wonderland_China/july_2021",
    "YIRANTIAN": "YIRANTIAN",
    "YOHO MAGAZINE JULY 2016": "YOHO_MAGAZINE/july_2016"
}

def sanitize_filename(filename):
    # 移除文件名中的特殊字符
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def process_directory(source_path, target_base):
    counter = 1
    for root, dirs, files in os.walk(source_path):
        rel_path = os.path.relpath(root, source_path)
        if rel_path == '.':
            continue

        # 找到对应的目标文件夹
        target_folder = None
        for orig, mapped in folder_mapping.items():
            if orig in rel_path:
                target_folder = mapped
                break

        if target_folder is None:
            continue

        # 创建目标文件夹
        full_target_dir = os.path.join(target_base, target_folder)
        os.makedirs(full_target_dir, exist_ok=True)

        # 处理文件
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.jfif')):
                source_file = os.path.join(root, file)
                # 生成新的文件名
                new_filename = f"zengwu_{target_folder.replace('/', '_')}_{counter:03d}.jpg"
                target_file = os.path.join(full_target_dir, new_filename)
                
                try:
                    shutil.copy2(source_file, target_file)
                    print(f"Copied: {source_file} -> {target_file}")
                    counter += 1
                except Exception as e:
                    print(f"Error copying {source_file}: {e}")

if __name__ == "__main__":
    process_directory(source_dir, target_base_dir) 