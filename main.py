from requirements_parser import parse_requirements
from figma_design_extractor import get_figma_data, extract_ui_elements
from test_plan_generator import generate_test_plan, write_markdown

def main():
    requirements_path = 'requirements.txt'
    requirements = parse_requirements(requirements_path)
    file_key = 'your_file_key'
    api_token = 'your_api_token'
    figma_data = get_figma_data(file_key, api_token)
    ui_elements = extract_ui_elements(figma_data)
    test_plan = generate_test_plan(requirements, ui_elements)
    write_markdown(test_plan, "test_plan.md")

if __name__ == "__main__":
    main()