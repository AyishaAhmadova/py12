import os
import shutil

# 1. 
example_dir = 'Example'
if not os.path.exists(example_dir):
    os.makedirs(example_dir)

# 2. 
sub_dir = os.path.join(example_dir, 'subdirect')
if not os.path.exists(sub_dir):
    os.makedirs(sub_dir)


image_file = 'image.jpg'  
text_file = 'example.txt'  


current_dir = os.getcwd()


image_path = os.path.join(current_dir, image_file)
text_path = os.path.join(current_dir, text_file)

# 3.
if os.path.exists(image_path):
    shutil.move(image_path, os.path.join(sub_dir, image_file))
else:
    print(f"sekil fayli tapilamdi: {image_path}")

if os.path.exists(text_path):
    shutil.move(text_path, os.path.join(sub_dir, text_file))
else:
    print(f"Metin fayli tapilmadi: {text_path}")

# 4. ı
for file_name in os.listdir(sub_dir):
    if file_name.endswith('.txt'):
        shutil.move(os.path.join(sub_dir, file_name), os.path.join(example_dir, file_name))

print("Emeliyyat tamamlandı!")
