from pdf2image import convert_from_path
import os
import requests
import time
start_time = time.time()
pdf_url = 'https://www.saudiexchange.sa/Resources/fsPdf/1541_0_2025-03-04_09-24-08_En.pdf'
output_folder = 'output'
local_pdf_path = os.path.join(output_folder, 'downloaded.pdf')

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Download the PDF if not already present
if not os.path.exists(local_pdf_path):
    response = requests.get(pdf_url, stream=True)
    response.raise_for_status()
    with open(local_pdf_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)


# Specify the file path and the page range
images = convert_from_path(local_pdf_path, first_page=1, last_page=83)
# Save images to a folder
for i, img in enumerate(images):
    img.save(f'output/downloaded/page_{i+1}.jpg', 'JPEG')

print(f'{len(images)} pages converted')


from pytesseract import image_to_string
full_text = []
for i, img in enumerate(images):
    text = image_to_string(img)
    # print(f'Page {i+1}: {text}')
    full_text.append(text)

with open('output/downloaded/full_text.txt', 'w') as f:
    f.write('\n'.join(full_text))

print(f'Full text saved to output/downloaded/full_text.txt')
print(f'Time taken: {time.time() - start_time} seconds')



