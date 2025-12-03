import os
import re
import base64

def extract_images(html_path, output_dir):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find base64 images
    # Pattern looks for <img src="data:image/png;base64,..."
    # We capture the base64 string
    pattern = re.compile(r'src="data:image/png;base64,([^"]+)"')
    
    matches = pattern.findall(content)
    
    print(f"Found {len(matches)} images.")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for i, data in enumerate(matches):
        try:
            image_data = base64.b64decode(data)
            filename = f"image_{i+1:03d}.png"
            output_path = os.path.join(output_dir, filename)
            
            with open(output_path, 'wb') as f_out:
                f_out.write(image_data)
            print(f"Saved {filename}")
        except Exception as e:
            print(f"Error saving image {i+1}: {e}")

if __name__ == "__main__":
    html_file = "/Users/wendydu/.gemini/antigravity/scratch/sleep_analysis_presentation/workbook.html"
    assets_dir = "/Users/wendydu/.gemini/antigravity/scratch/sleep_analysis_presentation/assets"
    extract_images(html_file, assets_dir)
