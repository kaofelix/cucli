# Get Workspace seats

View the used, total, and available member and guest seats for a Workspace.

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
    "/v2/team/{team_id}/seats": {
      "get": {
        "summary": "Get Workspace seats",
        "tags": [
          "Workspaces"
        ],
        "description": "View the used, total, and available member and guest seats for a Workspace.",
        "operationId": "GetWorkspaceseats",
        "parameters": [
          {
            "name": "team_id",
            "in": "path",
            "description": "Workspace ID",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string"
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
                  "title": "GetWorkspaceseatsresponse",
                  "required": [
                    "members",
                    "guests"
                  ],
                  "type": "object",
                  "properties": {
                    "members": {
                      "title": "Members",
                      "required": [
                        "filled_members_seats",
                        "total_member_seats",
                        "empty_member_seats"
                      ],
                      "type": "object",
                      "properties": {
                        "filled_members_seats": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "total_member_seats": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "empty_member_seats": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        }
                      },
                      "examples": [
                        {
                          "filled_members_seats": 9,
                          "total_member_seats": 9,
                          "empty_member_seats": 0
                        }
                      ]
                    },
                    "guests": {
                      "title": "Guests",
                      "required": [
                        "filled_guest_seats",
                        "total_guest_seats",
                        "empty_guest_seats"
                      ],
                      "type": "object",
                      "properties": {
                        "filled_guest_seats": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "total_guest_seats": {
                          "oneOf": [
                            {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            {
                              "type": "string",
                              "enum": [
                                "Infinity"
                              ]
                            }
                          ]
                        },
                        "empty_guest_seats": {
                          "oneOf": [
                            {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            {
                              "type": "string",
                              "enum": [
                                "Infinity"
                              ]
                            }
                          ]
                        }
                      },
                      "examples": [
                        {
                          "filled_guest_seats": 2,
                          "total_guest_seats": 50,
                          "empty_guest_seats": 48
                        },
                        {
                          "filled_guest_seats": 2,
                          "total_guest_seats": "Infinity",
                          "empty_guest_seats": "Infinity"
                        }
                      ]
                    }
                  },
                  "examples": [
                    {
                      "members": {
                        "filled_members_seats": 9,
                        "total_member_seats": 9,
                        "empty_member_seats": 0
                      },
                      "guests": {
                        "filled_guest_seats": 2,
                        "total_guest_seats": 50,
                        "empty_guest_seats": 48
                      }
                    },
                    {
                      "members": {
                        "filled_members_seats": 9,
                        "total_member_seats": 9,
                        "empty_member_seats": 0
                      },
                      "guests": {
                        "filled_guest_seats": 2,
                        "total_guest_seats": "Infinity",
                        "empty_guest_seats": "Infinity"
                      }
                    }
                  ]
                },
                "example": {
                  "members": {
                    "filled_members_seats": 9,
                    "total_member_seats": 9,
                    "empty_member_seats": 0
                  },
                  "guests": {
                    "filled_guest_seats": 2,
                    "total_guest_seats": 50,
                    "empty_guest_seats": 48
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
      "name": "Workspaces"
    }
  ]
}
```