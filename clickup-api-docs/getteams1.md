# Get Groups

This endpoint is used to view [User Groups](https://docs.clickup.com/en/articles/4010016-teams-how-to-create-user-groups) in your Workspace.\
 \
In our API documentation, `team_id` refers to the ID of a Workspace, and `group_id` refers to the ID of a User Group.

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
    "/v2/group": {
      "get": {
        "summary": "Get Groups",
        "tags": [
          "User Groups"
        ],
        "description": "This endpoint is used to view [User Groups](https://docs.clickup.com/en/articles/4010016-teams-how-to-create-user-groups) in your Workspace.\\\n \\\nIn our API documentation, `team_id` refers to the ID of a Workspace, and `group_id` refers to the ID of a User Group.",
        "operationId": "GetTeams1",
        "parameters": [
          {
            "name": "team_id",
            "in": "query",
            "description": "Workspace ID",
            "required": true,
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
            "name": "group_ids",
            "in": "query",
            "description": "Enter one or more User Group IDs to retrieve information about specific User Group.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string",
              "examples": [
                "C9C58BE9-7C73-4002-A6A9-310014852858"
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
                  "title": "GetTeamsresponse",
                  "required": [
                    "groups"
                  ],
                  "type": "object",
                  "properties": {
                    "groups": {
                      "type": "array",
                      "items": {
                        "title": "Group",
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
                            "userid": 301123,
                            "name": "product team",
                            "handle": "product",
                            "date_created": "1640122639829",
                            "initials": "PT",
                            "members": [
                              {
                                "id": 183,
                                "username": "Jerry",
                                "email": "jerry@example.com",
                                "color": "#40BC86",
                                "initials": "J",
                                "profilePicture": null
                              },
                              {
                                "id": 184,
                                "username": "Sam",
                                "email": "sam@example.com",
                                "color": "#FF8600",
                                "initials": "S",
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
                      "description": ""
                    }
                  },
                  "examples": [
                    {
                      "groups": [
                        {
                          "id": "4bfdfcec-6f4f-40a7-b0d6-22660d51870d",
                          "team_id": "123456",
                          "userid": 301123,
                          "name": "product team",
                          "handle": "product",
                          "date_created": "1640122639829",
                          "initials": "PT",
                          "members": [
                            {
                              "id": 183,
                              "username": "Jerry",
                              "email": "jerry@example.com",
                              "color": "#40BC86",
                              "initials": "J",
                              "profilePicture": null
                            },
                            {
                              "id": 184,
                              "username": "Sam",
                              "email": "sam@example.com",
                              "color": "#FF8600",
                              "initials": "S",
                              "profilePicture": null
                            }
                          ],
                          "avatar": {
                            "attachment_id": null,
                            "color": null,
                            "source": null,
                            "icon": null
                          }
                        },
                        {
                          "id": "fd31be63-41f2-4320-9043-9786fdf643d6",
                          "team_id": "301540",
                          "userid": 301828,
                          "name": "HR department",
                          "handle": "hr-dept",
                          "date_created": "1627087990293",
                          "initials": "HD",
                          "members": [
                            {
                              "id": 183,
                              "username": "Jerry",
                              "email": "jerry@example.com",
                              "color": "#40BC86",
                              "initials": "J",
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
                    }
                  ]
                },
                "example": {
                  "groups": [
                    {
                      "id": "4bfdfcec-6f4f-40a7-b0d6-22660d51870d",
                      "team_id": "123456",
                      "userid": 301123,
                      "name": "product managers",
                      "handle": "product",
                      "date_created": "1640122639829",
                      "initials": "PT",
                      "members": [
                        {
                          "id": 183,
                          "username": "Jerry",
                          "email": "jerry@example.com",
                          "color": "#40BC86",
                          "initials": "J",
                          "profilePicture": null
                        },
                        {
                          "id": 184,
                          "username": "Sam",
                          "email": "sam@example.com",
                          "color": "#FF8600",
                          "initials": "S",
                          "profilePicture": null
                        }
                      ],
                      "avatar": {
                        "attachment_id": null,
                        "color": null,
                        "source": null,
                        "icon": null
                      }
                    },
                    {
                      "id": "fd31be63-41f2-4320-9043-9786fdf643d6",
                      "team_id": "301540",
                      "userid": 301828,
                      "name": "HR department",
                      "handle": "hr-dept",
                      "date_created": "1627087990293",
                      "initials": "HD",
                      "members": [
                        {
                          "id": 183,
                          "username": "Jerry",
                          "email": "jerry@example.com",
                          "color": "#40BC86",
                          "initials": "J",
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