# Get Task's Time in Status

View how long a task has been in each status. The Total time in Status ClickApp must first be enabled by the Workspace owner or an admin.

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
    "/v2/task/{task_id}/time_in_status": {
      "get": {
        "summary": "Get Task's Time in Status",
        "tags": [
          "Tasks"
        ],
        "description": "View how long a task has been in each status. The Total time in Status ClickApp must first be enabled by the Workspace owner or an admin.",
        "operationId": "GetTask'sTimeinStatus",
        "parameters": [
          {
            "name": "task_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "9hz"
              ]
            }
          },
          {
            "name": "custom_task_ids",
            "in": "query",
            "description": "If you want to reference a task by it's custom task id, this value must be `true`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "examples": [
                true
              ]
            }
          },
          {
            "name": "team_id",
            "in": "query",
            "description": "When the `custom_task_ids` parameter is set to `true`, the Workspace ID must be provided using the `team_id` parameter.\n \\\nFor example: `custom_task_ids=true&team_id=123`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          },
          {
            "name": "Content-Type",
            "in": "header",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "const": "application/json",
              "type": "string",
              "examples": [
                "application/json"
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
                  "title": "GetTasksTimeinStatusresponse",
                  "required": [
                    "current_status",
                    "status_history"
                  ],
                  "type": "object",
                  "properties": {
                    "current_status": {
                      "title": "CurrentStatus",
                      "required": [
                        "status",
                        "color",
                        "total_time"
                      ],
                      "type": "object",
                      "properties": {
                        "status": {
                          "type": "string"
                        },
                        "color": {
                          "type": "string"
                        },
                        "total_time": {
                          "title": "TotalTime",
                          "required": [
                            "by_minute",
                            "since"
                          ],
                          "type": "object",
                          "properties": {
                            "by_minute": {
                              "type": "integer",
                              "contentEncoding": "int64"
                            },
                            "since": {
                              "type": "string"
                            }
                          },
                          "examples": [
                            {
                              "by_minute": 21708,
                              "since": "1604004423494"
                            }
                          ]
                        }
                      },
                      "examples": [
                        {
                          "status": "open",
                          "color": "#d3d3d3",
                          "total_time": {
                            "by_minute": 21708,
                            "since": "1604004423494"
                          }
                        }
                      ]
                    },
                    "status_history": {
                      "type": "array",
                      "items": {
                        "title": "StatusHistory",
                        "required": [
                          "status",
                          "color",
                          "type",
                          "total_time",
                          "orderindex"
                        ],
                        "type": "object",
                        "properties": {
                          "status": {
                            "type": "string"
                          },
                          "color": {
                            "type": "string"
                          },
                          "type": {
                            "type": "string"
                          },
                          "total_time": {
                            "title": "TotalTime",
                            "required": [
                              "by_minute",
                              "since"
                            ],
                            "type": "object",
                            "properties": {
                              "by_minute": {
                                "type": "integer",
                                "contentEncoding": "int64"
                              },
                              "since": {
                                "type": "string"
                              }
                            },
                            "examples": [
                              {
                                "by_minute": 21708,
                                "since": "1604004423494"
                              }
                            ]
                          },
                          "orderindex": {
                            "type": "integer",
                            "contentEncoding": "int32"
                          }
                        },
                        "examples": [
                          {
                            "status": "open",
                            "color": "#d3d3d3",
                            "type": "open",
                            "total_time": {
                              "by_minute": 21707,
                              "since": "1604004423494"
                            },
                            "orderindex": 0
                          }
                        ]
                      },
                      "description": ""
                    }
                  },
                  "examples": [
                    {
                      "current_status": {
                        "status": "open",
                        "color": "#d3d3d3",
                        "total_time": {
                          "by_minute": 21708,
                          "since": "1604004423494"
                        }
                      },
                      "status_history": [
                        {
                          "status": "open",
                          "color": "#d3d3d3",
                          "type": "open",
                          "total_time": {
                            "by_minute": 21707,
                            "since": "1604004423494"
                          },
                          "orderindex": 0
                        },
                        {
                          "status": "active status",
                          "color": "#5CF1D4",
                          "type": "custom",
                          "total_time": {
                            "by_minute": 23274,
                            "since": "1602607941692"
                          },
                          "orderindex": 4
                        }
                      ]
                    }
                  ]
                },
                "example": {
                  "current_status": {
                    "status": "open",
                    "color": "#d3d3d3",
                    "total_time": {
                      "by_minute": 21708,
                      "since": "1604004423494"
                    }
                  },
                  "status_history": [
                    {
                      "status": "open",
                      "color": "#d3d3d3",
                      "type": "open",
                      "total_time": {
                        "by_minute": 21707,
                        "since": "1604004423494"
                      },
                      "orderindex": 0
                    },
                    {
                      "status": "active status",
                      "color": "#5CF1D4",
                      "type": "custom",
                      "total_time": {
                        "by_minute": 23274,
                        "since": "1602607941692"
                      },
                      "orderindex": 4
                    }
                  ]
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
      "name": "Tasks"
    }
  ]
}
```