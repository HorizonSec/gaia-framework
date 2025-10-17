"""
SARIF standardization functions for GAIA Framework.
"""


def create_sarif_report(results, tool_name, version):
    """Create a SARIF-formatted report.
    
    Args:
        results: List of security findings.
        tool_name: Name of the tool generating the report.
        version: Version of the tool.
    
    Returns:
        Dictionary containing SARIF-formatted report.
    """
    sarif_report = {
        "version": "2.1.0",
        "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": tool_name,
                        "version": version
                    }
                },
                "results": results
            }
        ]
    }
    return sarif_report


def add_result_to_sarif(sarif_report, result):
    """Add a result to an existing SARIF report.
    
    Args:
        sarif_report: Existing SARIF report dictionary.
        result: Result to add to the report.
    
    Returns:
        Updated SARIF report.
    """
    if "runs" in sarif_report and len(sarif_report["runs"]) > 0:
        sarif_report["runs"][0]["results"].append(result)
    return sarif_report
