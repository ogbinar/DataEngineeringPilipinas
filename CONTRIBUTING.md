## Abstract

The idea of contributing is a great process for any OSS project. However, a structure is always required.
It eases the burden on the curator of the content who originally owns the repository.
In order to introduce structure, this document lists down the `Rules` on contributing in a fun and organized way.

### Rules

Here are the basic rules for contributing, this list is meant to be met for each Pull Request.

For the benefit of those that use the repository, adhering to this maintains the availability and safety of everyone's
contribution.

| No. | Rule                                         | Description                                                                                                                                                  | Example                                                                         |
|-----|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| 1   | Directory Naming                             | Directories are to use `lowercase` characters and words are separated by `hyphens (-)`.                                                                      | `this-is-a-directory`                                                           |
| 2   | File Naming                                  | Files are to use `lowercase` characters and words can be separated by any character                                                                          | `this-is-a-file.md`, `this_is_also_a_file.txt`, `this.is.also.another.file.csv` |
| 3   | End of Line                                  | `git` normally stores everything in `line feed (LF)` as the new line separator, this is not strongly enforced and is more recommended over a must.           | N/A                                                                             |
| 4   | No PII (Personal Identifiable Information)   | In no circumstance must any PII exist in the repository, this is to avoid being linked to data leaks that are of a criminal activity                         | N/A                                                                             |
| 5   | `README.md` is your TLDR;                    | Every relevant content must have a `README.md`, this allows your reader to know what to expect, and for the contributor to set the tone.                     | N/A                                                                             |
| 6   | No audios, videos and high resolution images | Binary data format is discouraged, it blows out the storage of the repository, and it may incur costs.                                                       | N/A                                                                             |
| 7   | `LICENSE.md` for shared code                 | For any code shared here, it most often means that it can be copy pasta'd anywhere. Apache and MIT licenses may be used to protect the code you are sharing. | N/A                                                                             |

### Directory Structure

The repository structure will be organized initially like below.

| Directory      | Purpose                                                                                                |
|----------------|--------------------------------------------------------------------------------------------------------|
| assets         | This directory should contain images for the purpose of visualization and `markdown` assets            |
| coding         | This directory should contain sub-directories for a specific programming, scripting, or query language |
| infrastructure | This directory should contain sub-directories for specific infrastructure purposes                     |
| references     | This directory should contain the references that are curated links to external references             |

```text
+--- assets
|    +--- data-camp
|    |    +--- data-camp-1.png
|    |    \--- data-camp-2.png
|    +--- data-sets
|    \--- README.md
+--- coding
|    +--- python
|    |    +--- project-samples
|    |    +--- script-samples
|    |    \--- README.md
|    +--- sql
|    |    +--- sql-server
|    |    +--- postgres
|    |    +--- mysql
|    |    \--- README.md
+--- infrastructure
|    +--- containerization
|    |    +--- postgres
|    |    |    \--- README.md
|    |    \--- README.md
|    +--- aws
|    |    +--- terraform
|    |    \--- README.md
+--- references
|    +--- reference-1
|    |    +--- FREE_RESOUCES.md
|    |    \--- README.md
|    \--- README.md
```