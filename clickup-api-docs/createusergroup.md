# Create Group

This endpoint creates a [User Group](https://docs.clickup.com/en/articles/4010016-teams-how-to-create-user-groups) within a Workspace.\
 \
User Groups are used to organize and manage users within a Workspace.\
 \
In the API documentation, `team_id` refers to the Workspace ID, and `group_id` refers to the User Group ID.\
 \
**Note:** Adding a guest with view-only permissions to a Team automatically converts them to a paid guest.\
 \
If no paid guest seats are available, an additional member seat will be added, increasing the number of paid guest seats.\
 \
This change incurs a prorated charge based on the billing cycle.

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
    "/v2/team/{team_id}/group": {
      "post": {
        "summary": "Create Group",
        "tags": [
          "User Groups"
        ],
        "description": "This endpoint creates a [User Group](https://docs.clickup.com/en/articles/4010016-teams-how-to-create-user-groups) within a Workspace.\\\n \\\nUser Groups are used to organize and manage users within a Workspace.\\\n \\\nIn the API documentation, `team_id` refers to the Workspace ID, and `group_id` refers to the User Group ID.\\\n \\\n**Note:** Adding a guest with view-only permissions to a Team automatically converts them to a paid guest.\\\n \\\nIf no paid guest seats are available, an additional member seat will be added, increasing the number of paid guest seats.\\\n \\\nThis change incurs a prorated charge based on the billing cycle.",
        "operationId": "CreateUserGroup",
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
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "CreateTeamrequest",
                "required": [
                  "name",
                  "members"
                ],
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "handle": {
                    "type": "string"
                  },
                  "members": {
                    "type": "array",
                    "items": {
                      "type": "integer",
                      "contentEncoding": "int32"
                    },
                    "description": ""
                  }
                },
                "examples": [
                  {
                    "name": "New team name",
                    "handle": "newteamname",
                    "members": [
                      123456,
                      987654
                    ]
                  }
                ]
              },
              "example": {
                "name": "New User Group name",
                "handle": "newusergroupname",
                "members": [
                  123456,
                  987654
                ]
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
                  "title": "CreateTeamresponse",
                  "required": [
                    "id",
                    "team_id",
                    "userid",
                    "name",
                    "handle",
                    "date_created",
                    "initials",
                    "members",
                    "avatar"
                  ],
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "team_id": {
                      "type": "string"
                    },
                    "userid": {
                      "type": "integer",
                      "contentEncoding": "int32"
                    },
                    "name": {
                      "type": "string"
                    },
                    "handle": {
                      "type": "string"
                    },
                    "date_created": {
                      "type": "string"
                    },
                    "initials": {
                      "type": "string"
                    },
                    "members": {
                      "type": "array",
                      "items": {
                        "title": "Members1",
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
                            "type": "string"
                          }
                        },
                        "examples": [
                          {
                            "id": 185,
                            "username": "Sam",
                            "email": "sam@example.com",
                            "color": "#4169E1",
                            "initials": "S",
                            "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                          }
                        ]
                      },
                      "description": ""
                    },
                    "avatar": {
                      "title": "Avatar",
                      "required": [
                        "attachment_id",
                        "color",
                        "source",
                        "icon"
                      ],
                      "type": "object",
                      "properties": {
                        "attachment_id": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "color": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "source": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "icon": {
                          "type": [
                            "string",
                            "null"
                          ]
                        }
                      },
                      "examples": [
                        {
                          "attachment_id": null,
                          "color": null,
                          "source": null,
                          "icon": null
                        }
                      ]
                    }
                  },
                  "examples": [
                    {
                      "id": "4bfdfcec-6f4f-40a7-b0d6-22660d51870d",
                      "team_id": "301540",
                      "userid": 301828,
                      "name": "User group",
                      "handle": "usergroup",
                      "date_created": "1640122639829",
                      "initials": "U",
                      "members": [
                        {
                          "id": 185,
                          "username": "Sam",
                          "email": "sam@example.com",
                          "color": "#4169E1",
                          "initials": "S",
                          "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                        },
                        {
                          "id": 186,
                          "username": "Alex",
                          "email": "alex@example.com",
                          "color": "#4169E1",
                          "initials": "A",
                          "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                        }
                      ],
                      "avatar": {
                        "attachment_id": null,
                        "color": null,
                        "source": null,
                        "icon": null
                      }
                    }
                  ]
                },
                "example": {
                  "id": "4bfdfcec-6f4f-40a7-b0d6-22660d51870d",
                  "team_id": "301540",
                  "userid": 301828,
                  "name": "User group",
                  "handle": "usergroup",
                  "date_created": "1640122639829",
                  "initials": "U",
                  "members": [
                    {
                      "id": 185,
                      "username": "Sam",
                      "email": "sam@example.com",
                      "color": "#4169E1",
                      "initials": "S",
                      "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                    },
                    {
                      "id": 186,
                      "username": "Alex",
                      "email": "alex@example.com",
                      "color": "#4169E1",
                      "initials": "A",
                      "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                    }
                  ],
                  "avatar": {
                    "attachment_id": null,
                    "color": null,
                    "source": null,
                    "icon": null
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
      "name": "User Groups"
    }
  ]
}
```