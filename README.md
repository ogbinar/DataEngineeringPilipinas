# dataengineering.ph

Landing page for dataengineering.ph

## Local Setup and Preview

1. **Install Quarto**:

    - macOS:

        ```
        brew install quarto
        ```

    - Linux / WSL (Debian or Ubuntu): download the `linux-amd64.deb` from the [Quarto releases](https://github.com/quarto-dev/quarto-cli/releases), then:

        ```
        sudo apt install ./quarto-<version>-linux-amd64.deb
        ```

    - Windows: run the installer from [quarto.org](https://quarto.org/docs/get-started/).

    Check the install with `quarto check`.

2. **Install R** (required for the .Rmd files under `content/table_index/`):

    - macOS: `brew install r`
    - Linux / WSL (Debian or Ubuntu): `sudo apt install r-base`
    - Windows: run the installer from [CRAN](https://cloud.r-project.org/).

3. **Install R dependencies**:

    ```
    R -e 'install.packages(c("knitr","rmarkdown"), repos="https://cloud.r-project.org")'
    ```

    If you are using the R project under `content/table_index/` with `renv/`, you can also run:

    ```
    R -e 'renv::restore()'
    ```

4. **Run the site locally**:

    ```
    quarto preview
    ```

    The preview server runs at `http://localhost:5548`.

### Preview a single page without R

`quarto preview` renders the whole site, including the .Rmd files, so it needs R. If you only changed one page, you can skip steps 2–3: render just that page into `_site/` and serve the folder:

```
quarto render partners.qmd
python3 -m http.server 8000 -d _site
```

Then open `http://localhost:8000/partners.html`. Links to pages you haven't rendered won't work.

# Contribution Guidelines for Data Engineering Pilipinas Quarto Website

Welcome to the Data Engineering Pilipinas Quarto website project! We're excited to have you contribute to our growing repository of data engineering resources. To ensure a smooth contribution process for everyone, please follow these guidelines.

## Getting Started

1. **Fork the Repository**: Start by forking the main repository to your GitHub account. This creates your own copy of the project where you can make changes.

2. **Clone Your Fork**: Clone your forked repository to your local machine using Git. This allows you to work on the files locally.

    ```
    git clone https://github.com/yourusername/DataEngineeringPilipinas.git
    ```

3. **Set Upstream Remote**: Add the original repository as an upstream remote to your local clone. This helps you to keep your fork up to date.

    ```
    git remote add upstream https://github.com/ogbinar/DataEngineeringPilipinas.git
    ```

## Making Changes

1. **Create a New Branch**: Always work on a new branch for your changes. This keeps your contributions organized and separate from the main branch.

    ```
    git checkout -b feature/your-new-feature-name
    ```

2. **Add Your Content**: Make your changes or additions to the project. If you're adding new content, ensure it's placed in the correct directory and follows the Quarto formatting guidelines.

3. **Commit Your Changes**: After making your changes, commit them to your branch. Use clear and concise commit messages to describe your updates.

    ```
    git add .
    git commit -m "Add a brief description of your changes"
    ```

4. **Keep Your Fork Updated**: Regularly sync your fork's main branch with the upstream repository to keep it up to date. This reduces potential merge conflicts.

    ```
    git fetch upstream
    git checkout main
    git merge upstream/main
    git push origin main
    ```

## Submitting Contributions

1. **Push Your Changes**: Push your changes to your fork on GitHub.

    ```
    git push origin feature/your-new-feature-name
    ```

2. **Create a Pull Request (PR)**: Go to the original Data Engineering Pilipinas repository on GitHub and create a new pull request. Base your PR on your feature branch and target the main branch of the upstream repository.

3. **Describe Your Contribution**: Provide a clear and detailed description of your pull request. Include the purpose of your changes and any other relevant information.

4. **Review and Collaboration**: Once your PR is submitted, the project maintainers will review your contributions. Be open to feedback and ready to make additional changes if requested.

## Guidelines

- **Quality**: Ensure your contributions are of high quality, with no spelling or grammatical errors.
- **Relevance**: Content should be relevant to data engineering and beneficial to the community.
- **Respect**: Respect the structure and formatting of the existing project. Follow Quarto and Markdown formatting standards.

Thank you for contributing to the Data Engineering Pilipinas Quarto website. Your efforts help make our community a richer and more informative space for data engineering professionals in the Philippines and beyond!