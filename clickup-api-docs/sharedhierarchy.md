# Shared Hierarchy

View the tasks, Lists, and Folders that have been shared with the authenticated user.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/team/{team_id}/shared": {
      "get": {
        "summary": "Shared Hierarchy",
        "tags": [
          "Shared Hierarchy"
        ],
        "description": "View the tasks, Lists, and Folders that have been shared with the authenticated user.",
        "operationId": "SharedHierarchy",
        "parameters": [
          {
            "name": "team_id",
            "in": "path",
            "description": "Workspace ID",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "SharedHierarchyresponse",
                  "required": [
                    "shared"
                  ],
                  "type": "object",
                  "properties": {
                    "shared": {
                      "title": "Shared7",
                      "required": [
                        "tasks",
                        "lists",
                        "folders"
                      ],
                      "type": "object",
                      "properties": {
                        "tasks": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "description": ""
                        },
                        "lists": {
                          "type": "array",
                          "items": {
                            "title": "List6",
                            "required": [
                              "id",
                              "name",
                              "orderindex",
                              "content",
                              "status",
                              "priority",
                              "assignee",
                              "task_count",
                              "due_date",
                              "start_date",
                              "archived"
                            ],
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string"
                              },
                              "name": {
                                "type": "string"
                              },
                              "orderindex": {
                                "type": "integer",
                                "contentEncoding": "int32"
                              },
                              "content": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              "status": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              "priority": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              "assignee": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              "task_count": {
                                "type": "string"
                              },
                              "due_date": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              "start_date": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              "archived": {
                                "type": "boolean"
                              }
                            },
                            "examples": [
                              {
                                "id": "1421",
                                "name": "Shared List",
                                "orderindex": 0,
                                "content": null,
                                "status": null,
                                "priority": null,
                                "assignee": null,
                                "task_count": "0",
                                "due_date": null,
                                "start_date": null,
                                "archived": false
                              }
                            ]
                          },
                          "description": ""
                        },
                        "folders": {
                          "type": "array",
                          "items": {
                            "title": "Folder11",
                            "required": [
                              "id",
                              "name",
                              "orderindex",
                              "content",
                              "task_count",
                              "due_date",
                              "archived"
                            ],
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string"
                              },
                              "name": {
                                "type": "string"
                              },
                              "orderindex": {
                                "type": "integer",
                                "contentEncoding": "int32"
                              },
                              "content": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              "task_count": {
                                "type": "string"
                              },
                              "due_date": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              "archived": {
                                "type": "boolean"
                              }
                            },
                            "examples": [
                              {
                                "id": "1058",
                                "name": "Shared Folder",
                                "orderindex": 0,
                                "content": null,
                                "task_count": "0",
                                "due_date": null,
                                "archived": false
                              }
                            ]
                          },
                          "description": ""
                        }
                      },
                      "examples": [
                        {
                          "tasks": [],
                          "lists": [
                            {
                              "id": "1421",
                              "name": "Shared List",
                              "orderindex": 0,
                              "content": null,
                              "status": null,
                              "priority": null,
                              "assignee": null,
                              "task_count": "0",
                              "due_date": null,
                              "start_date": null,
                              "archived": false
                            }
                          ],
                          "folders": [
                            {
                              "id": "1058",
                              "name": "Shared Folder",
                              "orderindex": 0,
                              "content": null,
                              "task_count": "0",
                              "due_date": null,
                              "archived": false
                            }
                          ]
                        }
                      ]
                    }
                  },
                  "examples": [
                    {
                      "shared": {
                        "tasks": [],
                        "lists": [
                          {
                            "id": "1421",
                            "name": "Shared List",
                            "orderindex": 0,
                            "content": null,
                            "status": null,
                            "priority": null,
                            "assignee": null,
                            "task_count": "0",
                            "due_date": null,
                            "start_date": null,
                            "archived": false
                          }
                        ],
                        "folders": [
                          {
                            "id": "1058",
                            "name": "Shared Folder",
                            "orderindex": 0,
                            "content": null,
                            "task_count": "0",
                            "due_date": null,
                            "archived": false
                          }
                        ]
                      }
                    }
                  ]
                },
                "example": {
                  "shared": {
                    "tasks": [],
                    "lists": [
                      {
                        "id": "1421",
                        "name": "Shared List",
                        "orderindex": 0,
                        "content": null,
                        "status": null,
                        "priority": null,
                        "assignee": null,
                        "task_count": "0",
                        "due_date": null,
                        "start_date": null,
                        "archived": false
                      }
                    ],
                    "folders": [
                      {
                        "id": "1058",
                        "name": "Shared Folder",
                        "orderindex": 0,
                        "content": null,
                        "task_count": "0",
                        "due_date": null,
                        "archived": false
                      }
                    ]
                  }
                }
              }
            }
          }
        },
        "deprecated": false
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Shared Hierarchy"
    }
  ]
}
```