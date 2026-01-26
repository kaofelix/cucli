# Remove Guest From Task

Revoke a guest's access to a task. \
 \
***Note:** This endpoint is only available to Workspaces on our [Enterprise Plan](https://clickup.com/pricing).*

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
    "/v2/task/{task_id}/guest/{guest_id}": {
      "delete": {
        "summary": "Remove Guest From Task",
        "tags": [
          "Guests"
        ],
        "description": "Revoke a guest's access to a task. \\\n \\\n***Note:** This endpoint is only available to Workspaces on our [Enterprise Plan](https://clickup.com/pricing).*",
        "operationId": "RemoveGuestFromTask",
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
                "c04"
              ]
            }
          },
          {
            "name": "guest_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                403
              ]
            }
          },
          {
            "name": "include_shared",
            "in": "query",
            "description": "Exclude details of items shared with the guest by setting this parameter to `false`. By default this parameter is set to `true`.",
            "required": false,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "examples": [
                false
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
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "RemoveGuestFromTaskresponse",
                  "required": [
                    "guest"
                  ],
                  "type": "object",
                  "properties": {
                    "guest": {
                      "title": "Guest2",
                      "required": [
                        "user",
                        "invited_by",
                        "can_see_time_spent",
                        "can_see_time_estimated",
                        "can_edit_tags",
                        "shared"
                      ],
                      "type": "object",
                      "properties": {
                        "user": {
                          "title": "User7",
                          "required": [
                            "id",
                            "username",
                            "email",
                            "color",
                            "profilePicture",
                            "initials",
                            "role",
                            "last_active",
                            "date_joined",
                            "date_invited"
                          ],
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "username": {
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "email": {
                              "type": "string"
                            },
                            "color": {
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "profilePicture": {
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "initials": {
                              "type": "string"
                            },
                            "role": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "last_active": {
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "date_joined": {
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "date_invited": {
                              "type": "string"
                            }
                          },
                          "examples": [
                            {
                              "id": 184,
                              "username": null,
                              "email": "guest@example.com",
                              "color": null,
                              "profilePicture": null,
                              "initials": "G",
                              "role": 4,
                              "last_active": null,
                              "date_joined": null,
                              "date_invited": "1583358383412"
                            }
                          ]
                        },
                        "invited_by": {
                          "title": "InvitedBy",
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "color": {
                              "type": "string"
                            },
                            "username": {
                              "type": "string"
                            },
                            "email": {
                              "type": "string"
                            },
                            "initials": {
                              "type": "string"
                            },
                            "profilePicture": {
                              "type": "string"
                            }
                          },
                          "examples": [
                            {
                              "id": 183,
                              "color": "#827718",
                              "username": "Jerry",
                              "email": "jerry@example.com",
                              "initials": "J",
                              "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                            }
                          ]
                        },
                        "can_see_time_spent": {
                          "type": "boolean"
                        },
                        "can_see_time_estimated": {
                          "type": "boolean"
                        },
                        "can_edit_tags": {
                          "type": "boolean"
                        },
                        "shared": {
                          "title": "Shared",
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
                                "type": "string"
                              },
                              "description": ""
                            },
                            "folders": {
                              "type": "array",
                              "items": {
                                "type": "string"
                              },
                              "description": ""
                            }
                          },
                          "examples": [
                            {
                              "tasks": [],
                              "lists": [],
                              "folders": []
                            }
                          ]
                        }
                      },
                      "examples": [
                        {
                          "user": {
                            "id": 184,
                            "username": null,
                            "email": "guest@example.com",
                            "color": null,
                            "profilePicture": null,
                            "initials": "G",
                            "role": 4,
                            "last_active": null,
                            "date_joined": null,
                            "date_invited": "1583358383412"
                          },
                          "invited_by": {
                            "id": 183,
                            "color": "#827718",
                            "username": "Jerry",
                            "email": "jerry@example.com",
                            "initials": "J",
                            "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                          },
                          "can_see_time_spent": true,
                          "can_see_time_estimated": true,
                          "can_edit_tags": true,
                          "shared": {
                            "tasks": [],
                            "lists": [],
                            "folders": []
                          }
                        }
                      ]
                    }
                  },
                  "examples": [
                    {
                      "guest": {
                        "user": {
                          "id": 184,
                          "username": null,
                          "email": "guest@example.com",
                          "color": null,
                          "profilePicture": null,
                          "initials": "G",
                          "role": 4,
                          "last_active": null,
                          "date_joined": null,
                          "date_invited": "1583358383412"
                        },
                        "invited_by": {
                          "id": 183,
                          "color": "#827718",
                          "username": "Jerry",
                          "email": "jerry@example.com",
                          "initials": "J",
                          "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                        },
                        "can_see_time_spent": true,
                        "can_see_time_estimated": true,
                        "can_edit_tags": true,
                        "shared": {
                          "tasks": [],
                          "lists": [],
                          "folders": []
                        }
                      }
                    }
                  ]
                },
                "example": {
                  "guest": {
                    "user": {
                      "id": 184,
                      "username": null,
                      "email": "guest@example.com",
                      "color": null,
                      "profilePicture": null,
                      "initials": "G",
                      "role": 4,
                      "last_active": null,
                      "date_joined": null,
                      "date_invited": "1583358383412"
                    },
                    "invited_by": {
                      "id": 183,
                      "color": "#827718",
                      "username": "Jerry",
                      "email": "jerry@example.com",
                      "initials": "J",
                      "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                    },
                    "can_see_time_spent": true,
                    "can_see_time_estimated": true,
                    "can_edit_tags": true,
                    "shared": {
                      "tasks": [],
                      "lists": [],
                      "folders": []
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
      "name": "Guests"
    }
  ]
}
```