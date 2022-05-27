from pathlib import Path
from textwrap import dedent

def get_redirect_html(new_url):
    return dedent(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="refresh" content="0; url='{new_url}'" />
    </head>
    </html>
    """)

pagefiles = Path(".").glob("**/*.html")
for f in pagefiles:
    new_url=f"https://tfiers.github.io/phd/{f.as_posix()}"
    print(f"Writing redirect to {new_url}")
    f.write_text(get_redirect_html(new_url))

print("All done.")
