# ML Club MCP Server — Project Scope

## 1. Use case

Build a Model Context Protocol (MCP) server that allows an MCP-compatible AI client to retrieve information about ML Club projects.

## 2. Data access

- Use sample project records stored locally in Python.
- Expose project information through a read-only MCP tool.
- Expose a general club overview through an MCP resource.
- Do not access external APIs, databases, private files or user accounts in this initial version.

## 3. Permitted actions

- List available sample projects.
- Read the club overview.
- Return structured project information to the MCP client.

## 4. Prohibited actions

- Create, update or delete project records.
- Modify files or execute arbitrary commands.
- Access credentials, private member information or external systems.

## 5. Trust boundary

The server is a local development application. Tool inputs are treated as untrusted, and returned data is limited to the sample records explicitly defined for the project.

## 6. Initial testing

- Verify tool and resource discovery in MCP Inspector.
- Test valid and invalid inputs where applicable.
- Confirm that the server does not modify data.
- Add automated unit and integration tests before expanding functionality.

## 7. Future scope

Backend integration, remote deployment and additional capabilities will be considered only after testing and security review.
