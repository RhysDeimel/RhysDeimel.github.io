<br />
<div align="center">
    <img src="content/extra/table_flip.png" alt="Logo">
</div>
<br />


# rhysdeimel.github.io
The personal blog of Rhys Deimel - a tech enthusiast, programmer, cloud magician,
and maker with a strong interest in data science, electronics, and a passion for automating the boring parts of life.

## Getting started
This is a [MkDocs](https://www.mkdocs.org/) site using [Material for MKDocs](https://squidfunk.github.io/mkdocs-material/)
dressed up as a blog. I wanted something simple, and low touch, because I'd much rather be doing better things with my 
life than maintaining a temperamental website.

### Overview
- Site-wide config can be found in `mkdocs.yml`
- Posts are written as Markdown files in `docs/recipes`.
  These require front matter to be rendered correctly.
  See existing posts for examples.
- Site template overrides are located in `overrides`


### Installing the project
```bash
virtualenv -p python3.11 venv
source venv/bin/activate
pip install -r requirements.txt
```

### Running the project
```
mkdocs serve
```

### Testing the project
```bash
pyspelling --config .pyspelling.yml
```

## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repository and create a pull request. You can also simply open an issue with the tag "enhancement". Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## TODO
- Giscus integration: https://squidfunk.github.io/mkdocs-material/tutorials/blogs/engage/?h=rss#giscus-integration