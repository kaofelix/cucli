# Get Folderless Lists

View the Lists in a Space that aren't located in a Folder.

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
    "/v2/space/{space_id}/list": {
      "get": {
        "summary": "Get Folderless Lists",
        "tags": [
          "Lists"
        ],
        "description": "View the Lists in a Space that aren't located in a Folder.",
        "operationId": "GetFolderlessLists",
        "parameters": [
          {
            "name": "space_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                789
              ]
            }
          },
          {
            "name": "archived",
            "in": "query",
            "description": "",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "examples": [
                false
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
                  "title": "GetFolderlessListsresponse",
                  "required": [
                    "lists"
                  ],
                  "type": "object",
                  "properties": {
                    "lists": {
                      "type": "array",
                      "items": {
                        "title": "List4",
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
                          "folder",
                          "space",
                          "archived",
                          "override_statuses",
                          "permission_level"
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
                            "type": "string"
                          },
                          "status": {
                            "oneOf": [
                              {
                                "title": "Status11",
                                "type": "object",
                                "properties": {
                                  "status": {
                                    "type": "string"
                                  },
                                  "color": {
                                    "type": "string"
                                  },
                                  "hide_label": {
                                    "type": "boolean"
                                  }
                                },
                                "examples": [
                                  {
                                    "status": "red",
                                    "color": "#e50000",
                                    "hide_label": true
                                  }
                                ]
                              },
                              {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              {}
                            ],
                            "examples": [
                              {
                                "status": "red",
                                "color": "#e50000",
                                "hide_label": true
                              }
                            ]
                          },
                          "priority": {
                            "oneOf": [
                              {
                                "title": "Priority4",
                                "type": "object",
                                "properties": {
                                  "priority": {
                                    "type": "string"
                                  },
                                  "color": {
                                    "type": "string"
                                  }
                                },
                                "examples": [
                                  {
                                    "priority": "high",
                                    "color": "#f50000"
                                  }
                                ]
                              },
                              {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              {}
                            ],
                            "examples": [
                              {
                                "priority": "high",
                                "color": "#f50000"
                              }
                            ]
                          },
                          "assignee": {
                            "type": [
                              "string",
                              "null"
                            ]
                          },
                          "task_count": {
                            "type": [
                              "string",
                              "null"
                            ]
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
                          "folder": {
                            "title": "Folder3",
                            "required": [
                              "id",
                              "name",
                              "hidden",
                              "access"
                            ],
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string"
                              },
                              "name": {
                                "type": "string"
                              },
                              "hidden": {
                                "type": "boolean"
                              },
                              "access": {
                                "type": "boolean"
                              }
                            },
                            "examples": [
                              {
                                "id": "1217",
                                "name": "Shared with me",
                                "hidden": false,
                                "access": false
                              }
                            ]
                          },
                          "space": {
                            "title": "Space2",
                            "required": [
                              "id",
                              "name",
                              "access"
                            ],
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string"
                              },
                              "name": {
                                "type": "string"
                              },
                              "access": {
                                "type": "boolean"
                              }
                            },
                            "examples": [
                              {
                                "id": "789",
                                "name": "Space Name",
                                "access": true
                              }
                            ]
                          },
                          "archived": {
                            "type": "boolean"
                          },
                          "override_statuses": {
                            "type": "boolean"
                          },
                          "permission_level": {
                            "type": "string"
                          }
                        },
                        "examples": [
                          {
                            "id": "124",
                            "name": "Updated List Name",
                            "orderindex": 1,
                            "content": "Updated List Content",
                            "status": {
                              "status": "red",
                              "color": "#e50000",
                              "hide_label": true
                            },
                            "priority": {
                              "priority": "high",
                              "color": "#f50000"
                            },
                            "assignee": null,
                            "task_count": null,
                            "due_date": "1567780450202",
                            "start_date": null,
                            "folder": {
                              "id": "456",
                              "name": "Folder Name",
                              "hidden": false,
                              "access": true
                            },
                            "space": {
                              "id": "789",
                              "name": "Space Name",
                              "access": true
                            },
                            "archived": false,
                            "override_statuses": false,
                            "permission_level": "create"
                          }
                        ]
                      },
                      "description": ""
                    }
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
      "name": "Lists"
    }
  ]
}
```