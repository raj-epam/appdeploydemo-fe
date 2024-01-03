import json
import sys

def convert_to_junit(json_data):
    junit_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<testsuites>\n'

    for issue in json_data.get('vulnerabilities', []):
        junit_xml += f'<testsuite name="{issue["title"]}" tests="1">\n'
        junit_xml += f'  <testcase name="{issue["title"]}" classname="Security Issues">\n'
        junit_xml += f'    <failure message="{issue["title"]}">{issue["description"]}</failure>\n'
        junit_xml += '  </testcase>\n'
        junit_xml += '</testsuite>\n'

    junit_xml += '</testsuites>'
    return junit_xml

if __name__ == "__main__":
    # Read Snyk JSON report from stdin
    snyk_json = sys.stdin.read()

    # Parse JSON
    try:
        snyk_data = json.loads(snyk_json)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        sys.exit(1)

    # Convert to JUnit XML
    junit_xml_output = convert_to_junit(snyk_data)

    # Print JUnit XML to stdout
    print(junit_xml_output)

