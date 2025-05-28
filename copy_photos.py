import os
import shutil
from pathlib import Path

source_dir = "/Users/josephxie/Desktop/Masterpiece/曾无/杂志"
target_base_dir = "/Users/josephxie/Desktop/网页/images/works/zengwu"  # 修改为以摄影师名字开始的路径

# 作品集分类映射
portfolio_mapping = {
    # 时尚杂志作品集
    "VOGUE_Collection": [
        "VOGUE CHINA",
        "NUMÉRO CHINA",
        "ELLE",
        "BAZAAR",
        "MARIE CLAIRE",
        "L'OFFICIEL",
        "MADAME FIGARO CHINA",
        "InStyle China",
        "FEMINA",
    ],
    
    # 生活方式杂志作品集
    "Lifestyle_Collection": [
        "MODERN WEEKLY CHINA",
        "T MAGAZINE",
        "WALLPAPER CHINA",
        "THE GOODLIFE 2014",
        "GQ CHINA",
        "Esquire China",
        "YOHO MAGAZINE JULY 2016",
    ],
    
    # 品牌合作作品集
    "Brand_Collection": [
        "ARETE FALL WINTER 2015",
        "AWAY LEE FALL WINTER 2015",
        "CRUSH COLLECTION FALL WINTER 2016",
        "MAYA LI 春夏 2017",
        "Nicole Zhang 春夏 2015",
        "NEIWAI2018春夏",
        "OVV2018春夏",
        "RICOSTRU",
        "SHUSHUTONG",
        "YIRANTIAN",
        "Various Campaigns",
    ],
    
    # 艺术摄影作品集
    "Art_Collection": [
        "Dazed China",
        "Dazed & Confused Korea",
        "BLOCCO 5",
        "EVENING",
        "LABORON",
        "Wonderland China July 2021",
    ]
}

# 反向映射，用于快速查找作品集
reverse_portfolio_mapping = {}
for portfolio, magazines in portfolio_mapping.items():
    for magazine in magazines:
        reverse_portfolio_mapping[magazine] = portfolio

def sanitize_filename(filename):
    # 移除文件名中的特殊字符
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def get_portfolio_name(magazine_name):
    # 根据杂志名获取对应的作品集名称
    for orig_name in reverse_portfolio_mapping:
        if orig_name in magazine_name:
            return reverse_portfolio_mapping[orig_name]
    return "Other_Collection"

def process_directory(source_path, target_base):
    # 确保目标根目录存在
    os.makedirs(target_base, exist_ok=True)
    
    # 为每个作品集创建目录
    for portfolio in portfolio_mapping.keys():
        os.makedirs(os.path.join(target_base, portfolio), exist_ok=True)
    
    counter = {portfolio: 1 for portfolio in portfolio_mapping.keys()}
    counter["Other_Collection"] = 1

    for root, dirs, files in os.walk(source_path):
        rel_path = os.path.relpath(root, source_path)
        if rel_path == '.':
            continue

        # 确定作品集
        portfolio = None
        for magazine_name in reverse_portfolio_mapping:
            if magazine_name in rel_path:
                portfolio = reverse_portfolio_mapping[magazine_name]
                break
        
        if portfolio is None:
            portfolio = "Other_Collection"

        # 创建目标文件夹结构
        target_folder = os.path.join(target_base, portfolio)
        os.makedirs(target_folder, exist_ok=True)

        # 处理文件
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.jfif')):
                source_file = os.path.join(root, file)
                # 生成新的文件名，包含作品集信息
                new_filename = f"zengwu_{portfolio}_{counter[portfolio]:03d}.jpg"
                target_file = os.path.join(target_folder, new_filename)
                
                try:
                    shutil.copy2(source_file, target_file)
                    print(f"Copied: {source_file} -> {target_file}")
                    counter[portfolio] += 1
                except Exception as e:
                    print(f"Error copying {source_file}: {e}")

if __name__ == "__main__":
    # 清空目标目录
    if os.path.exists(target_base_dir):
        shutil.rmtree(target_base_dir)
    
    # 处理文件
    process_directory(source_dir, target_base_dir) 