# Update Group

This endpoint is used to manage [User Groups](https://docs.clickup.com/en/articles/4010016-teams-how-to-create-user-groups), which are groups of users within your Workspace.\
 \
In our API, `team_id` in the path refers to the Workspace ID, and `group_id` refers to the ID of a User Group.\
 \
**Note:** Adding a guest with view-only permissions to a User Group automatically converts them to a paid guest.\
 \
If you don't have any paid guest seats available, a new member seat is automatically added to increase the number of paid guest seats.\
 \
This incurs a prorated charge based on your billing cycle.

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
    "/v2/group/{group_id}": {
      "put": {
        "summary": "Update Group",
        "tags": [
          "User Groups"
        ],
        "description": "This endpoint is used to manage [User Groups](https://docs.clickup.com/en/articles/4010016-teams-how-to-create-user-groups), which are groups of users within your Workspace.\\\n \\\nIn our API, `team_id` in the path refers to the Workspace ID, and `group_id` refers to the ID of a User Group.\\\n \\\n**Note:** Adding a guest with view-only permissions to a User Group automatically converts them to a paid guest.\\\n \\\nIf you don't have any paid guest seats available, a new member seat is automatically added to increase the number of paid guest seats.\\\n \\\nThis incurs a prorated charge based on your billing cycle.",
        "operationId": "UpdateTeam",
        "parameters": [
          {
            "name": "group_id",
            "in": "path",
            "description": "User Group ID",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "C9C58BE9"
              ]
            }
          }
        ],
        "requestBody": {
          "description": "The group handle can be updated, which is used to @mention a User Group within the Workspace.\\\n \\\nModify Group members by using the \"add\" and \"rem\" parameters with an array of user IDs to include or exclude members.",
          "content": {
            "application/json": {
              "schema": {
                "title": "UpdateTeamrequest",
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "handle": {
                    "type": "string"
                  },
                  "members": {
                    "title": "Members2",
                    "required": [
                      "add",
                      "rem"
                    ],
                    "type": "object",
                    "properties": {
                      "add": {
                        "type": "array",
                        "items": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "description": ""
                      },
                      "rem": {
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
                        "add": [
                          123456,
                          987654
                        ],
                        "rem": [
                          159753
                        ]
                      }
                    ]
                  }
                },
                "examples": [
                  {
                    "name": "New User Group Name",
                    "handle": "newusergroupname",
                    "members": {
                      "add": [
                        123456,
                        987654
                      ],
                      "rem": [
                        159753
                      ]
                    }
                  }
                ]
              },
              "example": {
                "name": "New User Group Name",
                "handle": "newusergroupname",
                "members": {
                  "add": [
                    123456,
                    987654
                  ],
                  "rem": [
                    159753
                  ]
                }
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
                  "title": "UpdateTeamresponse",
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
                        "title": "Members3",
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
                            "id": 201,
                            "username": "Jim Halpert",
                            "email": "jim@example.com",
                            "color": "#40BC86",
                            "initials": "JH",
                            "profilePicture": null
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
                      "team_id": "123456",
                      "userid": 301828,
                      "name": "New User Group Name",
                      "handle": "newusergroupname",
                      "date_created": "1640122639829",
                      "initials": "NN",
                      "members": [
                        {
                          "id": 201,
                          "username": "Jim Halpert",
                          "email": "jim@example.com",
                          "color": "#40BC86",
                          "initials": "JH",
                          "profilePicture": null
                        },
                        {
                          "id": 202,
                          "username": "Dwight Shrute",
                          "email": "dwight@example.com",
                          "color": "#FF8600",
                          "initials": "DS",
                          "profilePicture": null
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
                  "team_id": "123456",
                  "userid": 301828,
                  "name": "New User Group Name",
                  "handle": "newusergroupname",
                  "date_created": "1640122639829",
                  "initials": "NN",
                  "members": [
                    {
                      "id": 201,
                      "username": "Jim Halpert",
                      "email": "jim@example.com",
                      "color": "#40BC86",
                      "initials": "JH",
                      "profilePicture": null
                    },
                    {
                      "id": 202,
                      "username": "Dwight Shrute",
                      "email": "dwight@example.com",
                      "color": "#FF8600",
                      "initials": "DS",
                      "profilePicture": null
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