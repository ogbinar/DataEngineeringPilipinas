## Containerization

This module is for anyone to try out their hands in containerized workloads.

`Docker` is the most popular solution to use this, there are a few more OSS that does this like `podman`.

For the sake of clarity and consistency we will be using `Docker` as the springboard to get you familiarized with
containerization.

### Pre-Requisites

Containerization is actually treated like a black-box, read more in 
[Docker's Website](https://docs.docker.com/guides/get-started/) as it already has a curated
way content of on-boarding anyone.

The focus of this module is to just get you started after you install it yourself. There's already
a wealth of questions and answers in stackoverflow with respect to installation so please bear in mind that
the assumption here is you have at least past the hurdle of installing it yourself and you have done the pre-read.

Important!! Make sure you install LINUX based containers!

### But what if I really need help from the group?

Please post a message in [#coding-practice](https://discord.com/channels/1158210069440237649/1182489266081771641) and 
the group will try to help you out.

## Hit Me! How do we use `Docker`?

Before we start, if you've been installing services into your development machine for most of your life, `Docker` will 
change how you set up your development machines.

`Docker` spins up a container with a single service, the container is a minified version of the service as installed in
a Linux machine. If you've never dabbled in Linux, it's perfectly fine! The container runs on its own like a mini-VM,
you can easily destroy it and its contents. `Installing` in the old world is equivalent to `spinning-up` a container.
`Uninstalling` in the old world is equivalent to `destroying` the container.

We only normally want a container to have persistent data for our workloads. In this case, the examples we have here
will have a persistent storage mounted on the root folder of your machines in the `c:\tmp` or `/tmp` for linux users.

### Running the containers

#### Postgres

Take note that for containers in your machine to talk to each other, refer to `localhost` as `host.docker.internal` so
it can relay the traffic through your host machine and reach the other container.

Make sure you are in the `containerization` directory before you run this command.

##### Windows

```shell
c:\Projects\DataEngineeringPilipinas\containerization> docker-compose -f postgres/docker-compose up -d
```

##### Linux

```shell
/home/your_user/projects/DataEngineeringPilipinas/containerization % docker-compose -f postgres/docker-compose up -d
```

Alternatively, you can use the `Makefile` if you have `GNU Make` in your machine (both available in Windows and Linux).

```shell
make run-postgres
```

Shutting down is simply running either commands:

```shell
docker-compose -f postgres/docker-compose down
```

or

```shell
make stop-postgres
```