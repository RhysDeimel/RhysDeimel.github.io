<br />
<div align="center">
    <img src="content/extra/table_flip.png" alt="Logo">
</div>
<br />


# rhysdeimel.github.io
The personal blog of Rhys Deimel - a tech enthusiast, programmer, cloud magician, and maker with a strong interest in data science, electronics, and a passion for automating the boring parts of life


## Getting Started
This blog uses [Pelican](https://getpelican.com/) to convert Markdown files into something that vaguely resembles a blog. HTML templates and CSS are located in the `theme` directory, while all blog posts, images, and miscellany are located in `content`


### Prerequisites
* \>=python3.10
* \>=sass 1.55.0 


### Installation
1. Clone the repository
   ```sh
   git clone https://github.com/RhysDeimel/RhysDeimel.github.io.git
   ```
2. Install dependencies - preferably in a virtualenv
   ```sh
   pip install -r requirements.txt
   ```
3. Get developing!


## Usage
This website uses an exceptionally jank Sass file to overkill manage the small amount of CSS in this website. If you want to update or adjust it, you'll need to regenerate
the CSS to see any changes. With the Sass binary installed and present on your path, just run the following in the project root to automatically rebuild on a change:
```sh
sass --watch theme/static/css/style.scss theme/static/css/style.css
```


For the actual website generation, Pelican will take care of that. To automatically generate, and serve the site, run the following in the project root directory:
```sh
pelican -rl
```
and then preview the site by navigating to [http://localhost:8000/](http://localhost:8000/) in your browser.


## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repository and create a pull request. You can also simply open an issue with the tag "enhancement". Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
