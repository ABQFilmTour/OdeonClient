# OdeonClient
This repository is for a planned client to assist privilieged users of the [ABQ Film Tour](https://abqfilmtour.github.io/) application in modifying the serverside database from their PC.

Currently, a script retrieves a token that a privilieged user can add to the header for requests. The Python scripts implemented so far assist the user in viewing the database, approving, and deleting submitted content. I plan to expand on these features and create a GUI so trusted users can interact with the database without needing technical experience.

In its current state it requires a client secret JSON file that can be retrieved from the GoogleAPIs console for the project if the user has access.
