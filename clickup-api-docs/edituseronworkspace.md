# Edit User On Workspace

Update a user's name and role. \
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
    "/v2/team/{team_id}/user/{user_id}": {
      "put": {
        "summary": "Edit User On Workspace",
        "tags": [
          "Users"
        ],
        "description": "Update a user's name and role. \\\n \\\n***Note:** This endpoint is only available to Workspaces on our [Enterprise Plan](https://clickup.com/pricing).*",
        "operationId": "EditUserOnWorkspace",
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
          },
          {
            "name": "user_id",
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
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "EditUserOnWorkspacerequest",
                "required": [
                  "username",
                  "admin",
                  "custom_role_id"
                ],
                "type": "object",
                "properties": {
                  "username": {
                    "type": "string"
                  },
                  "admin": {
                    "type": "boolean"
                  },
                  "custom_role_id": {
                    "type": "integer",
                    "contentEncoding": "int32"
                  }
                },
                "examples": [
                  {
                    "username": "User Name",
                    "admin": false,
                    "custom_role_id": 998877
                  }
                ]
              },
              "example": {
                "username": "User Name",
                "admin": false,
                "custom_role_id": 998877
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "EditUserOnWorkspaceresponse",
                  "required": [
                    "member"
                  ],
                  "type": "object",
                  "properties": {
                    "member": {
                      "title": "Member7",
                      "type": "object",
                      "properties": {
                        "user": {
                          "title": "User21",
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
                              "description": "Owner = 1, Admin = 2, Member = 3, Guest = 4",
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "custom_role": {
                              "title": "CustomRole",
                              "required": [
                                "id",
                                "name"
                              ],
                              "type": "object",
                              "properties": {
                                "id": {
                                  "type": "integer",
                                  "contentEncoding": "int32"
                                },
                                "name": {
                                  "type": "string"
                                }
                              },
                              "examples": [
                                {
                                  "id": 12345,
                                  "name": "guest custom"
                                }
                              ]
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
                              "username": "User Name",
                              "email": "user@example.com",
                              "color": null,
                              "profilePicture": null,
                              "initials": "G",
                              "role": 3,
                              "custom_role": {
                                "id": 998877,
                                "name": "member custom"
                              },
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
                            "username": "User Name",
                            "email": "user@example.com",
                            "color": null,
                            "profilePicture": null,
                            "initials": "UN",
                            "role": 3,
                            "custom_role": {
                              "id": 998877,
                              "name": "member custom"
                            },
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
                      "member": {
                        "user": {
                          "id": 184,
                          "username": "User Name",
                          "email": "user@example.com",
                          "color": null,
                          "profilePicture": null,
                          "initials": "UN",
                          "role": 3,
                          "custom_role": {
                            "id": 998877,
                            "name": "member custom"
                          },
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
                  "member": {
                    "user": {
                      "id": 184,
                      "username": "User Name",
                      "email": "user@example.com",
                      "color": null,
                      "profilePicture": null,
                      "initials": "G",
                      "role": 3,
                      "custom_role": {
                        "id": 998877,
                        "name": "member custom"
                      },
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
      "name": "Users"
    }
  ]
}
```