def print_cve(cve: dict):
    return """
Published on {}.

**Description:**
*{}*

> CVSS Score: {}
> Severity: {}
> Vector String: {}
""".format(cve['published'], cve['description'], cve['cvss_score'], cve['cvss_severity'], cve['cvss_vectorString'])