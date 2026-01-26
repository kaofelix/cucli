# Get tracked time

***Note:** This is a legacy time tracking endpoint. We recommend using the Time Tracking API endpoints to manage time entries.*

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
    "/v2/task/{task_id}/time": {
      "get": {
        "summary": "Get tracked time",
        "tags": [
          "Time Tracking (Legacy)"
        ],
        "description": "***Note:** This is a legacy time tracking endpoint. We recommend using the Time Tracking API endpoints to manage time entries.*",
        "operationId": "Gettrackedtime",
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
                "9hv"
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
                  "title": "Gettrackedtimeresponse",
                  "required": [
                    "data"
                  ],
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "array",
                      "items": {
                        "title": "Datum",
                        "required": [
                          "user",
                          "time",
                          "intervals"
                        ],
                        "type": "object",
                        "properties": {
                          "user": {
                            "title": "User13",
                            "required": [
                              "id",
                              "username",
                              "email",
                              "color",
                              "initials",
                              "profilePicture"
                            ],
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "integer",
                                "contentEncoding": "int32"
                              },
                              "username": {
                                "type": "string"
                              },
                              "email": {
                                "type": "string"
                              },
                              "color": {
                                "type": "string"
                              },
                              "initials": {
                                "type": "string"
                              },
                              "profilePicture": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              }
                            },
                            "examples": [
                              {
                                "id": 1,
                                "username": "John Doe",
                                "email": "johndoe@gmail.com",
                                "color": "#795548",
                                "initials": "JD",
                                "profilePicture": null
                              }
                            ]
                          },
                          "time": {
                            "type": "integer",
                            "contentEncoding": "int32"
                          },
                          "intervals": {
                            "type": "array",
                            "items": {
                              "title": "Interval",
                              "required": [
                                "id",
                                "start",
                                "end",
                                "time",
                                "source",
                                "date_added"
                              ],
                              "type": "object",
                              "properties": {
                                "id": {
                                  "type": "string"
                                },
                                "start": {
                                  "type": [
                                    "string",
                                    "null"
                                  ]
                                },
                                "end": {
                                  "type": [
                                    "string",
                                    "null"
                                  ]
                                },
                                "time": {
                                  "type": "string"
                                },
                                "source": {
                                  "type": "string"
                                },
                                "date_added": {
                                  "type": "string"
                                }
                              },
                              "examples": [
                                {
                                  "id": "318",
                                  "start": null,
                                  "end": null,
                                  "time": "1000000",
                                  "source": "chrome",
                                  "date_added": "1569983937761"
                                }
                              ]
                            },
                            "description": ""
                          }
                        },
                        "examples": [
                          {
                            "user": {
                              "id": 1,
                              "username": "John Doe",
                              "email": "johndoe@gmail.com",
                              "color": "#795548",
                              "initials": "JD",
                              "profilePicture": null
                            },
                            "time": 1000000,
                            "intervals": [
                              {
                                "id": "318",
                                "start": null,
                                "end": null,
                                "time": "1000000",
                                "source": "chrome",
                                "date_added": "1569983937761"
                              }
                            ]
                          }
                        ]
                      },
                      "description": ""
                    }
                  },
                  "examples": [
                    {
                      "data": [
                        {
                          "user": {
                            "id": 1,
                            "username": "John Doe",
                            "email": "johndoe@gmail.com",
                            "color": "#795548",
                            "initials": "JD",
                            "profilePicture": null
                          },
                          "time": 1000000,
                          "intervals": [
                            {
                              "id": "318",
                              "start": null,
                              "end": null,
                              "time": "1000000",
                              "source": "chrome",
                              "date_added": "1569983937761"
                            }
                          ]
                        }
                      ]
                    }
                  ]
                },
                "example": {
                  "data": [
                    {
                      "user": {
                        "id": 1,
                        "username": "John Doe",
                        "email": "johndoe@gmail.com",
                        "color": "#795548",
                        "initials": "JD",
                        "profilePicture": null
                      },
                      "time": 1000000,
                      "intervals": [
                        {
                          "id": "318",
                          "start": null,
                          "end": null,
                          "time": "1000000",
                          "source": "chrome",
                          "date_added": "1569983937761"
                        }
                      ]
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
      "name": "Time Tracking (Legacy)"
    }
  ]
}
```