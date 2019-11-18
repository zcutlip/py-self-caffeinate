from setuptools import setup
about = {}
with open("selfcaffeinate/__about__.py") as fp:
    exec(fp.read(), about)

with open("README.md", "r") as fp:
    long_description = fp.read()

setup(name=about["__title__"],
      version=about["__version__"],
      platforms=['darwin'],
      description=about["__summary__"],
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="Zachary Cutlip",
      author_email="uid000@gmail.com",
      url="TBD",
      license="MIT",
      packages=['selfcaffeinate'],
      python_requires='>=2.7',
      install_requires=[],
      package_data={'selfcaffeinate': ['config/*']},
      )
