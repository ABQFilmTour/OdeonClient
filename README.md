# OdeonClient
This repository is for a planned client to assist privilieged users of the [ABQ Film Tour](https://abqfilmtour.github.io/) application in modifying the serverside database from their PC.

Currently, it only retrieves a token that a privilieged user can add to the header for requests. In the future I plan on giving it the capability to more easily make higher permission requests, and possibly even make a GUI so even less technical trusted users can interact with the database (for example, to approve, delete, or modify user submitted content).

In its current state it requires a client secret JSON file that can be retrieved from the GoogleAPIs console for the project if the user has access.
