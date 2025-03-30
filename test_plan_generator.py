def generate_test_plan(requirements, ui_elements):
    test_plan = []
    for req in requirements:
        if "log in" in req.lower():
            feature = "Authentication"
            test_case1 = {
                "name": "Successful Login",
                "steps": [
                    "Enter valid username and password.",
                    "Click Login button.",
                ],
                "expected": [
                    "Redirect to home page.",
                ],
            }
            test_case2 = {
                "name": "Invalid Login",
                "steps": [
                    "Enter invalid username or password.",
                    "Click Login button.",
                ],
                "expected": [
                    "Display error message.",
                ],
            }
            test_plan.append({"feature": feature, "test_cases": [test_case1, test_case2]})
    return test_plan

def write_markdown(test_plan, output_path):
    with open(output_path, 'w') as f:
        for feature in test_plan:
            f.write(f"## {feature['feature']}\n\n")
            for test_case in feature['test_cases']:
                f.write(f"### {test_case['name']}\n\n")
                f.write("**Steps:**\n\n")
                for step in test_case['steps']:
                    f.write(f"- {step}\n")
                f.write("\n**Expected Result:**\n\n")
                f.write("\n".join(test_case['expected']) + "\n\n")

# Example usage
# Assuming requirements and ui_elements are from previous steps