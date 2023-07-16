# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os

project = 'Notes'
copyright = '2023, Bubesh'
author = 'Bubesh'
release = '1.0'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'myst_parser',
    'sphinx_design',
    'sphinx_tags'
]

templates_path = ['_templates']
exclude_patterns = []

# To remove "View page source" link
html_show_sourcelink = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


############### Theme Configurations
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_use_index = True
html_css_files = [
    'css/custom_style.css',
]
collapse_navigation = False
html_theme_options = {
    'navigation_depth': 5,
}
############################################## Extensions

# Path to extension's source
sys.path.append(os.path.abspath("./_ext"))

################ sphinx_tags
tags_create_tags = True
tags_create_badges = True
# tags_output_dir = "_tags"  # default
tags_overview_title = "All tags"  # default: "Tags overview"
tags_extension = ["rst", "md"]  # default: ["rst"]
tags_intro_text = "Tags in this page:"  # default: "Tags:"
tags_page_title = "All my tags"  # default: "My tags:"
tags_page_header = "Pages with this tag"  # default: "With this tag"
tags_index_head = "Tags in this site"  # default: "Tags"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
