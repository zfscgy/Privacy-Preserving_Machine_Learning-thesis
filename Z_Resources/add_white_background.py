import os
from PIL import Image

def add_white_background_to_transparent_images(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith('.png'):
            img_path = os.path.join(input_directory, filename)
            img = Image.open(img_path)

            # Check if the image has an alpha channel (transparency)
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                # Create a white background
                background = Image.new("RGBA", img.size, (255, 255, 255, 255))
                # 处理透明度
                if img.mode == 'P':
                    img = img.convert('RGBA')
                alpha = img.split()[-1]  # 获取alpha通道
                
                # 将原图粘贴到白色背景上，使用原图的alpha通道作为掩码
                background.paste(img, (0, 0), alpha)
                # 去掉alpha通道，转换为RGB模式
                background = background.convert("RGB")
                # 去掉alpha通道，转换为RGB模式
                background = background.convert("RGB")
                background.save(os.path.join(output_directory, filename), 'PNG')
            else:
                # Just copy the image if it doesn't have transparency
                img.save(os.path.join(output_directory, filename), 'PNG')

if __name__ == "__main__":
    input_directory = '.'  # Replace with your input directory
    output_directory = './output_images'  # Replace with your output directory

    add_white_background_to_transparent_images(input_directory, output_directory)