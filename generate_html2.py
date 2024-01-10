# scripts/generate_html.py
import os
import yaml

def read_artwork_data(data_dir):
    """
    Read artwork data from YAML files in the specified directory.

    Args:
        data_dir (str): The directory containing artwork YAML files.

    Returns:
        list: A list of dictionaries, each containing artwork information.
    """
    artworks = []

    # Iterate through YAML files in the data directory
    for filename in os.listdir(data_dir):
        if filename.endswith(".yml") or filename.endswith(".yaml"):
            file_path = os.path.join(data_dir, filename)
            print(f"Reading data from {file_path}")

            with open(file_path, 'r') as file:
                artworks.append(yaml.safe_load(file))

    return artworks

def generate_artwork_html(artwork):
    """
    Generate HTML code for a single artwork.

    Args:
        artwork (dict): Dictionary containing artwork information.

    Returns:
        str: HTML code for the artwork.
    """
    print(f"Generating HTML for {artwork['name']}")

    # Check if there is at least one image
    images = artwork.get('img', [])
    if not images:
        return ""  # Skip artwork without images

    # Get the first image filename
    main_image = images[0]

    # HTML code for the masonry grid item
    artwork_html = f"""
    <div class="grid-item">
        <img class="img-responsive" alt="{artwork['name']}" src="img/{main_image}">
        <a href="./artwork-pages/{artwork['name']}.html" class="project-description">
            <div class="project-text-holder">
                <div class="project-text-inner">
                    <h3>{artwork['name']}</h3>
                    <p>Ver más</p>
                </div>
            </div>
        </a>
    </div>
    """

    return artwork_html

def generate_html(artwork_data):
    """
    Generate the complete HTML code for the gallery page.

    Args:
        artwork_data (list): List of dictionaries, each containing artwork information.

    Returns:
        str: Complete HTML code for the gallery page.
    """
    print("Artwork data received:")
    for i, artwork in enumerate(artwork_data):
        print(f"{i + 1}. {artwork['name']}")

    artworks_html = ""
    for artwork in artwork_data:
        artwork_html = generate_artwork_html(artwork)
        if artwork_html:
            artworks_html += artwork_html

    # Updated HTML structure for the complete page
    html_content = """
    <!DOCTYPE html>
    <html lang="es">

    <head>
        <!-- Meta tags for character set and viewport -->
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta content="Page description" name="description">
        <meta content="Developed by ININ" name="author">

        <link href="./assets/apple-icon-180x180.png" rel="apple-touch-icon">
        <link href="./assets/favicon.ico" rel="icon">

        <title>Clínica Dental de la Doctora Quadros</title>

        <!-- Link to the external CSS files -->
        <link rel="stylesheet" href="styles/main.82cfd66e.css">
        <link rel="stylesheet" href="styles/gallery.css">
    </head>

    <body>

    <!-- Add your content of header -->
    <header class="">
        <div class="navbar navbar-default visible-xs">
            <button type="button" class="navbar-toggle collapsed">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a href="./index.html" class="navbar-brand">Clínica Dental de la Doctora Quadros</a>
        </div>

        <nav class="sidebar">
            <div class="navbar-collapse" id="navbar-collapse">
                <div class="site-header hidden-xs">
                    <a class="site-brand" href="./index.html" title="">
                        <img class="img-responsive site-logo" alt="" src="./assets/images/mashup-logo.svg">
                        Clínica Dental de la Doctora Quadros
                    </a>
                    <p>Venta de equipos</p>
                </div>
                <ul class="nav">
                    <li><a href="./index.html" title="">Portada</a></li>
                    <li><a href="./about.html" title="">Acerca de</a></li>
                    <li><a href="./contact.html" title="">Contacto</a></li>

                </ul>

                <nav class="nav-footer">
                    <p class="nav-footer-social-buttons">
                        <a class="fa-icon" href="https://www.instagram.com/" title="">
                            <i class="fa fa-instagram"></i>
                        </a>
                        <a class="fa-icon" href="https://dribbble.com/" title="">
                            <i class="fa fa-dribbble"></i>
                        </a>
                        <a class="fa-icon" href="https://twitter.com/" title="">
                            <i class="fa fa-twitter"></i>
                        </a>
                    </p>
                    <p>© 2024 ININ | Clínica Dental de la Doctora Quadros</p>
                </nav>
            </div>
        </nav>
    </header>

    <main class="" id="main-collapse">

        <!-- Masonry grid for artworks -->
        <div class="hero-full-wrapper">
            <div class="grid">
                <div class="gutter-sizer"></div>
                <div class="grid-sizer"></div>

                {}
            </div>
        </div>

        <script>
            document.addEventListener("DOMContentLoaded", function (event) {{
                masonryBuild();
            }});
        </script>

    </main>

    <script>
        document.addEventListener("DOMContentLoaded", function (event) {{
            navbarToggleSidebar();
            navActivePage();
        }});
    </script>

    <!-- Google Analytics: change UA-XXXXX-X to be your site's ID

    <script>
      (function (i, s, o, g, r, a, m) {{
        i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {{
          (i[r].q = i[r].q || []).push(arguments)
        }}, i[r].l = 1 * new Date(); a = s.createElement(o),
          m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
      }})(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');
      ga('create', 'UA-XXXXX-X', 'auto');
      ga('send', 'pageview');
    </script>

    --><script type="text/javascript" src="./main.85741bff.js"></script>

    </body>

    </html>
    """.format(artworks_html)

    return html_content

def write_html_to_file(html_content, output_file="index.html"):
    """
    Write HTML content to a file.

    Args:
        html_content (str): HTML code to be written to the file.
        output_file (str): Name of the output HTML file. Default is "index.html".
    """
    with open(output_file, 'w') as index_file:
        index_file.write(html_content)

def main():
    print("Main function started")  # Add this line for debugging

    # Directory containing artwork data
    data_dir = "data"

    print(f"Reading artwork data from {data_dir}")  # Add this line for debugging

    # Read artwork data from YAML files
    artwork_data = read_artwork_data(data_dir)

    # Generate HTML content
    html_content = generate_html(artwork_data)

    # Write HTML content to index.html
    write_html_to_file(html_content)

if __name__ == "__main__":
    main()
