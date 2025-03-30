def parse_requirements(file_path):
    with open(file_path, 'r') as f:
        requirements = [req.strip() for req in f.readlines() if req.strip()]
    return requirements

# Example usage
requirements = parse_requirements('requirements.txt')
print(requirements)