# Table Indexes

## TOC
1. Create and populate table
2. [TODO] How an RDBMS retrieves data
3. [TODO] Filter by year
4. [TODO] Group by year

## Server Platform

- Unraid 6.11.5
- Docker 20.10.21
- i7-4770S 4C/8T
- 16GB DDR3
- 500GB Crucial MX500 SSD
- Other hardware exist but are not used in this demonstration

## MySQL RDBMS

The RDBMS used for this demonstration is MySQL 8.1.0. It is running as a Docker container
on top of an Unraid 6.11.5 server. The container instance is running un-constrained. It has
full access to the CPU and memory resources. The MySQL data files reside on the SSD. Only
the MySQL container will be running during the query executions.

The principles and (relative) results will be largely the same when other RDBMS are used. The syntax may
be different, however.

### Why MySQL?

Quickest RDBMS for me to set up and tear down.

## R Markdown

The raw source documents are written in R Markdown using R 4.3.2. R Markdown is similar in
structure and function to a `.ipynb` Python notebook you may be familiar with.

### Why R? Why not Python?

As data engineers, you will have to support a variety of languages/environments/platforms
used by different data-end-users. This is a way to expose you to a language other than Python.

## Disclaimers
1. None of the code presented are production-ready. It is advisable to use error-tolerant practices such as `tryCatch()` and DB transactions when working with DBs.

