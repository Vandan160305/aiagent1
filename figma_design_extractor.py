import requests

def get_figma_data(file_key, api_token):
    url = f"https://api.figma.com/v1/files/{file_key}"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch Figma data: {response.text}")

def extract_ui_elements(figma_data):
    # Simplified extraction: find all rectangles with text children
    nodes = figma_data['document']['children'][0]['children']  # Assuming first page
    ui_elements = []
    for node in nodes:
        if node['type'] == 'RECTANGLE':
            for child in node.get('children', []):
                if child['type'] == 'TEXT':
                    text = child['characters']
                    ui_elements.append({"type": "button", "text": text})
        elif node['type'] == 'TEXT':
            ui_elements.append({"type": "label", "text": node['characters']})
    return ui_elements

# Example usage
file_key = 'your_file_key'
api_token = 'your_api_token'
figma_data = get_figma_data(file_key, api_token)
ui_elements = extract_ui_elements(figma_data)
print(ui_elements)