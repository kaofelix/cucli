# Get Threaded Comments

View threaded comments. The parent comment is not included in the response.

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
    "/v2/comment/{comment_id}/reply": {
      "get": {
        "summary": "Get Threaded Comments",
        "description": "View threaded comments. The parent comment is not included in the response.",
        "tags": [
          "Comments"
        ],
        "operationId": "GetThreadedComments",
        "parameters": [
          {
            "name": "comment_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                456
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
                  "title": "GetTaskCommentsresponse",
                  "required": [
                    "comments"
                  ],
                  "type": "object",
                  "properties": {
                    "comments": {
                      "type": "array",
                      "items": {
                        "title": "Comment",
                        "required": [
                          "id",
                          "comment",
                          "comment_text",
                          "user",
                          "resolved",
                          "assignee",
                          "assigned_by",
                          "reactions",
                          "date"
                        ],
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string"
                          },
                          "comment": {
                            "type": "array",
                            "items": {
                              "title": "Comment1",
                              "required": [
                                "text"
                              ],
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "string"
                                }
                              },
                              "examples": [
                                {
                                  "text": "Task comment content"
                                }
                              ]
                            },
                            "description": ""
                          },
                          "comment_text": {
                            "type": "string"
                          },
                          "user": {
                            "title": "User2",
                            "required": [
                              "id",
                              "username",
                              "initials",
                              "email",
                              "color",
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
                              "initials": {
                                "type": "string"
                              },
                              "email": {
                                "type": "string"
                              },
                              "color": {
                                "type": "string"
                              },
                              "profilePicture": {
                                "type": "string"
                              }
                            },
                            "examples": [
                              {
                                "id": 183,
                                "username": "John Doe",
                                "initials": "JD",
                                "email": "johndoe@gmail.com",
                                "color": "#827718",
                                "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                              }
                            ]
                          },
                          "resolved": {
                            "type": "boolean"
                          },
                          "assignee": {
                            "title": "Assignee",
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
                                "id": 183,
                                "username": "John Doe",
                                "email": "example@email.com",
                                "color": "#827718",
                                "initials": "JD",
                                "profilePicture": "https://attachments.clickup.com/profilePictures/183_nx1.jpg"
                              }
                            ]
                          },
                          "assigned_by": {
                            "title": "AssignedBy",
                            "required": [
                              "id",
                              "username",
                              "initials",
                              "email",
                              "color",
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
                              "initials": {
                                "type": "string"
                              },
                              "email": {
                                "type": "string"
                              },
                              "color": {
                                "type": "string"
                              },
                              "profilePicture": {
                                "type": "string"
                              }
                            },
                            "examples": [
                              {
                                "id": 183,
                                "username": "John Doe",
                                "initials": "JD",
                                "email": "johndoe@gmail.com",
                                "color": "#827718",
                                "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                              }
                            ]
                          },
                          "reactions": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            },
                            "description": ""
                          },
                          "date": {
                            "type": "string"
                          },
                          "reply_count": {
                            "type": "string",
                            "description": "For threaded comments, `reply_count` is always 0."
                          }
                        },
                        "examples": [
                          {
                            "id": "458",
                            "comment": [
                              {
                                "text": "Task comment content"
                              }
                            ],
                            "comment_text": "Task comment content",
                            "user": {
                              "id": 183,
                              "username": "John Doe",
                              "initials": "JD",
                              "email": "johndoe@gmail.com",
                              "color": "#827718",
                              "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                            },
                            "resolved": false,
                            "assignee": {
                              "id": 183,
                              "username": "John Doe",
                              "initials": "JD",
                              "email": "johndoe@gmail.com",
                              "color": "#827718",
                              "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                            },
                            "assigned_by": {
                              "id": 183,
                              "username": "John Doe",
                              "initials": "JD",
                              "email": "johndoe@gmail.com",
                              "color": "#827718",
                              "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                            },
                            "reactions": [],
                            "date": "1568036964079",
                            "reply_count": "1"
                          }
                        ]
                      },
                      "description": ""
                    }
                  },
                  "examples": [
                    {
                      "comments": [
                        {
                          "id": "458",
                          "comment": [
                            {
                              "text": "Task comment content"
                            }
                          ],
                          "comment_text": "Task comment content",
                          "user": {
                            "id": 183,
                            "username": "John Doe",
                            "initials": "JD",
                            "email": "johndoe@gmail.com",
                            "color": "#827718",
                            "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                          },
                          "resolved": false,
                          "assignee": {
                            "id": 183,
                            "username": "John Doe",
                            "initials": "JD",
                            "email": "johndoe@gmail.com",
                            "color": "#827718",
                            "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                          },
                          "assigned_by": {
                            "id": 183,
                            "username": "John Doe",
                            "initials": "JD",
                            "email": "johndoe@gmail.com",
                            "color": "#827718",
                            "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                          },
                          "reactions": [],
                          "date": "1568036964079",
                          "reply_count": "1"
                        }
                      ]
                    }
                  ]
                },
                "example": {
                  "comments": [
                    {
                      "id": "458",
                      "comment": [
                        {
                          "text": "Task comment content"
                        }
                      ],
                      "comment_text": "Task comment content",
                      "user": {
                        "id": 183,
                        "username": "John Doe",
                        "initials": "JD",
                        "email": "johndoe@gmail.com",
                        "color": "#827718",
                        "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                      },
                      "resolved": false,
                      "assignee": {
                        "id": 183,
                        "username": "John Doe",
                        "initials": "JD",
                        "email": "johndoe@gmail.com",
                        "color": "#827718",
                        "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                      },
                      "assigned_by": {
                        "id": 183,
                        "username": "John Doe",
                        "initials": "JD",
                        "email": "johndoe@gmail.com",
                        "color": "#827718",
                        "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                      },
                      "reactions": [],
                      "date": "1568036964079",
                      "reply_count": "0"
                    }
                  ]
                }
              }
            }
          }
        },
        "deprecated": false
      }
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
      "name": "Comments"
    }
  ]
}
```